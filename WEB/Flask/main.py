import sqlite3
from configparser import ConfigParser
from flask import (
    Flask,
    render_template,
    url_for,
    request,
    redirect,
    flash
)

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

config = ConfigParser()
config.read("config.ini")
db_name = config.get('db_info', 'db_name')
db_table_name = config.get('db_info', 'db_table')


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
    return render_template('index.html', main_text="Home page")


@app.route('/success/<name>')
def success(name):
    return render_template('pattern.html', main_text="Welcome {} jan".format(name))


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        user_first_name = request.form.get('user_first_name')
        user_last_name = request.form.get('user_last_name')
        user_gender = request.form.get('user_gender')
        user_age = request.form.get('user_age')

        create_update_database(user_first_name, user_last_name, user_age, user_gender)
        return redirect(url_for('success', name='{}_{}'.format(user_first_name, user_last_name)))
    return render_template('create.html')


def create_update_database(first_name, last_name, age, gender):
    db = sqlite3.connect('{}'.format(config.get('db_info', 'db_name')))
    cursor = db.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS {} (
             first_name TEXT,
             last_name TEXT,
             gender TEXT,
             age INTEGER
    )""".format(db_table_name))

    cursor.execute(
        f"INSERT INTO {db_table_name} VALUES(?,?,?,?)",
        (first_name, last_name, gender, age)
    )
    db.commit()
    db.close()


@app.route('/search', methods=['GET'])
def get_search():
    if request.method == 'GET':
        search_param = request.args.get('search_param')

        if search_param is not None:

            if not search_param:
                flash('Please fill search parameter', 'error')
                return redirect(url_for('get_search'))

            db = sqlite3.connect(f'{db_name}')
            cursor = db.cursor()
            try:
                print('0000000000')
                cursor.execute(f'SELECT * FROM {db_table_name} WHERE first_name = "{search_param}"')
                searched_data = cursor.fetchall()
                print(searched_data, "data")
                cursor.execute(f'SELECT * FROM {db_table_name} WHERE last_name = "{search_param}"')
                searched_data.extend(cursor.fetchall())

            except Exception as err:
                print(err)
                flash('Irrelevant database', 'error')
                return redirect(url_for('get_search'))
            else:
                if searched_data:
                    return render_template('search.html', persons=searched_data)
                else:
                    flash('No matching', 'error')
                    return redirect(url_for('get_search'))

    return render_template('search.html')


@app.route('/search', methods=['POST'])
def post_search():
    return render_template('search.html')


if __name__ == "__main__":
    app.run()
