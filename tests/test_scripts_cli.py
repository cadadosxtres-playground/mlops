import unittest
import os
from unittest.mock import patch
import sys
from io import StringIO
from scripts.cli import *
import pathlib as pl


class TestScriptCli(unittest.TestCase):
    """
    Testing out cli.py
    """
    def setUp(self) -> None:
        os.environ['DATA_FILE_PATH'] = 'data/heart.csv'
        self.model_file_path = os.environ['MODEL_FILE_PATH'] = 'model/heart_model.pkl'
          

    def assertFileExists(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError(f"File doesn not exists {path}")


    @patch.dict(os.environ, {'DATA_FILE_PATH': 'data/heart.csv', 'MODEL_FILE_PATH': 'model/heart_model.pkl'})
    def test_using_env_variables_cli(self):
        main()
        self.assertFileExists(os.environ.get('MODEL_FILE_PATH'))

    @patch('sys.argv', ["scripts/cli.py","--data-file", 'data/heart.csv', "--model-path", 'model/heart_model.pkl'])
    def test_parse_args(self):
        args = parse_args()
        self.assertEqual(args.data_file_path, 'data/heart.csv')
        self.assertEqual(args.model_file_path, 'model/heart_model.pkl')

    @patch('sys.stdout', new_callable=StringIO)
    def test_using_conmmand_line_arguments_main(self, mock_stdout):
        with patch.object(sys, 'argv', ["scripts/cli.py","--data-file", 'data/heart.csv', "--model-path", 'model/heart_model.pkl']):
            main()


if __name__ == '__main__':
    unittest.main()