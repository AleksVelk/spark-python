# Request 1:

1. Create a python script to generate dummy data
2. Create a service to load the data to object storage using API service
3. API should have 2 routes. One for reading the data and one for listing the available files
4. Load data into object storage through API in chunks 
5. After a certain amount of records from the Kafka topic, you target the route for loading data to object storage


# Solution:

Build python script to populate user data from Faker library with following fields first_name, Last_name, address, and created_at.
Dummy data generated will be streamed to the Kafka topic using the Kafka producer script.
Consumer script will listen on the Kafka topic and pull and upload the data to a local txt file and at the same time will be uploaded to Minio testing server  "play.min.io".
The flask API will have two routes one for listing the files already uploaded to Minio and one for loading the data to the MinIO server.


# How to Run:
1. You need to have a zookeeper and Kafka server running on your local machine
2. Run the producer.py to generate dummy data. The script will upload data to the Kafka topic until it is manually stopped.
3. Run the app.py to access the API
4. Route /kafka_load_to_minio will load two files locally (each having maximum of 10 dummy users) and upload them under MinIO bucket(the bucket is set in the app.py)
5. route /list_files will produce the names of the already uploaded files under MinIO bucket
