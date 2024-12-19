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
    with open(path, "r") as file:
        line_list = file.readlines()

    report_list = []
    for i in range(len(line_list)):
        new_str_list = line_list[i].strip().split(" ")
        new_int_list = []
        for item in new_str_list:
            new_int_list.append(int(item))
        report_list.append(new_int_list)

    return report_list


def analyse_reports(report_list: list[list[int]]) -> int:
    safe_report_count = 0
    for report in report_list:
        difference_list = create_diff_list(report)
        bad_diff_index = evaluate_diff_list(difference_list, len(report))

        if bad_diff_index is not None:
            new_report_1 = report.copy()
            new_report_1.pop(bad_diff_index)
            diff_list_1 = create_diff_list(new_report_1)
            if evaluate_diff_list(diff_list_1, len(new_report_1)) is None:
                safe_report_count += 1
                print(
                    f"{new_report_1} - Safe ({report}) -  Diff_list: {diff_list_1} ({difference_list})"
                )

            else:
                new_report_2 = report.copy()
                new_report_2.pop(bad_diff_index + 1)
                diff_list_2 = create_diff_list(new_report_2)
                if evaluate_diff_list(diff_list_2, len(new_report_2)) is None:
                    safe_report_count += 1
                    print(
                        f"{new_report_2} - Safe ({report}) - Diff_list: {diff_list_2} ({difference_list})"
                    )
                # else:
                #     print(f"{report}, {new_report_1}, {new_report_2} - Unsafe")
        else:
            safe_report_count += 1

    return safe_report_count


def create_diff_list(report):
    difference_list = []
    for i in range(len(report) - 1):
        difference = report[i + 1] - report[i]
        difference_list.append(difference)
    return difference_list


def evaluate_diff_list(diff_list, report_length):
    positive_diff_count = 0
    negative_diff_count = 0
    bad_diff_index = None
    for i in range(len(diff_list)):
        if not (-3 <= diff_list[i] <= 3 and diff_list[i] != 0):
            bad_diff_index = i
            return bad_diff_index
        if diff_list[i] > 0:
            positive_diff_count += 1
        elif diff_list[i] < 0:
            negative_diff_count += 1
    if abs(positive_diff_count - negative_diff_count) >= report_length - 1:
        bad_diff_index = None
    elif negative_diff_count == 1:
        for i in range(len(diff_list)):
            if diff_list[i] < 0:
                bad_diff_index = i
    elif positive_diff_count == 1:
        for i in range(len(diff_list)):
            if diff_list[i] > 0:
                bad_diff_index = i
    else:
        bad_diff_index = 0  # Catch case where there are more than one incorrect diffs
    return bad_diff_index


report_list = get_file_data("Advent-of-Code-2024/Day 2/Day 2 Puzzle Input.txt")
print(analyse_reports(report_list))
