from google.cloud import storage


def upload_blob(bucket_name, file, destination_blob_name):
    """
    Upload file to gcb bucket
    """

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(destination_blob_name)

    blob.upload_from_file(file)

    print(f'file {file.filename} uploaded to destination {destination_blob_name}')
     