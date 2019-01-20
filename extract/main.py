from planet.planet import Client


def run(c):
    print(c.hello_world("Eric"))
    print(c.list_asset_types())
    return


if __name__ == "__main__":
    client = Client()
    run(client)
