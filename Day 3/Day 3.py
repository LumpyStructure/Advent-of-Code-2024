def get_memory_file(path) -> str:
    """Gets & returns the memory text from a given path"""
    with open(path, "r") as file:
        memory = file.read()
    return memory


def get_do_sequences(memory: str) -> str:
    """Returns a string of the do() sections of memory"""
    do_split_mem = memory.split("do()")  # Split on each do() command

    # Split on each dont() command in each do() section
    dont_split_mem = []
    for mem_seq in do_split_mem:
        dont_split_mem.append(mem_seq.split("don't"))

    # Take the do() section of each do()dont() slice
    final_split_mem = []
    for mem_seq in dont_split_mem:
        final_split_mem.append(mem_seq[0])

    # Return as one string
    return "".join(final_split_mem)


def get_mul_cmds(memory: str) -> list[str]:
    """Splits out the contents of valid mult commands into a list"""
    split_mem = memory.split("mul(")  # Split on the valid first half of the command

    # Splits out the contents of the mul() if there is a closing bracket
    for i in range(len(split_mem)):
        if ")" in split_mem[i]:
            split_mem[i] = split_mem[i].split(")", 1)[0]
        else:
            split_mem[i] = ""

    # Return list of mul() contents
    return split_mem


def calc_total(split_mem):
    """Multiplies the contents of the mul() commands and add them to total if valid"""
    total = 0

    for command in split_mem:
        try:
            # Split into two nums
            mult_nums = command.split(",")

            # Reject if nums are not actually numbers
            if mult_nums[0].isdigit() and mult_nums[1].isdigit():
                # If there aren't two digits in mul() command, program will throw IndexError here
                mult_nums[0] = int(mult_nums[0])
                mult_nums[1] = int(mult_nums[1])
            else:
                raise ValueError

            # Reject if nums are more than three digits
            if mult_nums[0] > 999 or mult_nums[1] > 999:
                raise ValueError

            mult_result = mult_nums[0] * mult_nums[1]
            total += mult_result
        except:
            continue

    return total


memory = get_memory_file("Advent-of-Code-2024/Day 3/Day 3 Puzzle Input.txt")
do_mem = get_do_sequences(memory)
split_mem = get_mul_cmds(do_mem)

print(calc_total(split_mem))
