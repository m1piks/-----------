def find_max_sequence(numbers):
    max_sequence = []
    current_sequence = []
    
    for num in numbers:
        if not current_sequence or num > current_sequence[-1]:
            current_sequence.append(num)
        else:
            if len(current_sequence) > len(max_sequence):
                max_sequence = current_sequence
            current_sequence = [num]
    
    if len(current_sequence) > len(max_sequence):
        max_sequence = current_sequence
    
    return max_sequence

# Вводим список чисел
numbers = [1, 5, 2, 3, 4, 6, 1, 7]

# Находим максимальную сплошную возрастающую последовательность
max_sequence = find_max_sequence(numbers)

# Выводим результат
print(max_sequence)