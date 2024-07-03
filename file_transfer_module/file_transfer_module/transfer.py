import os
import mimetypes
import boto3
from dotenv import load_dotenv
from google.cloud import storage


class awsConnection:
    def getS3Connection_enVariables(self):
        aws_access_Id = os.getenv('aws_access_Id')
        aws_access_pwd = os.getenv('aws_access_pwd')
        s3 =  boto3.client('s3',aws_access_key_id = aws_access_Id,aws_secret_access_key = aws_access_pwd) 
        return s3
    
def upload_to_s3(file_path, bucket_name):
    aws_conn = awsConnection()
    s3 = aws_conn.getS3Connection_enVariables()
    file_key = os.path.relpath(file_path)
    s3.upload_file(file_path, bucket_name, file_key)

def upload_to_gcs(file_path, bucket_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(os.path.relpath(file_path))
    blob.upload_from_filename(file_path)

def transfer_files(directory_path, s3_bucket_name, gcs_bucket_name, s3_file_types, gcs_file_types):
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_type, _ = mimetypes.guess_type(file_path)
            if file_type:
                if any(file_name.lower().endswith(ext) for ext in s3_file_types):
                    upload_to_s3(file_path, s3_bucket_name)
                    print(f"Uploaded {file_path} to S3 bucket '{s3_bucket_name}'")
                elif any(file_name.lower().endswith(ext) for ext in gcs_file_types):
                    upload_to_gcs(file_path, gcs_bucket_name)
                    print(f"Uploaded {file_path} to GCS bucket '{gcs_bucket_name}'")
                else:
                    print(f"Skipping {file_path} - Unsupported file type")
            else:
                print(f"Skipping {file_path} - Unknown file type")

# Example usage
if __name__ == '__main__':
    load_dotenv()
    directory_path = '/path/to/your/directory'
    s3_bucket_name = 'your-s3-bucket-name'
    gcs_bucket_name = 'your-gcs-bucket-name'
    s3_file_types = ['.jpg', '.png', '.svg', '.webp','mp3', 'mp4', 'mpeg4', 'wmv', '3gp', 'webm']
    gcs_file_types = ['.doc', '.docx', '.csv', '.pdf']

    transfer_files(directory_path, s3_bucket_name, gcs_bucket_name, s3_file_types, gcs_file_types)
