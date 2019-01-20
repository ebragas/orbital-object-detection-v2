"""Wrapper for Planet API"""

import os
import json
import requests
from requests.auth import HTTPBasicAuth


class Client(object):
    """Wrapper class for the Planet API.
    """

    def __init__(self):
        self._key = os.environ["PL_API_KEY"]
        self._base_url = "https://api.planet.com/"

    # TODO: Decorator to check/handle API response codes

    def list_item_types(self) -> dict:
        """API Reference: https://developers.planet.com/docs/api/reference/#operation/ListItemTypes
        """

        data = requests.get(self._base_url + "/data/v1/item-types").json()
        return {e["id"]: e["display_description"] for e in data["item_types"]}

    def list_asset_types(self) -> dict:
        """API Reference: https://developers.planet.com/docs/api/reference/#operation/ListAssetTypes
        """

        data = requests.get(self._base_url + "data/v1/asset-types").json()
        return {e["id"]: e["display_description"] for e in data["asset_types"]}

    def quick_search(self, filter_definition, item_types):

        body = {"item_types": item_types, "filter": filter_definition._filter}

        data = requests.post(
            self._base_url + "data/v1/quick-search",
            auth=HTTPBasicAuth(self._key, ""),
            json=body,
        ).json()

        # TODO: Return Item(s)
        item_list = [Item(e) for e in data["features"]]
        return item_list


class Item(object):
    """Items are entries in the Planet catalog and generally represent a single local observation (or scene)
    captured by a satellite.

    Item objects are similar to Google Cloud Storage blobs in that you must execute the `get_item()` method in
    order to load the actual item data.
    """

    def __init__(self, data):
        self.data = data

    def get_item(self):
        """Reload an Item's data using its self reference link
        """
        raise NotImplementedError


class Filter(object):
    """Create filter from geojson file
    See Planet documentation on generating GeoJson file for search area
    """

    def __init__(self, geojson_path, max_cloud_cover_pct):

        # Read from file
        with open(geojson_path) as f:
            geojson = json.load(f)

        self._geometry = geojson["features"][0]["geometry"]

        self._geometry_filter = {
            "type": "GeometryFilter",
            "field_name": "geometry",
            "config": self._geometry,
        }

        # TODO: Allow parameterization of dates
        self._date_range_filter = {
            "type": "DateRangeFilter",
            "field_name": "acquired",
            "config": {
                "gte": "2018-01-01T00:00:00.000Z",
                "lte": "2018-12-31T00:00:00.000Z",
            },
        }

        self._cloud_cover_filter = {
            "type": "RangeFilter",
            "field_name": "cloud_cover",
            "config": {"lte": max_cloud_cover_pct},
        }

        self._filter = {
            "type": "AndFilter",
            "config": [
                self._geometry_filter,
                self._date_range_filter,
                self._cloud_cover_filter,
            ],
        }


if __name__ == "__main__":
    pass
