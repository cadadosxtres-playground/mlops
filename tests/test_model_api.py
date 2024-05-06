import unittest
from ml_service.util.heart_model import HeartModel

from ml_service.cli import *
from ml_service.model_api import *
import json

data = {"tobacco": [0.0],
        "ldl": [6],
        "adiposity": [22.5],
        "famhist" : [1],
        "typea" : [55],
        "obesity" :  [29.14],
        "alcohol" : [3.81],
        "age" : [38] }

class TestHeartPredictionModel(unittest.TestCase):

    def setUp(self) -> None:
        self.heartModel = HeartModel()
        self.app = app.test_client()
        self.app.testing = True
    
    def test_predictionCLI(self):
        print("testing model prediction")
        self.assertIsNotNone(self.heartModel.prediction(data)) 


    def test_predictionAPI(self):
        print("testing prediction API")
        response = self.app.post("/prediction", json=data)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertIsNotNone(response_data)

    def test_pingAPI(self):
        print("testing prediction API")
        response = self.app.get("/ping")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'hello!!')