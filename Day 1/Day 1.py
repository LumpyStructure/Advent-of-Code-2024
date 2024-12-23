def get_file_data(path: str) -> tuple[list, list]:
    """Reads the file at the given path and returns two lists"""
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


# For part 1
def find_difference(list_1: list[int], list_2: list[int]) -> int:
    """Takes two lists and finds the total difference between corresponding elements in each list when sorted by size"""
    list_1.sort()
    list_2.sort()

    # Calculate the absolute difference between corresponding elements in each list and sum the results
    total_difference = 0
    for i in range(len(list_1)):
        total_difference += abs(list_1[i] - list_2[i])
    return int(total_difference)


# For part 2
def find_similarity_score(list_1: list, list_2: list) -> int:
    """Gives the similarity score of a list, defined as the number of occurences of a number in one list in the other list multiplied by the value of that number.
    This is repeated for all numbers in the list and the sum is calculated."""
    list_1.sort()
    list_2.sort()

    similarity_score = 0
    for i in range(len(list_1)):
        list_1_num = list_1[i]
        occurrences = 0  # Counts number of occurences of list_1_num in list_2

        try:
            list_2_index = list_2.index(list_1_num)
        except ValueError:
            pass  # No occurences of list_1_num, so nothing needs to be done
        else:
            step = 0
            # Iterate through list_2 until the current number is not equal to list_1_num
            while list_2[list_2_index + step] == list_1_num:
                occurrences += 1
                step += 1
        finally:
            similarity_score += list_1_num * occurrences

    return similarity_score


list_1, list_2 = get_file_data("Advent-of-Code-2024\Day 1\Day 1 Puzzle Input.txt")
difference = find_difference(list_1, list_2)
similarity_score = find_similarity_score(list_1, list_2)
print(difference)
print(similarity_score)
