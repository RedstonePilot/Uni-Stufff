import random


class GameBoard:
    def __init__(self):
        self.PLAYER1 = 1
        self.PLAYER2 = 2
        self._board = [[0 for _ in range(7)] for _ in range(6)]

    def __str__(self):
        top = []
        close = ("+---"*len(self._board[0])+"+\n")
        top.append(close)
        for row in self._board:
            tmp = []
            for cell in row:
                if cell == 0:
                    add = " - "
                elif cell == self.PLAYER1:
                    add = " X "
                else:
                    add = " O "
                tmp.append(f"|{add}")
            tmp.append("|\n")
            top.append("".join(tmp))
            top.append(close)
        tmp = [f"| {i} "for i in range(len(self._board[0]))]
        tmp.append("|\n")
        top.append("".join(tmp))
        top.append(close)
        return "".join(top)

    def get_move(self, move, player):
        for row in reversed(self._board):
            if row[move] == 0:
                row[move] = player
                break

    def get_valid_move(self):
        return [i for i, cell in enumerate(self._board[0]) if cell == 0]

    def iswinner(self, player):
        for row in self._board:
            for i in range(len(row) - 3):
                if row[i] == player and row[i+1] == player and row[i+2] == player and row[i+3] == player:
                    return True

        for j in range(len(self._board[0])):
            for i in range(len(self._board) - 3):
                if self._board[i][j] == player and self._board[i+1][j] == player and self._board[i+2][j] == player and self._board[i+3][j] == player:
                    return True

        for i in range(len(self._board) - 3):
            for j in range(len(self._board[0]) - 3):
                if self._board[i][j] == player and self._board[i+1][j+1] == player and self._board[i+2][j+2] == player and self._board[i+3][j+3] == player:
                    return True

        for i in range(len(self._board) - 3):
            for j in range(3, len(self._board[0])):
                if self._board[i][j] == player and self._board[i+1][j-1] == player and self._board[i+2][j-2] == player and self._board[i+3][j-3] == player:
                    return True

        return False


game = GameBoard()
for _ in range(56):
    game.get_move(random.choice(game.get_valid_move()), game.PLAYER1)
    game.get_move(random.choice(game.get_valid_move()), game.PLAYER2)


print(game)

print(game.iswinner(game.PLAYER1))
