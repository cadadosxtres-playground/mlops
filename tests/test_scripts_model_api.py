import unittest
from scripts.model_api import *
from unittest.mock import patch
import json

### First row from file data/heart.csv
test_data = { "data": {"tobacco": [12],
        "ldl": [5.73],
        "adiposity": [23.11],
        "famhist" : [1],
        "typea" : [49],
        "obesity" :  [25.3],
        "alcohol" : [97.2],
        "age" : [52] },
        "chd_expected": [1]
        }




class TestScriptModelAPI(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app.test_client()
        self.app.testing = True
    
    def test_pingAPI(self):
        print("testing prediction API")
        response = self.app.get("/ping")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'hello!!')

    @patch.dict(os.environ, {'MODEL_FILE_PATH': 'model/heart_model.pkl'})
    def test_predictionAPI(self):
        print("testing prediction API")
        response = self.app.post("/prediction", json=test_data['data'])
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertEquals(response_data, {'message': f'Result: {test_data["chd_expected"]}'})