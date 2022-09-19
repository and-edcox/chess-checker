def can_move(colour, piece, start, end) -> bool:
    """
    Function to check if a move on a chessboard is valid
    """

    start = convert_coords(start)
    end = convert_coords(end)

    if start == end:
        return "No move made"

    # Check orthogonal movement
    if piece == "rook" or piece == "queen":
        if start[0] == end[0] or start[1] == end[1]:
            return True

    # Check diagonal movement
    if piece == "bishop" or piece == "queen":
        if abs(start[0] - end[0]) == abs(start[1] - end[1]):
            return True

    # Check movement of max 1 space
    if piece == "king":
        if abs(start[0] - end[0]) <= 1 and abs(start[1] - end[1]) <= 1:
            return True

    # Check L shaped movement
    if piece == "knight":
        if sorted([abs(start[0] - end[0]), abs(start[1] - end[1])]) == [1, 2]:
            return True

    if piece == "pawn":
        # Check to see if pawn on starting spot and allow double move
        if start[1] in [1, 6]:
            jump = 2
        else:
            jump = 1

        # Check to see if pawn is moving in correct direction
        if (colour == "white" and (start[1] - end[1] > 0)) or (
            colour == "black" and (start[1] - end[1] < 0)
        ):
            # Check to see if no lateral movement and allowed forward jump
            if start[0] == end[0] and abs(start[1] - end[1]) <= jump:
                return True

    return False


def plot_board(colour=None, piece=None, start=None, end=None) -> tuple:
    """
    Function to provide board array for plotting and image URL for chosen piece
    """

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
    """
    Function to convert chess notation into coordinates
    """
    coord = coord.strip()

    letters = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}

    x = letters[coord[0].upper()]
    y = 8 - int(coord[1])

    return (x, y)
