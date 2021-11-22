# Requests for task 2

# Deploy a Spark Cluster (standalone, single node is quite sufficient) in Docker on local machine:

* Install docker on my local machine
* Download spark image from bitnami 

Commands:

curl -LO https://raw.githubusercontent.com/bitnami/bitnami-docker-spark/master/docker-compose.yml
docker-compose up -d

connect to spark-shell

./spark-shell spark://d5b13498e6dd:7077

# Load the dataset from the link (https://www.kaggle.com/promptcloud/careerbuilder-job-listing-2020) using Spark inside the job:

* Using the command i copied the file from my local machine to the docker container 

docker cp marketing_sample_for_careerbuilder_usa-careerbuilder_job_listing__20200401_20200630__30k_data.ldjson d5b13498e6dd:/opt/bitnami/spark/marketing_sample.ldjson


# Apply the following transformation on top of the data:

Scala scripts can be found under name query1 to query5
