import unittest
from extract.planet.planet import Client


class TestPlanetClient(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_api_key(self):
        self.assertIsNotNone(self.client._key)

    def test_list_item_types(self):
        self.assertEqual(len(self.client.list_item_types()), 14)

    def test_list_asset_types(self):
        self.assertEqual(len(self.client.list_asset_types()), 90)



if __name__ == "__main__":
    unittest.main()
