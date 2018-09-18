import concurrent.futures
import math


M = 1
N = 15


def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    sum = 0
    numbers = range(M, N)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, _is_prime in zip(numbers, executor.map(is_prime, numbers)):
            sum += number * _is_prime
    print("Sum:", sum)

if __name__ == '__main__':
    main()
