from flask import Flask, render_template, request, jsonify
import numpy as np
import onnxruntime as ort
from utils import preprocess_image, predict_digit
from PIL import Image
import os

app = Flask(__name__, template_folder='WebPage')

# Load ONNX model
onnx_session = ort.InferenceSession("mnist_cnn.onnx")

from flask import send_from_directory

@app.route('/sample_images/<filename>')
def serve_sample_image(filename):
    return send_from_directory('sample_images', filename)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})

    file = request.files['file']

    try:
        image = Image.open(file).convert('L')  # Grayscale
        image = image.resize((28, 28))         # Resize

        input_tensor = preprocess_image(image)
        prediction, confidence = predict_digit(onnx_session, input_tensor)

        return jsonify({
            'prediction': int(prediction),
            'confidence': {str(i): round(float(prob), 4) for i, prob in enumerate(confidence)}
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

