from google.cloud import storage


def upload_blob(file):
    """
        Upload file to gcb bucket
    """

    # define the name and location/fileName to sort the pdf
    bucket_name = 'pdfsusdata'

    destination_blob_name = f'{file.filename}'

    print(f'file: {file.filename} to be uploaded to destination {destination_blob_name}')

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(destination_blob_name)

    file.seek(0)
   
    blob.upload_from_file(file, content_type='application/pdf')

    print(f'file: {file.filename} uploaded to destination {destination_blob_name}')


def findPath(entityName) -> str:
    bucket_name = 'pdfsusdata'
    return f'https://storage.googleapis.com/{bucket_name}/{entityName}'
