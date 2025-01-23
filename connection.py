from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# Enable CORS for specific origins
CORS(app, resources={r"/*": {"origins": ["http://localhost:8080"]}})



if __name__ == "__main__":
    port = 5000

    app.run(host="0.0.0.0", port=port)