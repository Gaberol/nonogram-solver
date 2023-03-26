from visualiser import Visualiser


# The numbers on the side of the puzzle are represented by this tuple of tuples
# First tuple contains the numbers on the top (left to right)
# Second contains the numbers on the left (top to bottom)
PROJECTIONS = (((2,1), (3,1), (1,3), (3,1), (2,1)),
               ((5,), (2,2), (3,), (1,), (5,))
              )

class Main():
    def __init__(self, projections) -> None:
        self.projections = PROJECTIONS
        self.width = len(self.projections[0])
        self.height = len(self.projections[1])
        self.visualiser = Visualiser(self.projections, self.width, self.height)   
        self.board = []
        self._init_board()

    # Initialises empty board, 0 = empty square, 1 = black square
    def _init_board(self):
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(0)
            self.board.append(row)

    def main_loop(self):
        while True:
            self.visualiser.draw(self.board)

            # temporary code for testing
            x = int(input("x coordinate: ")) - 1
            y = self.height - int(input("y coordiante: "))
            if self.board[y][x]:
                self.board[y][x] = 0
            else:
                self.board[y][x] = 1
            

if __name__ == "__main__":
    program = Main(PROJECTIONS)
    program.main_loop()
