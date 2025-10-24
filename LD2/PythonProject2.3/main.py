
#lab 2.3

import random

def generate_profits(rows, cols, low, high):
    return [[random.randint(low, high) for _ in range(cols)] for _ in range(rows)]


def average_profits(profits):
    return [sum(shop) / len(shop) for shop in profits]


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{val:5}" for val in row))


def main():
    shops = 10
    months = 12


    profits = generate_profits(shops, months, -1000, 10000)

    print("Прибутки магазинів за рік (рядки - магазини, стовпці - місяці):")
    print_matrix(profits)

    averages = average_profits(profits)

    print("\nСередній прибуток за рік для кожного магазину:")
    for i, avg in enumerate(averages, start=1):
        print(f"Магазин {i}: {avg:.2f}")


if __name__ == "__main__":
    main()
