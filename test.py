import os
import time
import requests

with open('test1.log', 'w') as f:
    f.write('')


def test_api():
    print("---- test started ----")
    url = "http://10.102.148.193:30505/api/recommend"
    print('url: ', url)

    payload = {
        'songs': [
            "1985",
            "All The Small Things"
        ]
    }

    for i in range(0, 200):
        try:
            response = requests.post(url, json=payload, timeout=1.5)
            # print(response)
            response_json = response.json()
        except:
            response_json = "SERVICE_OFFLINE"

        print("[", i+1, " / 200 ]",
              time.strftime("%Y-%m-%d %H:%M:%S"), response_json)

        with open('test1.log', 'a') as f:
            f.write("[" + str(i+1) + " / 200 ] " +
                    time.strftime("%Y-%m-%d %H:%M:%S") + " " + str(response_json) + '\n')
        time.sleep(0.1)


if __name__ == "__main__":
    test_api()