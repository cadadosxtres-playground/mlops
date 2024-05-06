import unittest


from ml_service.util.generating_model import GenHeartModel
from ml_service.util.heart_model import MODEL_FILE_PATH
from ml_service.cli import main

import pathlib as pl


class TestTrainingModel(unittest.TestCase):
    def setUp(self) -> None:
        self.heartPredictModel = GenHeartModel()

    def assertFileExists(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError(f"File doesn not exists {path}")



    def test_loading_data(self):
        """
        Testing out that data are loaded when GenHeartModel object is created
        """
        self.assertIsNotNone(self.heartPredictModel.get_data_columns())


    def test_generating_model(self):
        model_file_path = self.heartPredictModel.generating_model()

        self.assertFileExists(model_file_path)
        
    def test_CLI(self):
        main()
        self.assertFileExists(MODEL_FILE_PATH)