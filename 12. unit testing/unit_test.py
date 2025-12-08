import unittest

class TestStringMethod(unittest.TestCase):
    #testcase pertama
    def test_strip(self):
        self.assertEqual('www.dicoding.com'.strip('c.mow'), 'dicoding')

    #testcase 2
    def test_isalnum(self):
        self.assertTrue('c0d1ng'.isalnum())
        self.assertFalse('c0d!ng'.isalnum())

    #testcase 3
    def test_index(self):
        s = 'dicoding'
        self.assertEqual(s.index('coding'), 2)
        #cek s.index gagal ketika tidak ditemukan

        with self.assertRaises(ValueError):
            s.index('decode')

if __name__ == '__main__':
    #testrunner
    unittest.main