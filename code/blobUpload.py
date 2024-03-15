from google.cloud import storage


def upload_blob(bucket_name, file, destination_blob_name):
    """
        Upload file to gcb bucket
    """
    print(f'file: {file.filename} to be uploaded to destination {destination_blob_name}')

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(destination_blob_name)

    blob.upload_from_file(file, content_type='application/pdf')

    print(f'file: {file.filename} uploaded to destination {destination_blob_name}')

 