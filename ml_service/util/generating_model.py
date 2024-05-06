import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
import os

history_mapping = {'Absent': 0,'Present': 1}
MODEL_FILE_PATH=os.environ["MODEL_FILE_PATH"]
DATA_FILE_PATH=os.environ["DATA_FILE_PATH"]

class GenHeartModel():

    def __init__(self) -> None:
        ### Loading and transforming the data
        self.data = pd.read_csv(DATA_FILE_PATH)
        print(f'Loaded file {DATA_FILE_PATH}')
        self.data["famhist"] = self.data["famhist"].map(history_mapping)
        self.mode_score = 0
        self.mode_score_test = 0
        self.model = None
    

    def get_data_columns(self):
        return self.data.columns.to_list()

    def generating_model(self):
        """
        This model is a LogisticRegresion
            input: 'tobacco','ldl','adiposity','famhist','typea','obesity', 'alcohol','age'
            output: chd (int [1|0])
        """
        X=self.data[['tobacco','ldl','adiposity','famhist','typea','obesity', 'alcohol','age']].values
        y=self.data[['chd']].values 
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
        self.model = LogisticRegression( C=100, penalty='l2',solver='liblinear')
        self.model.fit(X_train, y_train)
        self.mode_score = self.model.score(X_train, y_train)
        self.mode_score_test = self.model.score(X_test,y_test)
        with open(MODEL_FILE_PATH, 'wb') as model_pkl:
            pickle.dump(self.model,model_pkl)
        return MODEL_FILE_PATH


