def get_sequence():
    n = int(input("Введите количество элементов: "))
    print(''.join(str(i) * i for i in range(1, n + 1))[:n])


if __name__ == "__main__":
    get_sequence()