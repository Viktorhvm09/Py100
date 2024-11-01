from sys import api_version

numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
list_to_unknown = numbers[0:4]
list_after_unknown = numbers[5:]
# Не заметил что в количестве надо учитывать None
# average_of_numbers = sum(list_to_unknown + list_after_unknown) / len(list_to_unknown + list_after_unknown)
average_of_numbers = sum(list_to_unknown + list_after_unknown) / len(numbers)
# В задании нет требований к округлению. По начальному списку предположил что нужно получить целое число
# numbers[4] = int(average_of_numbers)
numbers[4] = round(average_of_numbers, 2)
print("Измененный список:", numbers)
