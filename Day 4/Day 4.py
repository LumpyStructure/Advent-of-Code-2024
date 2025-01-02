def get_horizontals(path: str) -> list[str]:
    """Returns a list of the horizontals"""
    with open(path, "r") as file:
        horizontals = file.readlines()

    # Remove the newline characters
    for i in range(len(horizontals)):
        horizontals[i] = horizontals[i].strip()
    return horizontals


def get_verticals(path: str) -> list[str]:
    """Returns a list of the verticals"""
    horizontals = get_horizontals(path)

    # Create a sublist for each vertical line (determined by the length of one of the horizontals)
    verticals = [[] for _ in range(len(horizontals[0]))]

    for horizontal in horizontals:
        # Append each character in the horizontal to the next sublist in verticals
        for i in range(len(horizontal)):
            verticals[i].append(horizontal[i])

    # Reform the lists into strings
    for i in range(len(verticals)):
        verticals[i] = "".join(verticals[i])

    return verticals


def get_diagonals(path: str) -> list[str]:
    """Returns a list of the diagonals"""
    horizontals = get_horizontals(path)
    diagonals = []

    # Create left to right diagonals

    # Iterate through the top row of the word search from left to right
    for x_start in range(len(horizontals[0])):
        y = 0
        new_diagonal = []
        # Iterate diagonally downward through the word search
        for x, y in zip(
            range(x_start, len(horizontals[0])), range(0, len(horizontals))
        ):
            new_diagonal.append(horizontals[y][x])

        # Reform the list into a string
        diagonals.append("".join(new_diagonal))

    # Iterate through the leftmost column of the word search,
    # excluding the first element (diagonal created in first loop)
    for y_start in range(1, len(horizontals)):
        x = 0
        new_diagonal = []
        # Iterate diagonally downward through the word search
        for x, y in zip(
            range(0, len(horizontals[0])), range(y_start, len(horizontals))
        ):
            new_diagonal.append(horizontals[y][x])

        # Reform the list into a string
        diagonals.append("".join(new_diagonal))

    # Create right to left diagonals

    # Iterate through the top row of the word search from right to left
    for x_start in range(len(horizontals[0]) - 1, -1, -1):
        y = 0  # Is this needed?
        new_diagonal = []
        # Iterate diagonally downward to the right through the word search
        for x, y in zip(range(x_start, -1, -1), range(len(horizontals))):
            new_diagonal.append(horizontals[y][x])

        # Reform the list into a string
        diagonals.append("".join(new_diagonal))

    # Iterate through the rightmost column of the word search,
    # excluding the first element (diagonal created in previous loop)
    for y_start in range(1, len(horizontals)):
        x = 0
        new_diagonal = []
        # Iterate diagonally downward through the word search
        for x, y in zip(
            range(len(horizontals[0]) - 1, -1, -1),
            range(y_start, len(horizontals)),
        ):
            new_diagonal.append(horizontals[y][x])

        # Reform the list into a string
        diagonals.append("".join(new_diagonal))
    return diagonals


def check_string(lines: list[str], search_word: str) -> int:
    """Returns the number of occurences of search_word, both forwards & backwards"""
    occurrences = 0
    # Check for search_word forwards
    for line in lines:
        occurrences += check_line(line, search_word)

    # Reverse search_word
    search_word = list(search_word)
    search_word.reverse()
    search_word = "".join(search_word)

    # Check for search_word backwards
    for line in lines:
        occurrences += check_line(line, search_word)

    return occurrences


def check_line(line: str, search_word: str) -> int:
    """Checks a line for a given search_word"""
    occurrences = 0
    for line_index in range(len(line) - len(search_word) + 1):
        # Check if letter matches first letter of search_word
        if line[line_index] == search_word[0]:
            word_matches = True
            # Check each subsequent letter
            for checking_index in range(1, len(search_word)):
                if line[checking_index + line_index] != search_word[checking_index]:
                    word_matches = False
                    break
            if word_matches:
                occurrences += 1
    return occurrences


path = "Day 4/Day 4 Puzzle Input.txt"
horizontals = get_horizontals(path)
verticals = get_verticals(path)
diagonals = get_diagonals(path)

print(
    check_string(horizontals, "XMAS")
    + check_string(verticals, "XMAS")
    + check_string(diagonals, "XMAS")
)
