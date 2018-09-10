from threading import Semaphore
from threading import Thread


def print_even(sem1, sem2):
    for x in range(0, 101, 2):
        sem2.acquire()
        print(x)
        sem1.release()


def print_odd(sem1, sem2):
    for x in range(1, 101, 2):
        sem1.acquire()
        print(x)
        sem2.release()


if __name__ == '__main__':
    sem1 = Semaphore()
    sem2 = Semaphore()
    sem1.acquire()
    t1 = Thread(target=print_even, args=(sem1, sem2))
    t2 = Thread(target=print_odd, args=(sem1, sem2))
    t1.start()
    t2.start()
