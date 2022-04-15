''' Function accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise.
The cells of the sudoku board may also contain 0's, which will represent empty cells.
Boards containing one or more zeroes are considered to be invalid solutions.
The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.'''

def valid_solution(board):
    result = False
    for index_x ,x in enumerate(board):
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for index_y ,y in enumerate(x):
            if y in lista:
                lista.remove(y)
            else:
                return print(result)

    for index_x ,x in enumerate(board):
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for index_y ,y in enumerate(x):
            if board[index_y][index_x] in lista:
                lista.remove(board[index_y][index_x])
            else:
                return print(result)

    for index_x in range(0 ,len(board) ,3):
        for index_y in range(0 ,len(board) ,3):
            lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for a in range(3):
                for b in range(3):
                    if board[ a +index_x][ b +index_y] in lista:
                        lista.remove(board[ a +index_x][ b +index_y])
                    else:
                        return print(result)



    return print(True)



valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                   [6, 7, 2, 1, 9, 0, 3, 4, 9],
                                   [1, 0, 0, 3, 4, 2, 5, 6, 0],
                                   [8, 5, 9, 7, 6, 1, 0, 2, 0],
                                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                   [9, 0, 1, 5, 3, 7, 2, 1, 4],
                                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                   [3, 0, 0, 4, 8, 1, 1, 7, 9]])