from planet.planet import Client, Filter, Item


def run(c):

    # Quick Search
    filter_def = Filter(
        "/Users/ericbragas/dev/orbital-object-detection-v2/extract/planet/sample-geojson/sf_bay.json",
        0.5,
    )
    results = c.quick_search(filter_def, ["REOrthoTile"])
    return


if __name__ == "__main__":
    client = Client()
    run(client)
