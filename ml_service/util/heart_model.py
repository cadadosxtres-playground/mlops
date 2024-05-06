import pickle
import os
import pandas as pd

MODEL_FILE_PATH=os.environ["MODEL_FILE_PATH"]

class HeartModel():
    """
    A class 
    """
    def __init__(self) -> None:
        self.model = pickle.load(open(MODEL_FILE_PATH, 'rb'))
    
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
