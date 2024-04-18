import unittest
from datetime import datetime, timezone
from your_module import get_file_name, group_by_prefix

class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.s3_filter_data = [
            {"file_name": "AAA/BBBB", "LastModified": datetime(2024, 4, 17, 22, 9, tzinfo=timezone.utc)},
            {"file_name": "CCC/XYZ/PPP.3520240417225140", "LastModified": datetime(2024, 4, 17, 22, 9, tzinfo=timezone.utc)},
            {"file_name": "PPP/EEE", "LastModified": datetime(2024, 4, 17, 22, 9, tzinfo=timezone.utc)},
            {"file_name": "XXXX/YYYY/ZZZZZ.164679", "LastModified": datetime(2024, 4, 17, 22, 9, tzinfo=timezone.utc)},
            {"file_name": "SSS/VVV/QQQQ.185450", "LastModified": datetime(2024, 4, 17, 22, 9, tzinfo=timezone.utc)},
            {"file_name": "WWW/SSS/XXX.20240418100849609", "LastModified": datetime(2024, 4, 17, 22, 9, tzinfo=timezone.utc)},
            {"file_name": "DDDD/DDD/EEEEE.20240418040846389", "LastModified": datetime(2024, 4, 17, 22, 9, tzinfo=timezone.utc)},
            {"file_name": "AAA/DDDD-11/AAA.20240418040846389.NOK", "LastModified": datetime(2024, 4, 17, 22, 9, tzinfo=timezone.utc)}
        ]

    def test_get_file_name(self):
        self.assertEqual(get_file_name("PPP/EEE"), "EEE")
        self.assertEqual(get_file_name("AAA/DDDD-11/AAA.20240418040846389.NOK"), "AAA/DDDD-11/AAA")
        # Add more test cases for various scenarios

    def test_group_by_prefix(self):
        result = group_by_prefix(self.s3_filter_data)
        self.assertEqual(result['AAA'], ['BBBB', 'DDD-11/AAA'])
        self.assertEqual(result['CCC/XYZ'], ['PPP'])
        # Add more test cases for various scenarios

if __name__ == '__main__':
    unittest.main()
