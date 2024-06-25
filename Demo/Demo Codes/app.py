from flask import Flask, request, jsonify
import numpy as np

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from flask_cors import CORS
from tensorflow.keras.models import load_model
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Server-side configuration
app = Flask(__name__)
CORS(app)

# Ensure necessary NLTK resources are available
nltk.download('stopwords')

# Load Arabic stop words
stop_words = set(stopwords.words('arabic'))

# Tokenizer parameters
max_vocab = 10000

# Define a new tokenizer instance for each request
tokenizer = None  # Global variable

# Load the LSTM model
lstm_model = load_model('lstm_model.h5')

# Define preprocessing function
def preprocess_text(text):
  tokens = word_tokenize(text)
  filtered_tokens = [word for word in tokens if word not in stop_words]
  return ' '.join(filtered_tokens)

# Define function to handle prediction request
@app.route('/predict', methods=['POST'])
def predict():
  global tokenizer  # Access global tokenizer instance

  data = request.json

  # Extract and validate text input
  text = data.get('text')
  if not text:
    return jsonify({'error': 'Text is required'}), 400

  # Preprocess the text
  preprocessed_text = preprocess_text(text)

  # Tokenize the text (using a new instance for each request)
  tokenizer = Tokenizer(num_words=max_vocab)
  tokenizer.fit_on_texts([preprocessed_text])
  sequences = tokenizer.texts_to_sequences([preprocessed_text])
  padded_sequences = pad_sequences(sequences, maxlen=128, padding='post')

  # Make prediction using the model
  prediction = lstm_model.predict(padded_sequences)
  predicted_label = np.argmax(prediction, axis=1)[0]

  response = {
    'converted_text': text,  # Assuming no conversion happens
    'prediction': prediction.tolist()[0]  # Convert prediction to a list
  }
  return jsonify(response)

if __name__ == '__main__':
  app.run(debug=True)


