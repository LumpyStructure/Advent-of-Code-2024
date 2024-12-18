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
        direction = -2  # Placeholder value to detect first iteration
        unsafe_report = False
        for i in range(len(report) - 1):
            prev_direction = direction
            difference = report[i + 1] - report[i]
            if -3 <= difference < 0:
                direction = -1
            elif 0 < difference <= 3:
                direction = 1
            else:
                direction = 0

            if direction != prev_direction and prev_direction != -2:
                unsafe_report = True
                break

        if not unsafe_report:
            safe_report_count += 1
    return safe_report_count


report_list = get_file_data("Day 2 Puzzle Input.txt")
print(analyse_reports(report_list))
