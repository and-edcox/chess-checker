import unittest
from chess import can_move


class TestChess(unittest.TestCase):
    def test_valid_move(self):
        self.assertEqual(
            can_move(colour="white", piece="rook", start="A8", end="D8"), True
        )
        self.assertEqual(
            can_move(colour="white", piece="bishop", start="A8", end="D8"), False
        )


if __name__ == "__main__":
    unittest.main()
