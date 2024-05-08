from ml_service.generating_model import GenHeartModel
import os
import argparse
import sys


# Parsing arguments from command line
def parse_args(manual_args=None):
    existArgs=lambda y: len(list(filter(lambda x: y in x, sys.argv)))
    parser = argparse.ArgumentParser(description="Generate heart model")
    parser.add_argument("--data-file", dest="data_file_path", type=str, help="Path to data file")
    parser.add_argument("--model-path", dest="model_file_path", type=str, help="Path to model file")
    
    ### This check below is to avoid an exception running unittest
    if any([existArgs('data'),existArgs('model'),manual_args]):
        args = parser.parse_args()
    else:
        args = None
    return args


# Validating arguments
def validating_arguments(args):
    data_file_path, model_file_path = os.environ.get("DATA_FILE_PATH"), os.environ.get("MODEL_FILE_PATH")
    # No arguments and environment variable have been set
    if not any([args, data_file_path, model_file_path]):
        raise Exception("ERROR!! Any argument or Environment variable has not been setup")
    # Environment variables have bin set
    if args:
        return args
    # if only environment variable has been set
    if all([data_file_path, model_file_path]):
        arguments = ["--data-file", data_file_path, "--model-path", model_file_path]
        parser = argparse.ArgumentParser(description="Generate heart model")
        parser.add_argument("--data-file", dest="data_file_path", type=str, help="Path to data file")
        parser.add_argument("--model-path", dest="model_file_path", type=str, help="Path to model file")
        mArgs = parser.parse_args(arguments)
        return mArgs
    else:
        raise Exception(f"ERROR!! Unexpected error has happened parsing environment variables: {arguments}")
    


### Generating model

def main():
    try:
        # TODO Refactoring parse_args and validating_arguments with the intention of having only one function
        # Parsing arguments
        args = parse_args()

        #Validating arguments
        args = validating_arguments(args)
        print("Generating model")
        genHeartModel = GenHeartModel(data_file_path=args.data_file_path)
        print(f'Generated model {genHeartModel.generating_model(model_file_path=args.model_file_path)}')
    except Exception as e:
        print(f"ERROR!!! Unexpected error has happened: {e}")

    

if __name__ == '__main__':
    main()