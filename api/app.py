from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request
    return jsonify({'prediction': ""})


@app.route('/', methods=['GET'])
def Test():
    return 'Welcome to, Test App API!'

