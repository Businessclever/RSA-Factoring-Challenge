#!/usr/bin/python3

import sys


def factorize(number):
    factors = []
    for i in range(2, int(number**0.5) + 1):
        while number % i == 0:
            factors.append(i)
            number //= i
    if number > 1:
        factors.append(number)
    return factors


def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        return

    input_file = sys.argv[1]

    try:
        with open(input_file, "r") as file:
            for line in file:
                number = int(line.strip())
                factors = factorize(number)
                factorization = "*".join(str(factor) for factor in factors)
                print(f"{number}={factorization}")

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")


if __name__ == "__main__":
    main()

