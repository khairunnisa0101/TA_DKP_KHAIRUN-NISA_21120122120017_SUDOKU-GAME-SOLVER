#Ukuran
N = 9

#Pengecekan penempatan angka
def isSafe(sudoku, row, col, num):
    for i in range(N):
        if sudoku[row][i] == num:
            return False
        
    for i in range(N):
        if sudoku[i][col] == num:
            return False
        
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if sudoku[startRow + i][startCol + j] == num:
                return False
    return True

#Pengecekan angka yang sama pada blok 3x3
def hasDupBlock(sudoku):
    for i in range(0, N, 3):
        for j in range(0, N, 3):
            block = set()
            for m in range(3):
                for n in range(3):
                    num = sudoku[i+m][j+n]
                    if num != 0:
                        if num in block:
                            return True
                        else:
                            block.add(num)
    return False

#Pengecekan angka yang sama pada baris
def hasDupRow(sudoku, row):
    row_values = set()
    for col in range(N):
        num = sudoku[row][col]
        if num != 0:
            if num in row_values:
                return True
            else:
                row_values.add(num)
    return False

#pengecekan angka yang sama pada kolom
def hasDupCol(sudoku, col):
    column_values = set()
    for row in range(N):
        num = sudoku[row][col]
        if num != 0:
            if num in column_values:
                return True
            else:
                column_values.add(num)
    return False


def solveSudoku(sudoku, row, col):
    if row == N - 1 and col == N:
        return True
    if col == N:
        row += 1
        col = 0
    if sudoku[row][col] > 0:
        return solveSudoku(sudoku, row, col + 1)
    
    for num in range(1, N + 1):
        if isSafe(sudoku, row, col, num):
            sudoku[row][col] = num
            
            if hasDupBlock(sudoku) or hasDupRow(sudoku, row) or hasDupCol(sudoku, col):
                sudoku[row][col] = 0
                return False
            
            if solveSudoku(sudoku, row, col + 1):
                return True
            
            sudoku[row][col] = 0
    return False

def solver(sudoku):
    if solveSudoku(sudoku, 0, 0):
        return sudoku
    else:
        return "no"