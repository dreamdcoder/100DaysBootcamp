import math


def prime_checker(num):
        i = 2
        while i < num:
            if num % i == 0:
                return "not a prime number."
            i += 1
        return "a prime number."


if __name__ == "__main__":
    n = int(input("Enter number:\n"))
    s = prime_checker(num=n)
    print(f"The given number {n} is {s}")
