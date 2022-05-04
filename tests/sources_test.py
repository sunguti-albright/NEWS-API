import unittest
from models import source
Source = source.Source


class SourceTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Movie Class
    """

    def setUp(self):
        """
        SetUp method that will run before every Test
        """
        self.new_source = Source(54321, "Steph Curry with the lead", "The NBA all star goes for the Gold again, this seems to be his new hobby since the last win", "https://web.whatsapp.com/" ,"sports")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

if __name__ == '__main__':
    unittest.main()