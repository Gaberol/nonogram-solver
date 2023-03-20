This is a solver for the Japanese puzzle game Nonogram. I chose to tackle this problem as I have been addicted to solving nonograms for the past two months and have already developed reliable heuristics for solving these puzzles quickly.

## Primary objective
Find a solution for a correct nonogram puzzle as fast as feasible with a visual representation. The time to solve a chosen puzzle is inherently linked to its size (width x height), so even the fastest solver will struggle with larger puzzles. A high polynomial time complexity is expected.

#### Secondary objectives 
Process random Nonogram puzzles and find all possible solutions or determine that there are none.

## Technology
All code will be written in python, as that is the language I am most comfortable with.

#### Algorithms and data structures
Achieving the objectives of this solver requires implementation of unique data structures and algorithms made to fit the rules of the game. The first step will be to create a line solver, an algorithm that tries to solve the puzzle line-by-line. Use of heuristics will come in handy when attempting to find a solution quickly. Dynamic programming techniques will be necessary when attempting to find all possible solutions.

## Interface
The solver will take text input specifying the size of the board and the numbers along the sides. The solver will put out a visual representation of each step it takes.

## Research
Here are some papers I have taken note of while looking into Nonogram solvers:

[D. Berend, D. Pomeranz, R. Rabani, B. Raziel, "Nonograms: Combinatorial questions and algorithms", _Discrete Applied Mathematics_, vol. 169, pp.30-42, May 2014](https://www.sciencedirect.com/science/article/pii/S0166218X14000080)

[I.C. Wu, D.J. Sun, L.P. Chen, K.Y Chen, C.H. Kuo, H.H. Kang, H.H. Lin, "An Efficient Approach to Solving Nonograms", _IEEE transactions on computational intelligence and AI in games_, vol. 5, no. 3, pp. 251-264, Sep. 2013](https://ir.nctu.edu.tw/bitstream/11536/22772/1/000324586300005.pdf)

[R.A. Oosterman, "Complexity and solvability of Nonogram puzzles", Master's thesis, Fac. Sci. Eng, Univ. Groningen, Groningen, 2017](https://fse.studenttheses.ub.rug.nl/15287/1/Master_Educatie_2017_RAOosterman.pdf)

There's also this website:

[Theory - Nonogram Solver](https://ssjools.hopto.org/nonogram/theory#ambiprobs)

I have also looked at other people's solutions to this problem on the github topic page:

[nonogram-solver - Github Topics](https://github.com/topics/nonogram-solver)

## Course-specific stuff
I can read Python. I understand both Finnish and English, but this project will be done entirely in English. My study program is TKT-kandi.

