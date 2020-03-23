import unittest
import geddata
from sprint2.dcai_sprint2 import birth_before_death
from sprint2.dcai_sprint2 import marriage_before_divorce


class TestSprint2(unittest.TestCase):
    def test_US03(self):
        inds, fams = geddata.get_inds_fams('res/US03.ged')
        self.assertEqual(birth_before_death(fams), 'ERROR: birthday should occur before the death of a person!')

    def test_US04(self):
        inds, fams = geddata.get_inds_fams('res/US04.ged')
        self.assertEqual(marriage_before_divorce(fams), 'ERROR: FAMILY: US04: 133: @F1@: Marriage should occur before divorce of spouses')


if __name__ == '__main__':
    unittest.main()