from threading import Condition
from threading import Thread


def print_even(cond1, cond2):
    for x in range(0, 101, 2):
        with cond2:
            cond2.wait()
            print(x)
        with cond1:
            cond1.notify_all()


def print_odd(cond1, cond2):
    for x in range(1, 101, 2):
        with cond1:
            cond1.wait()
            print(x)
        with cond2:
            cond2.notify_all()


if __name__ == '__main__':
    cond1 = Condition()
    cond2 = Condition()
    t1 = Thread(target=print_even, args=(cond1, cond2))
    t2 = Thread(target=print_odd, args=(cond1, cond2))
    t1.start()
    t2.start()
    with cond2:
        cond2.notify_all()
