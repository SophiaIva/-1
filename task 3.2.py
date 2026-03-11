# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, separator=','):
    first_set = set(first_group.split(separator))
    second_set = set(second_group.split(separator))
    return list(first_set.intersection(second_set))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group, participants_second_group, '|')
print(common_participants)
