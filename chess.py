def check_move(colour, piece, start, end) -> bool:

    start = convert_coords(start)
    end = convert_coords(end)

    if start == end:
        return "No move made"

    if piece == "rook" or piece == "queen":
        if start[0] == end[0] or start[1] == end[1]:
            return True

    if piece == "bishop" or piece == "queen":
        if abs(start[0] - end[0]) == abs(start[1] - end[1]):
            return True

    if piece == "king":
        if abs(start[0] - end[0]) <= 1 and abs(start[1] - end[1]) <= 1:
            return True

    if piece == "knight":
        if sorted([abs(start[0] - end[0]), abs(start[1] - end[1])]) == [1, 2]:
            return True

    if piece == "pawn":
        if start[1] in [1, 6]:
            jump = 2
        else:
            jump = 1

        if (colour == "white" and (start[1] - end[1] > 0)) or (
            colour == "black" and (start[1] - end[1] < 0)
        ):
            if start[0] == end[0] and abs(start[1] - end[1]) <= jump:
                return True

    return False


def plot_board(colour=None, piece=None, start=None, end=None) -> tuple:

    board = []

    for i in range(8):
        board.append([(x + i + 1) % 2 for x in range(8)])

    if start and end:

        start = convert_coords(start)
        end = convert_coords(end)
        board[start[1]][start[0]] = 2
        board[end[1]][end[0]] = 3

    if colour and piece:
        image_url = f"./static/images/{colour.lower()}/{piece.lower()}.png"
    else:
        image_url = None

    return board, image_url


def convert_coords(coord) -> tuple:
    coord = coord.strip()

    letters = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}

    x = letters[coord[0].upper()]
    y = 8 - int(coord[1])

    return (x, y)
