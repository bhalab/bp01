from google.cloud import storage
import json

def upload_blob(bucket_name, blob_text, destination_blob_name, context):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_string(blob_text)

    print('File {} uploaded to bucket {}.'.format(
        destination_blob_name,
        bucket_name))

def cloud_function(event,context):
    if not ('.json' in event['name']):
        BUCKET_NAME = event['bucket']
        BLOB_NAME = 'cloud_fn_output.json'
        EVENT = json.dumps(event)
    
        upload_blob(BUCKET_NAME, EVENT, BLOB_NAME, context)
