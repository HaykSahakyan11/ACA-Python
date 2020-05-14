import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('display.max_rows', 999)
pd.set_option('display.max_columns', 999)


def problem1():
    name = ["name1", "name2", "name3", "name4", "name5"]
    surname = ["surname1", "surname2", "surname3", "surname4", "surname5"]
    sex = ["men", "women", "women", "men", "men"]
    status = ["student", "tutor", "student", "student", "student"]
    age_group = ["20-30", "30-35", "20-30", "20-30", "20-30"]

    columns = ["name", "surname", "sex", "status", "age_group"]

    df = pd.DataFrame()

    for col in columns:
        df[col] = locals().get("{}".format(col))
    return df.set_index(["name", "surname"])


def problem2():
    netflix = pd.read_csv('netflix_titles.csv')
    return netflix[(netflix.release_year > 2015) &
                   (netflix.cast.str.contains("Kevin Spacey|Leonardo DiCaprio"))].reset_index(drop=True)


def problem3():
    netflix = pd.read_csv('netflix_titles.csv')
    new_netflix = pd.DataFrame()
    new_netflix[["director", "num_mov/dir"]] = netflix.groupby(["director"]).count()["show_id"].reset_index()
    return pd.merge(netflix, new_netflix, on="director")


def problem4():
    netflix = pd.read_csv('netflix_titles.csv')
    netflix["cast"] = netflix['cast'].str.split(',')
    return netflix.explode("cast")


def problem5(path='netflix_titles.csv'):
    netflix = pd.read_csv(path)
    netflix.cast.fillna("Noone", inplace=True)

    sorted_netflix = netflix[(netflix.type == "Movie") & (netflix.cast.str.contains("Antonio Banderas"))]
    sorted_netflix = sorted_netflix.sort_values("release_year").reset_index(drop=True)
    sorted_netflix['duration'] = sorted_netflix['duration'].apply(lambda x: int(x.split()[0]))

    plot_df = sorted_netflix[['duration', "release_year"]].groupby(["release_year"]).sum().reset_index()
    plt.scatter(plot_df["release_year"], plot_df["duration"], label="minutes/year")
    plt.ylabel("Minutes")
    plt.xlabel("Year")
    plt.title("Minutes starred by Antonio Banderas per year")
    plt.legend()
    plt.show()
    return sorted_netflix
