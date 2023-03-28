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

    # Turns the rows and columns of the board matrix
    # into a list of simple rows for easier checking
    def _make_rows(self):
        rows = []
        for row in self.board:
            rows.append(row[::-1])
        for i in range(self.width):
            column = []
            for j in reversed(range(self.height)):
                column.append(self.board[j][i])
            rows.append(column)
        return rows
    
    def _check_rows(self, rows, projections):
        for i in range(self.height * 2):
            if i >= self.height:
                proj = i - self.height
                rows_or_columns = projections[0]
            else:
                proj = i
                rows_or_columns = projections[1]
            for j in range(len(rows_or_columns[proj])):
                block_len = rows_or_columns[proj][j]
                count = 0
                row = rows[i]
                while row:
                    if row.pop():
                        count += 1
                        if count == block_len:
                            if row and row.pop(): return False
                            continue
                    elif count > 0: return False
                    else:
                        print("error")
                        break
                if count < block_len: return False
        return True

    def check(self, projections):
        rows = self._make_rows()
        if self._check_rows(rows, projections):
            return True
        else:
            return False

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
