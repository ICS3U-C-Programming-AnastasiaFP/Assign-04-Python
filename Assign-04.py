#!/usr/bin/env python3
# Created by: Anastasia Friedenstein Patino
# Created on: December. 08, 2023
# Program calculates the sum of all the multiples of 3 or 5 below 1000


def main():
    print(
        "Hello, today this program shall calculate/find the sum of all the multiples of 3 or 5 below 1000"
    )

    sum = 0
    sum2 = 0

    for counter in range(1000):
        if counter % 3 == 0:
            sum = sum + counter
            print(counter)
        if counter % 5 == 0:
            sum2 = sum2 + counter
            print(counter)
    print(f" sum of multiples of 3: {sum}")
    print(f" sum of multiples of 5: {sum2}")


if __name__ == "__main__":
    main()
