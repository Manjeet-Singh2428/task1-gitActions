import unittest
from hello import hello

class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello, World in task 1!")

if __name__ == "__main__":
    unittest.main()
