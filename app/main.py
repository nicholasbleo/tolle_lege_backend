from flask import Flask
import os
import json

DATA_FOLDER = '/data/'

app = Flask(__name__)
app.config['DATA_FOLDER'] = DATA_FOLDER

@app.route("/")
def index():
    return "Index for the Tolle Lege backend service."

@app.route("/text-data/<filename>")
def get_text_data(filename):
    data_path = os.path.join(app.static_folder, 'data', filename)
    with open(data_path) as f:
        json_data = json.load(f)
    return json_data