def count_digits(number):
    number_str = str(number).replace(',', '.')  # Заменяем запятую на точку (если есть)
    if '.' in number_str:
        integer_part, decimal_part = number_str.split('.')
        return len(integer_part) + len(decimal_part)
    else:
        return len(number_str)

# Вводим число
number = input("Введите число: ")

# Вычисляем количество цифр в числе
digits_count = count_digits(number)

# Выводим результат
print("Количество цифр в числе:", digits_count)