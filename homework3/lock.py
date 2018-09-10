from threading import Lock
from threading import Thread


def print_even(lock1, lock2):
    for x in range(0, 101, 2):
        lock2.acquire()
        print(x)
        lock1.release()


def print_odd(lock1, lock2):
    for x in range(1, 101, 2):
        lock1.acquire()
        print(x)
        lock2.release()


if __name__ == '__main__':
    lock1 = Lock()
    lock2 = Lock()
    lock1.acquire()
    t1 = Thread(target=print_even, args=(lock1, lock2))
    t2 = Thread(target=print_odd, args=(lock1, lock2))
    t1.start()
    t2.start()
