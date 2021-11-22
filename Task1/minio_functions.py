from minio import Minio
from minio.error import S3Error

def open_client():
    client = Minio(
        "play.min.io",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
    )
    return client

def minio_uploader(file_name,bucket_name,file_path="C:\\Installations\\"):
    client = open_client()

    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)

    client.fput_object(
        bucket_name, file_name, file_path+file_name,
    )

def minio_list_objects(bucket_name):
    file_names = []
    client = open_client()
    object = client.list_objects(bucket_name)
    for o in object:
        file_names.append(o.object_name)
    return file_names