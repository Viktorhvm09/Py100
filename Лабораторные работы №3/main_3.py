from gc import set_debug
from itertools import product


def count_letters(text: str) -> dict:
    """
    Функция возвращает словарь котором ключи это буквы нижнего регистра полученные из text,
    а значение это сколько раз эта буква встретилась в text.

    пример:
        text = 'У лукоморья дуб зелёный;'
        result = count_letters(text)
        print(result)  # {'у': 3, 'л': 2, 'к': 1, 'о': 2, 'м': 1, 'р': 1, 'ь': 1, 'я': 1, 'д': 1, 'б': 1, 'з': 1,
        'е': 1, 'ё': 1, 'н': 1, 'ы': 1, 'й': 1}
    """
    ...  # TODO Реализуйте функцию
    text = text.lower()
    letter_count = dict()
    for symbol in text:
        if symbol.isalpha():
            if letter_count.get(symbol) is None:
                letter_count[symbol] = 1
            else:
                count = letter_count.get(symbol)
                count += 1
                letter_count[symbol] = count
    # print(letter_count)
    return letter_count

def calculate_frequency(letter_count: dict) -> dict:
    """
    Функция возвращает словарь, где буква используется как ключ, а ее частота как значение.

    пример:
        letter_count = {'у': 3, 'л': 2, 'к': 1, 'о': 2, 'м': 1, 'р': 1, 'ь': 1, 'я': 1, 'д': 1, 'б': 1, 'з': 1,
        'е': 1, 'ё': 1, 'н': 1, 'ы': 1, 'й': 1}
        result = calculate_frequency(letter_count)
        print(result)  # {'у': 0.15, 'л': 0.1, 'к': 0.05, 'о': 0.1, 'м': 0.05, 'р': 0.05, 'ь': 0.05, 'я': 0.05,
        'д': 0.05, 'б': 0.05, 'з': 0.05, 'е': 0.05, 'ё': 0.05, 'н': 0.05, 'ы': 0.05, 'й': 0.05}
    """
    ...  # TODO Реализуйте функцию
    calculate_frequency = dict()
    set_symbol = list(letter_count.keys())
    set_values = list(letter_count.values())
    product_frequency = []
    for values in set_values:
        frequency_letter = values / sum(set_values)
        product_frequency.append(frequency_letter)

    for index, value in enumerate(set_symbol):
        calculate_frequency[value] = product_frequency[index]
    # print(calculate_frequency)
    return calculate_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

count_dict = count_letters(main_str)
frequency_dict = calculate_frequency(count_dict)

# TODO Распечатайте в столбик букву и её частоту в тексте


# print(count_dict.keys())
# print(frequency_dict)

for _ in frequency_dict:
    print(f"{_}: {frequency_dict[_]:.2f}")