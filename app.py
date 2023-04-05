from flask import Flask, request, jsonify
import os
import time
from datetime import datetime, date, timedelta
# from utils import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    response = {
        'status': 'OK',
        'message': 'Connect Karachi is LIVE! Data dedo bhaiiiiiii!!!'
    }
    return response


if __name__ == '__main__':
    app.run(threaded=True, port=5000)