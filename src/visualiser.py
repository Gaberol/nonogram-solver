class Visualiser():
    def __init__(self, projections, width, height):
        self.projections = projections
        self.width = width
        self.height = height

    def draw(self, board):
        rows = []
        for i in range(self.height):
            row = ""
            for num in self.projections[1][i]:
                row += str(num).rjust(2)
            row += "|"
            for square in board[i]:
                if square:
                    row += "■│"
                else:
                    row += " │"
            rows.append(row)

        maxrow = len(max(rows, key=len))
        topmax = len(max(self.projections[0], key=len))

        output = "\n" + "─" * maxrow + "\n\n"

        for i in range(topmax):
            row = ""
            for column in self.projections[0]:
                if len(column) >= topmax - i:
                    row += str(column[i-(topmax-len(column))]).ljust(2)
                else:
                    row += "  "
            output += row.rjust(maxrow) + "\n"
        
        output += ("┌" + "─┬" * (self.width-1) + "─┐").rjust(maxrow) + "\n"

        for i in range(len(rows)):
            output += rows[i].rjust(maxrow) + "\n"
            if i < len(rows)-1:
                output += ("├" + "─┼" * (self.width-1) + "─┤").rjust(maxrow) + "\n"

        output += ("└" + "─┴" * (self.width-1) + "─┘").rjust(maxrow) + "\n"

        print(output)