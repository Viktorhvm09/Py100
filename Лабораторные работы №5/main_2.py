# TODO импортировать необходимые модули
import csv
import json
import collections


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, "r", encoding="utf-8") as f:
        lines = [line for line in csv.DictReader(f)]
        # for line in lines:
            # print(line)


    ...  # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w', encoding="utf-8") as file:
        json.dump(lines, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")
