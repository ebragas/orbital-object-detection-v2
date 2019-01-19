from planet import Client


def run(c):
    print c.hello_world('Eric')

if __name__ == "__main__":
    client = Client()
    run(client)
