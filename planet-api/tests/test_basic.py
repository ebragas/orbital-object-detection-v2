import unittest
from planet.planet import Client

class TestPlanetClientMethods(unittest.TestCase):

    def setUp(self):
        self.client = Client()

    def test_hello_world(self):
        self.assertEqual(self.client.hello_world(), "Hello, World!")

    def test_hello_world2(self):
        self.assertEqual(self.client.hello_world("Eric"), "Hello, Eric!")


if __name__ == "__main__":
    unittest.main()
