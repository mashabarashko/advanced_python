from threading import Timer

import time


def print_even():
    for x in range(0, 101, 2):
        print(x)
        time.sleep(0.02)


def print_odd():
    for x in range(1, 101, 2):
        print(x)
        time.sleep(0.02)


if __name__ == '__main__':
    t1 = Timer(0, print_even)
    t2 = Timer(0.01, print_odd)
    t1.start()
    t2.start()
