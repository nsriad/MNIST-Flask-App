# MNIST Digit Classifier Web App

This is a simple web application that uses a Convolutional Neural Network (CNN) model trained on the MNIST dataset to predict handwritten digits (0–9). The model is exported in ONNX format and deployed with Flask.

- In the following directory, open linux terminal.
- Install necessary libraries given in the "requirements.txt" file.
- After installing all the required libraries, run "python app.py"
- Click or copy the local host url something like "http://127.0.0.1:5000/"

---

## Project Structure

mnist_flask_app/  
│
├── app.py  
├── mnist_cnn.onnx               ← exported ONNX model  
├── samples_images/              ← Random 5 MNIST images  
├── WebPage/  
│   └── index.html               ← HTML for upload & prediction  
├── utils.py                     ← helper functions  
├── requirements.txt             ← libraries needed  
└── README.md                    ← how to run the app  
