# test_app.py
import unittest
from app import main  # assuming 'main' is a function in your app.py

class TestApp(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), "Hello, Docker!")

if __name__ == '__main__':
    unittest.main()
