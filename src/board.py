class Board():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = []
        self._init_board()

    # Initialises empty board, 0 = empty square, 1 = black square
    def _init_board(self):
        for _ in range(self.height):
            row = []
            for __ in range(self.width):
                row.append(0)
            self.board.append(row)

    def mark(self, x, y):
        standard_x = x - 1
        standard_y = self.height - y
        output = "coloured"
        if self.board[standard_y][standard_x]:
            self.board[standard_y][standard_x] = 0
            output = "erased"
        else:
            self.board[standard_y][standard_x] = 1
        return f"{output} ({x},{y})"
    
    def get(self):
        return self.board
