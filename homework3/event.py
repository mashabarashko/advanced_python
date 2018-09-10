from threading import Event
from threading import Thread


def print_even(event1, event2):
    for x in range(0, 101, 2):
        event2.wait()
        event2.clear()
        print(x)
        event1.set()


def print_odd(event1, event2):
    for x in range(1, 101, 2):
        event1.wait()
        event1.clear()
        print(x)
        event2.set()


if __name__ == '__main__':
    event1 = Event()
    event2 = Event()
    event2.set()
    t1 = Thread(target=print_even, args=(event1, event2))
    t2 = Thread(target=print_odd, args=(event1, event2))
    t1.start()
    t2.start()
