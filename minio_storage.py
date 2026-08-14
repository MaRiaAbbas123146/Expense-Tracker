import boto3
from botocore.client import Config

# Connect to MinIO
s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:9000",
    aws_access_key_id="minioadmin",
    aws_secret_access_key="minioadmin",
    config=Config(signature_version="s3v4"),
    region_name="us-east-1"
)

BUCKET_NAME = "expense-tracker"


# List objects in bucket
def list_objects():
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)

    if "Contents" not in response:
        print("Bucket is empty.")
        return

    for obj in response["Contents"]:
        print(obj["Key"])


# Upload a file
def upload_file(file_path, object_name):
    s3.upload_file(
        file_path,
        BUCKET_NAME,
        object_name
    )

    print("File uploaded successfully!")


# Download a file
def download_file(object_name, file_path):
    s3.download_file(
        BUCKET_NAME,
        object_name,
        file_path
    )

    print("File downloaded successfully!")


# Delete an object
def delete_file(object_name):
    s3.delete_object(
        Bucket=BUCKET_NAME,
        Key=object_name
    )

    print("File deleted successfully!")



# Test connection
if __name__ == "__main__":

    delete_file("downloaded_testfile.txt")

    print("\nObjects in MinIO bucket:")
    list_objects()
# if __name__ == "__main__":

#     upload_file("testfile.txt", "testfile.txt")

#     print("\nObjects in MinIO bucket:")
#     list_objects()

    # download_file(
    #     "testfile.txt",
    #     "downloaded_testfile.txt"
    # )
