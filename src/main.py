from visualiser import Visualiser
from board import Board


# The numbers on the side of the puzzle are represented by this tuple of tuples
# First tuple contains the numbers on the top (left to right)
# Second contains the numbers on the left (top to bottom)
PROJECTIONS = (((2,1), (3,1), (1,3), (3,1), (2,1)),
               ((5,), (2,2), (3,), (1,), (5,))
              )

class Main():
    def __init__(self, projections):
        self.projections = projections
        self.width = len(self.projections[0])
        self.height = len(self.projections[1])
        self.visualiser = Visualiser(self.projections, self.width, self.height)   
        self.board = Board(self.width, self.height)

    def main_loop(self):
        count = 0
        while True:
            self.visualiser.draw(self.board.get())

            # temporary code for testing
            x = int(input("x coordinate: "))
            y = int(input("y coordiante: "))
            print(self.board.mark(x, y))
            count += 1
            if count == 18:
                if self.board.check(self.projections):
                    print("Correct!")
                else:
                    print("Incorrect :(")
                break
            

if __name__ == "__main__":
    test = [3, 4, 5]
    test2 = []
    test2.append(test[0])
    print(test2.pop())
    print(test2)
    print(test)
    program = Main(PROJECTIONS)
    program.main_loop()
