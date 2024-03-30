import time
import sys


def robot(start: int = 0):
    print(f'robot {start}')
    n = start
    while True:
        if n > start+10: return
        print(n)
        n += 1
        time.sleep(1)


if __name__ == "__main__":
    start_num = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    robot(start_num)