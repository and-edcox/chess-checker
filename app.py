from chess import plot_board, can_move
from flask import Flask, request, render_template

# Coordinates for html dropdown
COORDS = []
for letter in ["A", "B", "C", "D", "E", "F", "G", "H"]:
    for i in range(8):
        COORDS.append(f"{letter}{i+1}")

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    # Initial load of the app
    if request.method == "GET":

        move = None

        board, image_url = plot_board()

    else:
        colour = request.form.get("colour")
        piece = request.form.get("piece")
        start = request.form.get("start")
        end = request.form.get("end")

        move = can_move(colour, piece, start, end)
        print(move)

        board, image_url = plot_board(colour, piece, start, end)

    return render_template(
        "home.html", coords=COORDS, check_move=move, board=board, url=image_url
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
