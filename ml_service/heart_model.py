import pickle
import pandas as pd

class HeartModel():
    """
    A class to predict Heart Disease based on model loaded from a pickle file
    """
    def __init__(self,model_file_path) -> None:
        try:
            self.model = pickle.load(open(model_file_path, 'rb'))
        except FileNotFoundError:
            print(f"ERROR!!! File: {model_file_path} doesn't exist")
        except Exception as e:
            print(f"ERROR!!! Unexpected error happened loading file: {model_file_path}, msg: {e}")
    
    def prediction(self, data):
        try:
            df = pd.DataFrame(data)
            # IMPORTANT!!!: Defining column order for the model input prediction
            desired_order= ['tobacco','ldl','adiposity','famhist','typea','obesity', 'alcohol','age']
            df = df.reindex(columns=desired_order)
            print(f'Predicting data for input: {df.to_json()}')
            prediction = self.model.predict(df.values)
            print(f"Result: {prediction}")
            return prediction
        except Exception as e:
            print(f'Error {e}')            
