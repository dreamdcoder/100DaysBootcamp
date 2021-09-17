import math


def paint_calculator(height, width, coverage):
    tins = math.ceil(height * width / coverage)
    return tins


if __name__ == "__main__":
    h = float(input("Enter height of your wall:\n"))
    w = float(input("Enter width of your wall:\n"))
    c = 5
    t = paint_calculator(height=h, width=w, coverage=c)
    print(f"Total tins of paint required are {t}.")
