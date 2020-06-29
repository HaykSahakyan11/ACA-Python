import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from pymongo import MongoClient
from configparser import ConfigParser
from sklearn import metrics
from matplotlib import pyplot as plt

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


# The goal of this class is
# - to get data (from database which parameters were set in config.ini file)
# - to prepare data for further processing (data_cleaning, data_transformation methods)
# - to plot some useful analytic information (Price/Area and Price/Area regression)
# - to train models(LinearRegression,RandomForestRegressor) using consequent data
# - to get feedback from trainings (RMSE, score)
# - to make a decision about model that will be used for prediction
# - to improve model using new train data


class HousePrices:
    # Initializes all variables that will be used, called in prospect and
    # runs method __runs to get workable instance for first stage
    # some variables values getting processes can be smarter (columns_to_remove, columns_names_transform),
    # but for now we use hard coding )))
    def __init__(self):
        self.config = ConfigParser()
        self.client = MongoClient()
        self.rand_forest_regr = RandomForestRegressor(criterion='mse', n_estimators=1000, random_state=0, n_jobs=-1)
        self.linear_regr = LinearRegression()
        self.best_learned = None
        self.min_data_length_for_prediction = None
        self.rmse_linear_regr = None
        self.rmse_rand_forest_regr = None
        self.columns_to_remove = ['region', 'Unnamed: 0', 'url']
        self.columns_names_transform = ['district', 'condition', 'street', 'building_type']

        self.__run()

    # Reads config.ini file to get user parameters such database name, collection name
    # converts collection to pandas dataframe for further processes
    # extract data for method __plot
    # calls __train method
    def __run(self):
        try:
            self.config.read("config.ini")
            database = self.client[f"{self.config.get('mongodb', 'database_name')}"]
            self.collection = database[f"{self.config.get('mongodb', 'collection_name')}"]

            data = pd.DataFrame(list(self.collection.find({}))).drop("_id", axis=1)
        except Exception as err:
            raise ("Incorrect Database information", err)

        self.prices = data['price']
        self.area = data['area']
        data = self.data_cleaning(data)
        data = self.data_transformation(data)

        self.__plot()

        self.__train(data)

    def data_cleaning(self, data):
        return data.drop(labels=self.columns_to_remove, axis=1)

    def data_transformation(self, data):
        le = preprocessing.LabelEncoder()
        for col in self.columns_names_transform:
            le.fit(data[f'{col}'])
            data[f'{col}'] = le.transform(data[f'{col}'])
        return data

    # Gets data from caller (this method can be called by __rune method when initializing
    # or by user after initialization),
    # checks from where or how it was called by looking on "best_learned".
    # Initially "best_learned" has value None as no-one is learned. This mean we get data from our database,
    # so it is not need to update database with already existing data
    # Otherwise ("best_learned" has value different to "None") updates database by data.
    def __train(self, data):
        if self.best_learned:
            self.database_update(data)

        # Splits data to 2 parts - data for training(train_data) and data for testing(test)
        # "test" as "train_data", also will be split.
        # Second part of "test" ("test_y" eg. test right answers) than will be used for training also,
        # to improve models
        train_data, test = train_test_split(data, test_size=0.2, random_state=5)

        train_X = train_data.drop(['price'], axis=1)
        train_y = train_data['price']

        test_X = test.drop(['price'], axis=1)
        test_y = test['price']

        self.min_data_length_for_prediction = len(train_X.columns)

        score_rand_forest_regr = self.rand_forest_regr_learning(train_X, train_y, test_X, test_y)
        score_linear_regr = self.linear_regr_learning(train_X, train_y, test_X, test_y)

        if self.rmse_rand_forest_regr > self.rmse_linear_regr:
            self.best_learned = self.rand_forest_regr
        else:
            self.best_learned = self.linear_regr

        print(f'RMSE RandomForestRegressor {self.rmse_rand_forest_regr}')
        print(f'RMSE LinearRegression {self.rmse_linear_regr}')
        print(f'Scores for LinearRegression {score_linear_regr}')
        print(f'Scores for RandomForestRegressor {score_rand_forest_regr}')
        print(f'For prediction will be used {str(self.best_learned).split("(")[0]}')

    def rand_forest_regr_learning(self, train_X, train_y, test_X, test_y):
        self.rand_forest_regr.fit(train_X, train_y)
        y_pred = self.rand_forest_regr.predict(test_X)
        self.rmse_rand_forest_regr = round(metrics.mean_squared_error(test_y, y_pred, squared=False), 2)
        train_score = round(self.rand_forest_regr.score(train_X, train_y) * 100, 2)
        self.rand_forest_regr.fit(test_X, test_y)
        test_score = round(self.rand_forest_regr.score(test_X, test_y) * 100, 2)
        return train_score, test_score

    def linear_regr_learning(self, train_X, train_y, test_X, test_y):
        self.linear_regr.fit(train_X, train_y)
        y_pred = self.linear_regr.predict(test_X)
        self.rmse_linear_regr = round(metrics.mean_squared_error(test_y, y_pred, squared=False), 2)
        train_score = round(self.linear_regr.score(train_X, train_y) * 100, 2)
        self.linear_regr.fit(test_X, test_y)
        test_score = round(self.linear_regr.score(test_X, test_y) * 100, 2)
        return train_score, test_score

    def database_update(self, data):
        self.collection.insert_many(data.to_dict('records'))
        print("Database updated")

    def predict(self, test):
        if isinstance(test, (np.ndarray, pd.Series, list)):
            assert len(test) == self.min_data_length_for_prediction, \
                "Length of data did not match to requirements"
            return self.best_learned.predict([test])
        if isinstance(test, pd.DataFrame):
            try:
                data_pred = self.data_cleaning(test)
                data_pred = self.data_transformation(data_pred)
                return self.best_learned.predict([data_pred])
            except Exception as err:
                print(err)
        raise ValueError("incorrect prediction data")

    def __plot(self):
        plt.style.use('fivethirtyeight')
        x = self.area
        y = self.prices

        plt.plot(x, y, 'o', linewidth=2, markersize=3, label="Price/Area")

        m, b = np.polyfit(x, y, 1)
        plt.plot(x, m * x + b, color='red', label="Price/Area Lin. Reg.", linewidth=2)

        plt.grid(True)
        plt.legend(loc="upper left")
        plt.title("House prices (USD) by area")
        plt.ylabel("Prices")
        plt.xlabel("Area")
        plt.tight_layout()
        plt.show()


a = HousePrices()
