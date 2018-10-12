import unittest
from ex2 import reconstruct_trip

class Test(unittest.TestCase):
  def test_short_case(self):
    short_set = [
      (None, 'PDX'),
      ('PDX', 'DCA'),
      ('DCA', None)
    ]
    self.assertEqual(reconstruct_trip(short_set), ['PDX', 'DCA'])

  def test_long_case(self):
    long_set = [
      ('PIT', 'ORD'), #8
      ('XNA', 'CID'), #5
      ('SFO', 'BHM'), #2
      ('FLG', 'XNA'), #4
      (None, 'LAX'),  #0
      ('LAX', 'SFO'), #1
      ('CID', 'SLC'), #6
      ('ORD', None),
      ('SLC', 'PIT'), #7
      ('BHM', 'FLG'), #3
    ]
    self.assertEqual(reconstruct_trip(long_set), ['LAX', 'SFO', 'BHM', 'FLG', 'XNA', 'CID', 'SLC', 'PIT', 'ORD'])

  def test_incorrect_case(self):
    incorrect_set = [
      ('LHD', 'DAB'),
      (None, 'HVN'),
      ('MSO', 'SFO'),
      ('RDU', 'ABQ'),
      ('ACY', None),
    ]
    self.assertEqual(reconstruct_trip(incorrect_set), [])

if __name__ == '__main__':
  unittest.main()