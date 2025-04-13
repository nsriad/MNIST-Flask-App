import numpy as np

def preprocess_image(image):
    image = np.array(image).astype(np.float32)
    image = image / 255.0  # normalize to 0-1
    image = np.expand_dims(np.expand_dims(image, 0), 0)  # shape: [1, 1, 28, 28]
    return image

def predict_digit(session, input_tensor):
    inputs = {session.get_inputs()[0].name: input_tensor}
    outputs = session.run(None, inputs)
    logits = outputs[0]
    predicted_class = np.argmax(logits)
    probabilities = np.exp(logits[0]) / np.sum(np.exp(logits[0]))
    return predicted_class, probabilities

