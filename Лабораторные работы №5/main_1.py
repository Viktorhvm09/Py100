# TODO решите задачу
import json

FILENAME = "input.json"

def task() -> float:
    with open(FILENAME, encoding="utf-8") as file:
        json_data = json.load(file)
    product = []
    for item in json_data:
        product.append([item["score"] * item["weight"]])
    sum_product = sum(sum(product, []))
    return round(sum_product, 3)


print(task())
