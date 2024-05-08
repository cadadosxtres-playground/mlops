import unittest
from ml_service.heart_model import HeartModel



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


class TestHearModel(unittest.TestCase):

    def setUp(self) -> None:
        self.model_file_path = 'model/heart_model.pkl'

    def test_prediction(self):
        print("testing model prediction")
        heartModel = HeartModel(self.model_file_path)
        result = heartModel.prediction(test_data['data'])
        
        self.assertEquals(result, test_data['chd_expected'], msg=f"Result: {result}, chd_expected: {test_data['chd_expected']}")     