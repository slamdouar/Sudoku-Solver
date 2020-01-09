sudoku = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#Here we try to see if there is any empty cells on the sudoku
def find_empty_cells(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j]==0:
                return(i,j)
#This is a function to chek if we can input a number on a given cell in the sudoku
def check_valid(sudoku, num, cell):
    #Check row and column
    for i in range(9):
        if sudoku[i][cell[1]]==num and i!=cell[0]:
            return False
        if sudoku[cell[0]][i]==num and i!=cell[1]:
            return False
    #Check box
    p_x=cell[0]//3
    p_y=cell[1]//3
    for i in range(p_x*3,p_x*3+3):
        for j in range(p_y*3,p_y*3+3):
            if sudoku[i][j]==num and i!=cell[0] and j!=cell[1]:
                return False
    return True

#backtracking algorithm to solve the sudoku
def sudoku_solver(sudoku):
    empty_cell=find_empty_cells(sudoku)
    #If there are no empty cells, then the sudoku is solved
    if not empty_cell:
        return True
    #Recursive try to solve the solution
    for i in range(1,10):
        if check_valid(sudoku, i, empty_cell):
            sudoku[empty_cell[0]][empty_cell[1]]=i
            #when we input a value, we try to solve it again until we reach a final solution
            if sudoku_solver(sudoku):
                return True
            #if we can't solve it, it ;eans that it is the wrong value so we go on to the next
            sudoku[empty_cell[0]][empty_cell[1]]=0
    return False

#This is a function to print the sudoku in a nice way
def print_board(sudoku):
    for i in range(9):
        if i%3==0 and i!=0:
            print('- - - - - - - - - - - -')
        for j in range(9):
            if j%3==0:
                print('| ',end='')
            if j==8:
                print(sudoku[i][j])
            else:
                print(sudoku[i][j],end=' ')
print("Let's try to solve this sudoku")
print_board(sudoku)
if sudoku_solver(sudoku):
    print('Like a boss!')
    print_board(sudoku)
else:
    print('Oopsies, this sudoku is not solvable')
