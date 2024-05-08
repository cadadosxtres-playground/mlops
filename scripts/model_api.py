from flask import Flask, request, jsonify
from ml_service.heart_model import HeartModel
import os





app = Flask(__name__)

@app.route('/prediction', methods=['POST'])
def predictionAPI():
    if request.method == 'POST':
        model_file_path=os.environ["MODEL_FILE_PATH"]
        if not model_file_path:
            return jsonify({"error": f"environment variable MODEL_FILE_PATH not defined "})
        else:
            heartModel = HeartModel(model_file_path)
        # Get JSON data from the request
        json_data = request.json
        
        # Process the JSON data
        if json_data:
            result = heartModel.prediction(json_data)
            message = f"Result: {result}"
            return jsonify({'message': message}), 200
        else:
            return jsonify({'error': 'No JSON data received'}), 400

@app.route('/ping', methods=['GET'])
def ping():
    return 'hello!!', 200

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)