sudoku1 = [
    [0,8,7,0,9,0,3,0,2],
    [0,0,0,7,0,0,6,0,0],
    [2,9,0,6,0,0,4,0,1],
    [0,3,4,1,8,0,0,0,0],
    [0,0,6,5,0,9,7,0,0],
    [0,0,0,0,6,7,2,8,0],
    [1,0,2,0,0,5,0,4,7],
    [0,0,8,0,0,6,0,0,0],
    [9,0,5,0,1,0,8,3,0]
    ]

sudoku2 = [
    [0,8,7,0,9,0,3,0,2],
    [0,0,0,7,0,0,6,0,0],
    [2,9,0,6,0,0,4,0,1],
    [0,3,4,1,0,0,0,0,0],
    [0,0,6,5,0,9,7,0,0],
    [0,0,0,0,0,7,2,0,0],
    [1,0,2,0,0,5,0,4,7],
    [0,0,8,0,0,6,0,0,0],
    [9,0,5,0,1,0,8,3,0]
    ]

sudoku3 = [
    [0,0,8,0,7,0,6,0,0],
    [0,1,0,5,6,0,0,0,0],
    [0,2,0,0,0,0,0,0,1],
    [0,6,0,0,0,0,0,0,0],
    [5,7,1,0,3,0,4,9,8],
    [0,0,0,0,0,0,0,7,0],
    [4,0,0,0,0,0,0,6,0],
    [0,0,0,0,4,3,0,5,0],
    [0,0,3,0,5,0,2,0,0]
    ]

sudoku4 = [
    [0,3,8,4,7,1,6,2,5],
    [7,1,4,5,6,2,8,3,9],
    [6,2,5,3,9,8,7,4,1],
    [3,6,9,7,8,4,5,1,2],
    [5,7,1,2,3,6,4,9,8],
    [8,4,2,9,1,5,3,7,6],
    [4,5,7,8,2,9,1,6,3],
    [2,8,6,1,4,3,9,8,7],
    [1,9,3,6,5,7,2,8,4]
    ]

sudoku5 = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    ]


def pre_check(sudoku):
    cur_list = []
    for i in range(len(sudoku)):
        #checks rows
        cur_list.clear()
        for num in sudoku[i]:
            if num in cur_list and num != 0:
                return False
            cur_list.append(num)
        #checks columns
        cur_list.clear()
        for row in sudoku:
            if row[i] in cur_list and row[i] != 0:
                return False
            cur_list.append(row[i])
    #checks boxes
    for i in range(3):
        for j in range(3):
            cur_list.clear()
            for row in range(3):
                for column in range(3):
                    value = sudoku[j*3+column][i*3+row]
                    if value in cur_list and value != 0:
                        return False
                    cur_list.append(value)
    return True

#recursive backtracking method
def solve(sudoku,one_sol):
    #find the first 0
    zero_found = False
    i = 0
    while i < 9 and not zero_found:
        j = 0
        while j < 9 and not zero_found:
            if sudoku[i][j] == 0:
                x = j
                y = i
                zero_found = True
            j += 1
        i += 1
    if not zero_found:
        #finds a solution (no 0's left) and prints it
        print(sudoku)
        return True
    #tries every digit
    for i in range(1,10):
        #creates column list
        column = []
        for row in sudoku:
            column.append(row[x])
        #creates box list
        box = []
        x_box = x // 3
        y_box = y // 3
        for a,v in enumerate(sudoku):
            if y_box == a // 3:
                for b,w in enumerate(v):
                    if x_box == b // 3:
                        box.append(w)
        #only places the digit if there are no conflicts
        if not(i in sudoku[y] or i in column or i in box):
            sudoku[y][x] = i
            if solve(sudoku,one_sol) and one_sol:
                #only stops if a solution is found
                #and that only one solution was asked for
                return True
    #runs if no digit can be placed, so backtracks
    sudoku[y][x] = 0
    return False
def solve_robust(sudoku,one_sol):
    if pre_check(sudoku):
        solve(sudoku,one_sol)
    else:
        print(-1)


solve_robust(sudoku1,True)
