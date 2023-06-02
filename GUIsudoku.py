from tkinter import *
from solver import solver
import sys

class SudokuSolver:
    def __init__(self, root):
        self.root = root
        self.N = 9
        self.cells = {}

        self.root.title("Sudoku Solver")
        self.root.geometry("324x450")
        self.root.config(bg="#ecc5c0")

        label = Label(self.root, text="Isikan angka lalu klik Solve" , bg= "#ecc5c0").grid(row=0, column=0, columnspan=10)

        self.errLabel = Label(self.root, text="", fg="red", bg= "#ecc5c0")
        self.errLabel.grid(row=15, column=1, columnspan=15, pady=7)

        self.solvedLabel = Label(self.root, text="", fg="green", bg ="#ecc5c0")
        self.solvedLabel.grid(row=15, column=1, columnspan=20, pady=5)
        

        self.reg = self.root.register(self.validateNumber)

        self.draw9x9Grid()

        btn = Button(self.root, command=self.getValues, text="Solve", width=10, bg= "#6afb92")
        btn.grid(row=20, column=1, columnspan=5, pady=10)

        btn = Button(self.root, command=self.clearValues, text="Clear", width=10 ,bg="#eb5406")
        btn.grid(row=20, column=5, columnspan=5, pady=10)
        
        btn = Button(self.root, command=self.exitProgram, text="Exit", width=10, bg="#808080")
        btn.grid(row=23, column=3, columnspan=5, pady=10)

    def validateNumber(self, P):
        out = (P.isdigit() or P == "") and len(P) < 2
        return out

    def draw3x3Grid(self, row, column, bgcolor):
        for i in range(3):
            for j in range(3):
                e = Entry(self.root, width=5, bg=bgcolor, justify="center", validate="key",
                          validatecommand=(self.reg, "%P"))
                e.grid(row=row+i+1, column=column+j+1, sticky="nsew", padx=1, pady=1, ipady=5)
                self.cells[(row+i+1, column+j+1)] = e

    def draw9x9Grid(self):
        color = "#D0ffff"
        for rowNo in range(1, 10, 3):
            for colNo in range(0, 9, 3):
                self.draw3x3Grid(rowNo, colNo, color)
                if color == "#D0ffff":
                    color = "#ffffd0"
                else:
                    color = "#D0ffff"

    def clearValues(self):
        self.errLabel.configure(text="")
        self.solvedLabel.configure(text="")
        for row in range(2, 11):
            for col in range(1, 10):
                cell = self.cells[(row, col)]
                cell.delete(0, "end")

    def getValues(self):
        board = []
        self.errLabel.configure(text="")
        self.solvedLabel.configure(text="")
        for row in range(2, 11):
            rows = []
            for col in range(1, 10):
                val = self.cells[(row, col)].get()
                if val == "":
                    rows.append(0)
                else:
                    rows.append(int(val))

            board.append(rows)
            
        if self.isBoardFull(board):
            self.solvedLabel.configure(text="Papan sudah penuh!" , fg= "orange")
        else:
            self.updateValue(board)

    def updateValue(self, s):
        sol = solver(s)
        if sol != "no":
            for rows in range(2, 11):
                for col in range(1, 10):
                    self.cells[(rows, col)].delete(0, "end")
                    self.cells[(rows, col)].insert(0, sol[rows - 2][col - 1])
            self.solvedLabel.configure(text="Sudoku terselesaikan!")
        else:
            self.errLabel.configure(text="Tidak ada solusi   yang mungkin!")
    
    def isBoardFull(self, board):
        for row in board:
            if 0 in row:
                return False
        return True
    
    def exitProgram(self):
        self.root.destroy()
        sys.exit() 

if __name__ == "__main__":
    root = Tk()
    app = SudokuSolver(root)
    root.mainloop()