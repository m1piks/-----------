def find_numbers(S, P):
    for X in range(1, 1001):
        for Y in range(1, 1001):
            if X + Y == S and X * Y == P:
                return X, Y

# Вводим сумму и произведение чисел
S = int(input("Введите сумму чисел: "))
P = int(input("Введите произведение чисел: "))

# Находим числа X и Y
X, Y = find_numbers(S, P)

# Выводим результат
print("Задуманные числа: X =", X, "и Y =", Y)