import unittest
from planet.planet import Client


class TestPlanetClient(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_api_key(self):
        self.assertIsNotNone(self.client._key)

    def test_hello_world(self):
        self.assertEqual(self.client.hello_world(), "Hello, World!")
        self.assertEqual(self.client.hello_world("Eric"), "Hello, Eric!")


if __name__ == "__main__":
    unittest.main()
