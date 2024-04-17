import unittest
from datetime import datetime, timedelta, timezone
from unittest.mock import patch, MagicMock
import boto3

def list_objects_v2_mock(Bucket, Prefix):
    # Mock response with sample objects
    sample_objects = [
        {'Key': 'prefix1/object1', 'LastModified': datetime(2024, 4, 15, 12, 0, tzinfo=timezone.utc), 'DeleteMarker': True},
        {'Key': 'prefix1/object2', 'LastModified': datetime(2024, 4, 16, 8, 0, tzinfo=timezone.utc), 'DeleteMarker': True},
        {'Key': 'prefix2/object3', 'LastModified': datetime(2024, 4, 16, 10, 0, tzinfo=timezone.utc), 'DeleteMarker': True}
    ]
    return {'Contents': sample_objects}

class TestS3ObjectDeletion(unittest.TestCase):

    @patch('boto3.client')
    def test_objects_filtered_by_date_range(self, mock_client):
        # Mock S3 client and its response
        mock_s3 = MagicMock()
        mock_s3.list_objects_v2.side_effect = list_objects_v2_mock
        mock_client.return_value = mock_s3
        
        # Set the date range for testing
        from_date = datetime(2024, 4, 15, 0, 0, tzinfo=timezone.utc)
        to_date = datetime(2024, 4, 16, 23, 59, 59, tzinfo=timezone.utc)
        
        # Call the function under test
        filtered_objects = get_filtered_objects(from_date, to_date)
        
        # Assert that the correct number of objects are filtered
        self.assertEqual(len(filtered_objects), 2)
        
        # Assert that objects are filtered correctly
        self.assertIn({'Key': 'prefix1/object1', 'LastModified': datetime(2024, 4, 15, 12, 0, tzinfo=timezone.utc), 'DeleteMarker': True}, filtered_objects)
        self.assertIn({'Key': 'prefix1/object2', 'LastModified': datetime(2024, 4, 16, 8, 0, tzinfo=timezone.utc), 'DeleteMarker': True}, filtered_objects)

if __name__ == '__main__':
    unittest.main()
