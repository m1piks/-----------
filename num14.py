def powers_of_two(N):
    power = 0
    result = 1
    while result <= N:
        print(result)
        power += 1
        result = 2 ** power

# Вводим число N
N = int(input("Введите число N: "))

# Выводим все целые степени двойки, не превосходящие число N
powers_of_two(N)