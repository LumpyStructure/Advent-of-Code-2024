# Ideas
#   Rather than trying to reverse strings, maybe check for both 'XMAS' and 'SAMX'
#   Do checking all by iterating, just pass in pre-processed strings for horizontal, verticals & diagonals
#       If using this method, might be easier to just reverse string (or iterate in reverse order)


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

    return verticals


def get_diagonals(path: str) -> list[str]:
    """Returns a list of the diagonals"""


def check_string(string: list[str]) -> int:
    """Returns the number of occurences of 'XMAS', both forwards & backwards"""
