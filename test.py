import time
import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

with open('test1.log', 'w') as f:
    f.write('')

def test_api():
    logging.info("---- test started ----")
    url = "http://10.102.148.193:30505/api/recommend"
    logging.info(f'url: {url}')

    payload = {
        'songs': [
            "1985",
            "Starboy"
        ]
    }

    for i in range(0, 2000):
        try:
            response = requests.post(url, json=payload, timeout=0.2)
            response_json = response.json()
            logging.info(f"[{i+1}/200] {response_json}")
        except Exception as e:
            logging.error(f"[{i+1}/200] Failed to send request: {e}")
            response_json = "SERVICE_OFFLINE"

        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        with open('test1.log', 'a') as f:
            f.write(f"[{i+1}/2000] {timestamp} {response_json}\n")

        time.sleep(0.1)

if __name__ == "__main__":
    test_api()

