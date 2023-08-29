def min_flips(n, coins):
    heads = coins.count('H')
    tails = coins.count('T')
    return min(heads, tails)

n = int(input("Введите количество монеток: "))
coins = input("Введите последовательность монеток (например, HHTTH): ")

min_flips_needed = min_flips(n, coins)
print("Минимальное количество монеток, которые нужно перевернуть:", min_flips_needed)