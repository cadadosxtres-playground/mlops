from ml_service.util.generating_model import GenHeartModel


### Generating model

def main():
    print("Generating model")
    heart = GenHeartModel()
    print(f'Generated model {heart.generating_model()}')

    

if __name__ == '__main__':
    main()