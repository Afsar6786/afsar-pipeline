"""
Example: Using azure_utils for uploading & downloading files
"""

from afsar_pipeline import azure_utils

# Replace with your Azure Storage connection string & details
STORAGE_CONNECTION_STRING = "your_connection_string_here"
CONTAINER_NAME = "your-container"
UPLOAD_FILE_PATH = "sample.csv"
BLOB_NAME = "sample.csv"
DOWNLOAD_FILE_PATH = "downloaded_sample.csv"

# Upload a file
azure_utils.upload_to_blob(STORAGE_CONNECTION_STRING, CONTAINER_NAME, BLOB_NAME, UPLOAD_FILE_PATH)

# Download the same file back
azure_utils.download_from_blob(STORAGE_CONNECTION_STRING, CONTAINER_NAME, BLOB_NAME, DOWNLOAD_FILE_PATH)