import time
import sys
import requests
import asyncio

stopFlag = 0


async def requester():
    global stopFlag
    try:
        r = requests.get("http://localhost:8000/checkFlag", headers={'Accept': 'application/json'}).json()
        stopFlag = r['Flag']
    except Exception as e:
        print(e)


async def robot(start: int = 0):
    global stopFlag
    t = time.time()
    n = start
    while True:
        if time.time() - t >= 1.0:
            t = time.time()
            await requester()
            if stopFlag:
                return 0
            print(n)
            n += 1


if __name__ == "__main__":
    start_num = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    asyncio.run(robot(start_num))