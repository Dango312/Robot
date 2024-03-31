import time
import sys
import requests


def robot(start: int = 0):
    t = time.time()
    n = start
    while True:
        if time.time() - t >= 1.0:
            t = time.time()
            r = requests.get("http://localhost:8000/checkFlag", headers={'Accept': 'application/json'}).json()
            if r['Flag'] == 1:
                return 0
            print(n)
            n += 1


if __name__ == "__main__":
    start_num = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    robot(start_num)