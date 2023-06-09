def pow_recursive(a, b):
    if b == 1:
        return a
    elif b == 0:
        return 1
    else:
        return(a * pow_recursive(a, b - 1))
a = int(input("Введите число: "))
b = int(input("В какую степень возвести заданное число? "))
print(f"Результат равен: {pow_recursive(a, b)}")