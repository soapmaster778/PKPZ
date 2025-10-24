def input_array():
    n = int(input("Введіть кількість елементів масиву: "))
    arr = []
    for i in range(n):
        arr.append(int(input(f"Введіть елемент {i}: ")))
    return arr


def process_array(arr):
    # 1. Знаходимо суму непарних негативних елементів
    negative_odd_sum = sum(x for x in arr if x < 0 and x % 2 != 0)

    # 2. Замінюємо кратні 3 елементи на цю суму
    result = [negative_odd_sum if x % 3 == 0 else x for x in arr]

    return result, negative_odd_sum


def output_array(arr, negative_odd_sum):
    print("\nСума непарних негативних елементів:", negative_odd_sum)
    print("Масив після обробки:", arr)


def main():
    arr = input_array()
    result, neg_sum = process_array(arr)
    output_array(result, neg_sum)


if __name__ == "__main__":
    main()
