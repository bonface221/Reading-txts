import unittest
import readfiles 

class TestReadFiles(unittest.TestCase):
    def test_get_data(self):
        with open('text.txt','r') as handle:
            data = handle.read()
            self.assertEqual(data,readfiles.read_file('text.txt'))

    def test_nonfile(self):
        self.assertEqual(None, readfiles.read_file('tests.txt'))


if __name__== '__main__':
    unittest.main()
















