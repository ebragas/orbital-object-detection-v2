"""Wrapper for Planet API"""

import os
import requests


class Client(object):
    def __init__(self):
        self._key = os.environ["PL_API_KEY"]
        self._base = "https://api.planet.com/"

    # TODO: Decorator to check/handle API response codes

    def list_item_types(self) -> dict:
        """API Reference: https://developers.planet.com/docs/api/reference/#operation/ListItemTypes
        """
        data = requests.get(self._base + "/data/v1/item-types").json()
        return {e["id"]: e["display_description"] for e in data["item_types"]}

    def list_asset_types(self) -> dict:
        """API Reference: https://developers.planet.com/docs/api/reference/#operation/ListAssetTypes
        """
        data = requests.get(self._base + "data/v1/asset-types").json()
        return {e["id"]: e["display_description"] for e in data["asset_types"]}


class Item(object):
    pass


if __name__ == "__main__":
    pass
