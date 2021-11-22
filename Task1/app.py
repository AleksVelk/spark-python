from flask import Flask,jsonify

from minio_functions import minio_list_objects
from consumer import load_data

app = Flask(__name__)

set_bucket_name = "fhdsghf"

@app.route("/")
def root():
    return "<h1>Task 1</h1><br><a href=""http://127.0.0.1:5000/kafka_load_to_minio"">Click to Generate Minio files</a><br><a href=""http://127.0.0.1:5000/list_files"">Click to List the files uploaded to Minio</a>"

@app.route("/kafka_load_to_minio",methods=['GET'])
def get():
    load_data(set_bucket_name=set_bucket_name)
    lists = minio_list_objects(bucket_name=set_bucket_name)
    return jsonify({"file lists":lists})

@app.route("/list_files",methods=['GET'])
def get_lists():
    lists = minio_list_objects(bucket_name=set_bucket_name)
    return jsonify({"file lists":lists})
    