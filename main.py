

"1st program"

print((9**0.5)*5)

"2nd program"
print(9.99 > 9.98,1000!=1000.1)

result = (9.99 > 9.98) and (1000 != 1000.1)
print(result)

"3rd program"

# Выражение без приоритета
result_without_priority = 2 * 2 + 2
print("Результат без приоритета:", result_without_priority)

# Выражение с приоритетом для сложения
result_with_priority = 2 * (2 + 2)
print("Результат с приоритетом:", result_with_priority)

# Сравнение результатов
comparison_result = result_without_priority == result_with_priority
print("Результат сравнения:", comparison_result)

"3rd program"

# Дана строка '123.456'
number_str = '123.456'

# Найти индекс точки
dot_index = number_str.index('.')

# Вывести первую цифру после запятой
first_digit_after_dot = number_str[dot_index + 1]
print(first_digit_after_dot)


# Другой вариант решения по теме модуля :

# Преобразуем строку в дробное число
number_str = '123.456'
number_float = float(number_str)

# Умножаем на 10, чтобы сместить 4 в целую часть
shifted_number = number_float * 10

# Преобразуем в целое число, чтобы отбросить дробную часть
shifted_int = int(shifted_number)

# Используем остаточное деление на 10, чтобы получить последнюю цифру (4)
first_digit_after_dot = shifted_int % 10

# Выводим результат
print(first_digit_after_dot)