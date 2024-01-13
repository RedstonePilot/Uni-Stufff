from collections import deque


class ColourPuzzle:
    def __init__(self, puzzle):
        self._board = puzzle.copy()
        if len(self._board) != 4 or len(self._board[0]) != 4:
            raise ValueError

        self._zero_place = [0, 0]
        one = two = three = zero = 0
        for y, row in enumerate(self._board):
            for x, sq in enumerate(row):
                match sq:
                    case 1:
                        one += 1
                    case 2:
                        two += 1
                    case 3:
                        three += 1
                    case 0:
                        zero += 1
                        self._zero_place = [x, y]
        if one != 5 or two != 5 or three != 5 or zero != 1:
            raise ValueError

    def matchPattern(self, pattern):
        return pattern == [self._board[1][1:3], self._board[2][1:3]]

    def _update_zero(self):
        for y, row in enumerate(self._board):
            for x, sq in enumerate(row):
                if sq == 0:
                    self._zero_place = [x, y]
                    break

    def moveLowerTile(self):
        self._update_zero()
        if self._zero_place[1] == 3:  # ie bottom of board
            return False
        self._board[self._zero_place[1]][self._zero_place[0]], self._board[self._zero_place[1]+1][self._zero_place[0]
                                                                                                  ] = self._board[self._zero_place[1]+1][self._zero_place[0]], self._board[self._zero_place[1]][self._zero_place[0]]
        self._zero_place[1] -= 1
        return True

    def moveUpperTile(self):
        self._update_zero()
        if self._zero_place[1] == 0:  # ie top of board
            return False
        self._board[self._zero_place[1]][self._zero_place[0]], self._board[self._zero_place[1]-1][self._zero_place[0]
                                                                                                  ] = self._board[self._zero_place[1]-1][self._zero_place[0]], self._board[self._zero_place[1]][self._zero_place[0]]
        self._zero_place[1] += 1
        return True

    def moveLeftTile(self):
        self._update_zero()
        if self._zero_place[0] == 0:  # ie left of board
            return False
        self._board[self._zero_place[1]][self._zero_place[0]], self._board[self._zero_place[1]][self._zero_place[0] - 1
                                                                                                ] = self._board[self._zero_place[1]][self._zero_place[0] - 1], self._board[self._zero_place[1]][self._zero_place[0]]
        self._zero_place[0] -= 1
        return True

    def moveRightTile(self):
        self._update_zero()
        if self._zero_place[0] == 3:  # ie right of board
            return False
        self._board[self._zero_place[1]][self._zero_place[0]], self._board[self._zero_place[1]][self._zero_place[0] + 1
                                                                                                ] = self._board[self._zero_place[1]][self._zero_place[0]+1], self._board[self._zero_place[1]][self._zero_place[0]]
        self._zero_place[0] += 1
        return True

    def solvable(self, pattern, n):
        if self.matchPattern(pattern):
            return True
        if n == 0:
            return False
        for move in [self.moveUpperTile, self.moveLowerTile, self.moveLeftTile, self.moveRightTile]:
            original_board = [row[:] for row in self._board]
            if move():
                if self.solvable(pattern, n - 1):
                    self._board = original_board
                    return True
            self._board = original_board  # undo the move
        return False
