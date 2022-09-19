from chess import Board, check_move
from flask import Flask, request, render_template

BOARD = Board()
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "GET":

        move = None

    else:
        colour = request.form.get("colour")
        piece = request.form.get("piece")
        start = request.form.get("start")
        end = request.form.get("end")

        move = check_move(colour, piece, start, end)

        BOARD.plot_board(move)

    BOARD.plot_board()

    return render_template("home.html", check_move=move, url="/static/images/board.png")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
