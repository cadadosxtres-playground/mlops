import unittest


from ml_service.generating_model import GenHeartModel


import pathlib as pl


class TestGenHeartModel(unittest.TestCase):
    """
    Testing out class GenHeartModel 
    """
    def setUp(self) -> None:
        self.model_file_path = 'model/heart_model.pkl'
        self.data_file_path = 'data/heart.csv'
        self.genHearModel = GenHeartModel(data_file_path=self.data_file_path)

    def assertFileExists(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError(f"File doesn not exists {path}")



    def test_loading_data(self):
        """
        Testing out that data are loaded when GenHeartModel object is created
        """
        self.assertIsNotNone(self.genHearModel.get_data_columns(),msg="Data loaded")


    def test_generating_model(self):
        model_file_path = self.genHearModel.generating_model(self.model_file_path)

        self.assertFileExists(model_file_path)
        
if __name__ == '__main__':
    unittest.main()