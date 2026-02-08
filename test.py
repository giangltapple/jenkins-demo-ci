import unittest

class TestApp(unittest.TestCase):
    def test_dummy(self):
        # Luôn luôn đúng để demo Pass
        self.assertTrue(True)
        print("TEST CASE: OK")

if __name__ == '__main__':
    unittest.main()
