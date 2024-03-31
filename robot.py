import time
import sys
import requests
import asyncio

sFlag = 0


async def requester():
    global sFlag
    try:
        r = requests.get("http://localhost:8000/checkFlag", headers={'Accept': 'application/json'}).json()
        sFlag = r['Flag']
    except Exception as e:
        print(f"Unable to connect {e}")


async def robot(start: int = 0):
    global sFlag
    t = time.time()
    n = start
    while True:
        if time.time() - t >= 1.0:
            print(f"dTime {time.time() - t}")
            t = time.time()
            await requester()
            if sFlag:
                return 0
            print(n)
            n += 1


if __name__ == "__main__":
    start_num = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    asyncio.run(robot(start_num))

