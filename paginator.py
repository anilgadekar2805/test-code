import boto3
from datetime import datetime

# Initialize the S3 client
s3 = boto3.client('s3')

# Specify the bucket name
bucket_name = 'your_bucket_name'

# Define the start and end date
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 4, 17)

# Get a list of all object versions in the bucket, handling pagination
delete_markers = []
paginator = s3.get_paginator('list_object_versions')
for page in paginator.paginate(Bucket=bucket_name):
    for version in page.get('Versions', []):
        if 'IsDeleteMarker' in version and version['IsDeleteMarker']:
            delete_marker_date = version['LastModified']
            if start_date <= delete_marker_date <= end_date:
                delete_markers.append(version)

# Print the delete marker objects
for delete_marker in delete_markers:
    print(delete_marker)
