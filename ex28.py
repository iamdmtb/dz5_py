def sum(num_1, num_2):
    if num_1 == 0:
        return num_2
    else:
        return 1 + sum(num_1 - 1, num_2)
print(sum(int(input("Введите первое слагаемое: ")), int(input("Введите второе слагаемое: "))))