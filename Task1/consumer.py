from os import close
from flask.json import load
from kafka import KafkaConsumer
import json
import time

from minio_functions import minio_uploader

def open_topic():
    consumer = KafkaConsumer(
        "TestTopic",
        bootstrap_servers='localhost:9092',
        auto_offset_reset ='earliest',
        group_id="consumer-group-a")
    return consumer

def load_data(set_bucket_name):
    consumer = open_topic()

    f_no = 1
    i = 0
    data =""
    
    for msg in consumer:  
        if(f_no >2):
            break
        else:
            data = data +'\n'+ str(msg.value)
            i += 1
            if(i==10):
                with open(f'C:\\Installations\\data{f_no}.txt','w') as f:
                    f.write(data)
                f.close
                minio_uploader(bucket_name=set_bucket_name,file_name=f'data{f_no}.txt')
                i=0
                f_no+=1
                data =""