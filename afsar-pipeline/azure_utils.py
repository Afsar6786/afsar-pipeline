from azure.storage.blob import BlobServiceClient
import pandas as pd
from io import StringIO

def read_csv_from_blob(connection_string, container_name, blob_name):
    """Read CSV from Azure Blob into Pandas."""
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    data = blob_client.download_blob().readall().decode("utf-8")
    return pd.read_csv(StringIO(data))


def upload_to_blob(storage_connection_string, container_name, blob_name, local_file_path):
    """
    Uploads a local file to Azure Blob Storage.
    """
    blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    with open(local_file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
    print(f"Uploaded {local_file_path} to {container_name}/{blob_name}")


def download_from_blob(storage_connection_string, container_name, blob_name, download_file_path):
    """
    Downloads a file from Azure Blob Storage.
    """
    blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    with open(download_file_path, "wb") as file:
        file.write(blob_client.download_blob().readall())
    print(f"Downloaded {container_name}/{blob_name} to {download_file_path}")