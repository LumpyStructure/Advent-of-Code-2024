# Program spec
#   Process text file
#   Reports must be:
#       All increasing or all decreasing
#       Difference of at least 1 and at most 3
#   Test program output:
#       Safe
#       Unsafe
#       Unsafe
#       Unsafe
#       Unsafe
#       Safe
#
#       2 reports safe


def get_file_data(path: str) -> list[list[int]]:
    """Read the file at the given path and return a 2D list with each report as a sublist"""
    with open(path, "r") as file:
        line_list = file.readlines()

    report_list = []
    for i in range(len(line_list)):
        new_str_list = line_list[i].strip().split(" ")

        # Convert each item in new_str_list to ints and append it to report_list
        new_int_list = []
        for item in new_str_list:
            new_int_list.append(int(item))
        report_list.append(new_int_list)

    return report_list


def analyse_reports(report_list: list[list[int]]) -> int:
    """Analyse a 2D list of reports and return the number of safe reports"""
    safe_report_count = 0
    for report in report_list:
        difference_list = create_diff_list(report)
        bad_diff_index = evaluate_diff_list(difference_list)

        if bad_diff_index is not None:
            new_report_1 = report.copy()
            new_report_1.pop(bad_diff_index)
            diff_list_1 = create_diff_list(new_report_1)
            if evaluate_diff_list(diff_list_1) is None:
                safe_report_count += 1
            else:
                new_report_2 = report.copy()
                new_report_2.pop(bad_diff_index + 1)
                diff_list_2 = create_diff_list(new_report_2)
                if evaluate_diff_list(diff_list_2) is None:
                    safe_report_count += 1
        else:
            safe_report_count += 1

    return safe_report_count


def create_diff_list(report: list[int]) -> list[int]:
    """Create a list of the signed differences / 'vectors' betweeen each element"""
    difference_list = []
    for i in range(len(report) - 1):
        difference = report[i + 1] - report[i]
        difference_list.append(difference)
    return difference_list


def evaluate_diff_list(diff_list: list[int]) -> int | None:
    """Returns the index of the bad difference value (does not meet constraints) if there is only one.\n
    If there are multiple bad differences, 0 is returned\n
    If there is no bad difference, None is returned"""

    positive_diff_count = 0
    negative_diff_count = 0
    bad_diff_index = None

    for i in range(len(diff_list)):
        if abs(diff_list[i]) > 3 or diff_list[i] == 0:
            bad_diff_index = i
            return bad_diff_index

        # Increment one of the two counters depending on the sign of the difference
        if diff_list[i] > 0:
            positive_diff_count += 1
        elif diff_list[i] < 0:
            negative_diff_count += 1

    # If there is none or only one 'odd difference out', then there is no bad difference
    if abs(positive_diff_count - negative_diff_count) >= len(diff_list):
        return bad_diff_index
    elif negative_diff_count == 1:
        # Find the singluar negative difference
        for i in range(len(diff_list)):
            if diff_list[i] < 0:
                bad_diff_index = i
    elif positive_diff_count == 1:
        # Find the singular positive difference
        for i in range(len(diff_list)):
            if diff_list[i] > 0:
                bad_diff_index = i
    else:
        # Catch case where there is more than one incorrect difference & return 0
        bad_diff_index = 0
    return bad_diff_index


report_list = get_file_data("Advent-of-Code-2024/Day 2/Day 2 Puzzle Input.txt")
print(analyse_reports(report_list))
