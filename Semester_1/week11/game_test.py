import unittest
from gameboard import GameBoard


class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.game = GameBoard()

    def test_get_valid_move(self):
        valid_moves = self.game.get_valid_move()
        self.assertIsInstance(valid_moves, list)
        self.assertTrue(all(isinstance(move, int) for move in valid_moves))

    def test_iswinner(self):
        # Initially, there should be no winner
        self.assertFalse(self.game.iswinner(self.game.PLAYER1))
        self.assertFalse(self.game.iswinner(self.game.PLAYER2))

        # Simulate a winning condition for PLAYER1
        for _ in range(4):
            self.game.get_move(1, self.game.PLAYER1)
        self.assertTrue(self.game.iswinner(self.game.PLAYER1))

        # Reset the game
        self.game = GameBoard()

        # Simulate a winning condition for PLAYER2
        for _ in range(4):
            self.game.get_move(1, self.game.PLAYER2)
        self.assertTrue(self.game.iswinner(self.game.PLAYER2))


if __name__ == '__main__':
    unittest.main()
