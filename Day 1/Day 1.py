import math


def get_file_data(path: str) -> tuple[list, list]:
    with open(path, "r") as file:
        line_list = file.readlines()
    list_1 = []
    list_2 = []
    for i in range(len(line_list)):
        new_line = line_list[i]
        new_line.strip()
        items_to_add = new_line.split("   ")
        list_1.append(int(items_to_add[0]))
        list_2.append(int(items_to_add[1]))
    return list_1, list_2


def find_difference(list_1: list[int], list_2: list[int]) -> int:
    list_1.sort()
    list_2.sort()
    total_difference = 0
    for i in range(len(list_1)):
        total_difference += math.fabs(list_1[i] - list_2[i])
    return int(total_difference)


def find_similarity_score(list_1: list, list_2: list) -> int:
    list_1.sort()
    list_2.sort()

    similarity_score = 0
    for i in range(len(list_1)):
        list_1_num = list_1[i]
        occurrences = 0

        try:
            list_2_index = list_2.index(list_1_num)
        except ValueError:
            occurrences += 0
        else:
            step = 0
            while list_2[list_2_index + step] == list_1_num:
                occurrences += 1
                step += 1
        finally:
            similarity_score += list_1_num * occurrences

    return similarity_score


list_1, list_2 = get_file_data("Day 1 Puzzle Input.txt")
difference = find_difference(list_1, list_2)
similarity_score = find_similarity_score(list_1, list_2)
print(difference)
print(similarity_score)
