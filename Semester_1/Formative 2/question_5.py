from copy import deepcopy


class Blotris:
    """Class containing all the methods for the blotris game
    """

    def __init__(self, rows, cols):
        """Initialise the Blotris Class with a board with "row" rows and "col" columns

        Args:
            rows (int): How many rows the board has
            cols (int): How many columns the board has

        Raises:
            ValueError: If the board is too small (row or col is less that 5)
        """
        self._rows, self._cols = rows, cols
        if rows < 5 or cols < 5:  # too small board
            raise ValueError("The board must be at least 5 by 5")
        self._board = [[0 for _ in range(cols)]for _ in range(rows)]

    def add(self, shape, row, col):
        """Adds a shape to the board if possible

        Args:
            shape (list of lists): The definition of the shape e.g:
                                   [[1, 1], [1, 0], [1, 0], [1, 0]

            row (int): Which row the top left of the shape should be 
            col (int): Which column the top left of the shape should be 

        Returns:
            bool: True if the shape was placed, else False
        """
        # assume it can be placed
        if row < 0 or col < 0:  # placed outside the grid to the top left
            return False

        width, height = len(shape[0]), len(shape)
        if col + width > self._cols or height + row > self._rows:  # the shape would go out the board
            return False
        board_copy = deepcopy(self._board)
        for i, r in enumerate(shape):
            global_row = i + row
            for j, c in enumerate(r):
                global_col = j + col
                if board_copy[global_row][global_col] == 1 and c == 1:  # block there already
                    return False
                if c == 1:
                    board_copy[global_row][global_col] = 1

        self._board = board_copy
        return True

    def update(self):
        """Checks if any rows are full and can be removed.
           If so it removes the row and shifts all the
           rows above down. The size of the board remains
           the same
        """
        for i, _ in enumerate(reversed(self._board)):
            if 0 not in self._board[i]:  # full row
                for j in range(i, 0, -1):
                    self._board[j] = self._board[j-1].copy()
                # pad the top with 0 to maintain size
                self._board[0] = [0]*len(self._board[0])
