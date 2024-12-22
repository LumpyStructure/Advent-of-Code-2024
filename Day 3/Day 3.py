def get_memory_file(path) -> str:
    with open(path, "r") as file:
        memory = file.read()
    return memory


memory = get_memory_file("Advent-of-Code-2024/Day 3/Day 3 Puzzle Input.txt")


split_mem = memory.split("mul(")
for i in range(len(split_mem)):
    if ")" in split_mem[i]:
        split_mem[i] = split_mem[i].split(")", 1)[0]
    else:
        split_mem[i] = ""
# print(split_mem)

total = 0

for command in split_mem:
    try:
        mult_nums = command.split(",")
        if mult_nums[0].isdigit() and mult_nums[1].isdigit():
            mult_nums[0] = int(mult_nums[0])
            mult_nums[1] = int(mult_nums[1])
        else:
            raise KeyError
        if mult_nums[0] > 999 or mult_nums[1] > 999:
            raise ValueError
        print(mult_nums[0], mult_nums[1])
        mult_result = mult_nums[0] * mult_nums[1]
        total += mult_result
    except ValueError:
        continue
    except IndexError:
        continue
    except KeyError:
        continue

print(total)
