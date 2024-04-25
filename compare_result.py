import unittest
from your_module import compare_rvs_and_s3

class TestCompareRVSandS3(unittest.TestCase):
    
    def setUp(self):
        self.s3_bucket_filename_input = ['DDD.N59R11.CCCVLIST.FFF12', 'DDD.N59R11.CCCVLIST.FFF12',
                                         'DDD.N59R11.CCCVLIST.FWS12',
                                         'DFF.N59VWI.DPD.B0.53', 'DDD.N59R11.CYCVDET.FFF12',
                                         'DDD.N59R11.CYCVDET.FFF12',
                                         'DFF.N59K8N.DPV1LOG.D1212', 'AAA.BBB.CCC.11', 'AAA.BBB.CCC.11']
        self.other_web_filename_input = ['DDD.N59R11.CCCVLIST.FFF12', 'DDD.N59R11.CCCVLIST.FWS12', 'DDS.N59R11.DPVRS.DS',
                                         'DDS.N59R11.DPVRS.DS',
                                         'DFF.N59VWI.DPD.B0.53', 'DDD.N59R11.CYCVDET.FFF12', 'DDD.N59R11.CYCVDET.FFF12',
                                         'DFF.N59K8N.DPV1LOG.D1212', 'DUC.N59R11.PLATIN.ANLIE', 'AAA.BBB.CCC.11']

    def test_compare_rvs_and_s3(self):
        # Test case 1: Both lists are identical
        expected_output = [{'in_rvs_web_newly_added_file': None},
                           {'from_s3_not_transfer_file': None},
                           {'s3_and_rvsweb_missmatched_files': None}]
        self.assertEqual(compare_rvs_and_s3(self.s3_bucket_filename_input, self.s3_bucket_filename_input), expected_output)
        
        # Test case 2: Lists are different
        expected_output = [{'in_rvs_web_newly_added_file': {'DUC.N59R11.PLATIN.ANLIE': 1}},
                           {'from_s3_not_transfer_file': {'DDD.N59R11.CCCVLIST.FFF12': 1}},
                           {'s3_and_rvsweb_missmatched_files': {'DDD.N59R11.CYCVDET.FFF12': {'new_value': 2, 'old_value': 1}}}]
        self.assertEqual(compare_rvs_and_s3(self.s3_bucket_filename_input, self.other_web_filename_input), expected_output)

if __name__ == '__main__':
    unittest.main()
