# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, separator=","):
    first_group = first_group.split(separator)
    second_group = second_group.split(separator)
    common_participants = list(set(first_group).intersection(second_group))
    common_participants.sort()

    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Проверьте работу функции с разделителем отличным от запятой
find_common_participants(participants_first_group, participants_second_group, "|")
