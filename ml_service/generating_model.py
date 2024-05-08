import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

history_mapping = {'Absent': 0,'Present': 1}

class GenHeartModel():
    """
    A class for predicting Heart Disease using Logistic Regression
    https://github.com/eduai-repo/ML-Demo/blob/main/2%20Classification/2.%20One%20with%20Heart%20Disease%20Prediction.ipynb
    """
    def __init__(self,data_file_path) -> None:
        ### Loading and transforming the data
        try:
            self.data = pd.read_csv(data_file_path)
        except FileNotFoundError:
            print(f"ERROR!! loading data file: {data_file_path} does't exists")
        except Exception as e:
            print(f"ERROR!!: Unexpected error loading file; {data_file_path}, error: {e}")
        print(f'Loaded file {data_file_path}')
        self.data["famhist"] = self.data["famhist"].map(history_mapping)
        self.mode_score = 0
        self.mode_score_test = 0
        self.model = None
    

    def get_data_columns(self):
        return self.data.columns.to_list()

    def generating_model(self, model_file_path):
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
        try:
            with open(model_file_path, 'wb') as model_pkl:
                pickle.dump(self.model,model_pkl)
            return model_file_path
        except FileNotFoundError:
            print(f"ERROR!! opening data file: {model_file_path} does't exists")
        except Exception as e:
            print(f"ERROR!!: Unexpected error opening file; {model_file_path}, error: {e}")


