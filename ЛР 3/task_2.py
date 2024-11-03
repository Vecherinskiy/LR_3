def find_common_participants(srt_1, str_2, separator=','):
    set_1 = set(srt_1.split(separator))
    set_2 = set(str_2.split(separator))
    common_set = set_1.intersection(set_2)
    return sorted(list(common_set))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

list_common = find_common_participants(participants_first_group, participants_second_group, separator='|')
print(list_common)