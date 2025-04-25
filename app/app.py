import os
import numpy as np
import cv2
import tensorflow as tf
from flask import Flask, request, render_template, jsonify
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load the trained model
MODEL_PATH = os.path.join('models', 'SatCoverClassifier.keras')
model = load_model(MODEL_PATH)

class_mapping = {
    0: 'AnnualCrop', 1: 'Forest', 2: 'HerbaceousVegetation',
    3: 'Highway', 4: 'Industrial', 5: 'Pasture',
    6: 'PermanentCrop', 7: 'Residential', 8: 'River',
    9: 'SeaLake'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    # Read and preprocess the image
    img_bytes = file.read()
    nparr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Resize to match model input
    resized_img = tf.image.resize(img_rgb, (64, 64))
    
    # Normalize and expand dims for batch
    normalized_img = resized_img / 255.0
    input_data = np.expand_dims(normalized_img, 0)
    
    # Make prediction
    predictions = model.predict(input_data)
    
    # Get top 3 predictions
    top3_indices = np.argsort(predictions[0])[-3:][::-1]
    results = []
    
    for idx in top3_indices:
        results.append({
            'class': class_mapping[idx],
            'confidence': float(predictions[0][idx] * 100)
        })
    
    return jsonify({
        'prediction': results[0]['class'],
        'confidence': results[0]['confidence'],
        'top3': results
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)