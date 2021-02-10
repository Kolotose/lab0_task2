"""
Repository link https://github.com/Kolotose/lab0_task2.git
"""

def read_board(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> read_board("board.txt")
    ["**** ****", "***1 ****", "**  3****", \
     "* 4 1****", "     9 5 ", " 6  83  *", \
     "3   1  **", "  8  2***", "  2  ****"]
    """
    with open(path, 'r', encoding='utf-8') as file:
        board = file.readlines()
    file.close()

    return board

def check_board_complete(board: list):
    """
    Checks if the board is completed with all the numbers

    >>> check_board_complete(["**** ****", "***1 ****", "**  3****", \
                              "* 4 1****", "     9 5 ", " 6  83  *", \
                              "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    for line in board:
        for element in line:
            if element == ' ':
                return False

    return True

def check_board_size(board:list):
    """
    Used in validate_board()

    Checks if the board is 9x9

    >>> check_board_size(["**** ****", "***1 ****", "**  3****", \
                          "* 4 1****", "     9 5 ", " 6  83  *", \
                          "3   1  **", "  8  2***", "  2  ****"])
    True
    """
    if len(board) != 9:
        return False
    
    for line in board:
        if len(line) != 9:
            return False

    return True

def check_board_form(board: list):
    """
    Used in validate_board()

    Checks if the board is correct form

    >>> check_board_form(["**** ****", "***1 ****", "**  3****", \
                          "* 4 1****", "     9 5 ", " 6  83  *", \
                          "3   1  **", "  8  2***", "  2  ****"])
    True
    """
    # Checking if stars are not placed where they do not need to be
    for i in range(5):
        # 5, because we have to have (8, 0), (7, 1), ..., (4, 4) be filled
        # and it is 5 cells. We will be leaning on them (shape similar to L)
        if board[8-i][i] == '*':
            return False
        
        for j in range(1, 5):
            if board[8-i-j][i] == '*' or board[8-i][i+j] == '*':
                return False

    # Checking if the tiles are not placed where they do not need to be
    for i in range(4):
        # Top right square
        for j in range(4):
            if board[i][8-j] != '*':
                return False
        
        # Top left and bottom right square
        for j in range(4-i):
            if board[i][j] != '*' or board[8-i][8-j] != '*':
                return False

    return True

def check_numbers(board: list):
    """
    Used in validate_board()

    Checks if the numbers in same columns, rows and colours are different

    >>> check_numbers(["**** ****", "***1 ****", "**  3****", \
                       "* 4 1****", "     9 5 ", " 6  83  *", \
                       "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> check_numbers(["**** ****", "***1 ****", "**  3****", \
                       "* 4 1****", "     9 5 ", " 6  83  *", \
                       "3      **", "  8  2***", "  2  ****"])
    True
    """
    if rows_check(board) and \
       columns_check(board) and \
       color_check(board):
        # All conditions are satisfied
        return True
    
    return False


def rows_check(board: list):
    """
    Used in check_numbers()

    Checks if the numbers in same rows are different

    >>> rows_check(["**** ****", "***1 ****", "**  3****", \
                    "* 4 1****", "     9 5 ", " 6  83  *", \
                    "3   1  **", "  8  2***", "  2  ****"])
    True
    """
    for line in board:
        numbers_in_line = []
        for element in line:
            if element.isnumeric():
                numbers_in_line.append(element)
        
        if check_uniqueness(numbers_in_line) == False:
            return False
    
    return True

def columns_check(board: list):
    """
    Used in check_numbers()

    Checks if the numbers in same columns are different

    >>> columns_check(["**** ****", "***1 ****", "**  3****", \
                       "* 4 1****", "     9 5 ", " 6  83  *", \
                       "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    for j in range(9):
        numbers_in_column = []
        for i in range(9):
            if board[i][j].isnumeric():
                numbers_in_column.append(board[i][j])
        
        if check_uniqueness(numbers_in_column) == False:
            return False
    
    return True

def color_check(board: list):
    """
    Used in check_numbers()

    Checks if the numbers in same columns are different

    >>> color_check(["**** ****", "***1 ****", "**  3****", \
                     "* 4 1****", "     9 5 ", " 6  83  *", \
                     "3   1  **", "  8  2***", "  2  ****"])
    True
    """
    for i in range(5):
        numbers_in_colour = []
        numbers_in_colour.append(board[8-i][i])
        
        for j in range(1, 5):
            numbers_in_colour.append(board[8-i-j][i])
            numbers_in_colour.append(board[8-i][i+j])

        if check_uniqueness(numbers_in_colour) == False:
            return False
    
    return True

def check_uniqueness(list_of_numbers: list):
    """
    Used in color_check(), rows_check(), columns_check()

    Checks if the numbers in list are unique

    >>> check_uniqueness(['1', '2', '3', '4', '6', '7', '8', '9'])
    True
    >>> check_uniqueness(['1', '2', '3', '4', '5', '6', '7', '1'])
    False
    """
    for number in range(1, 10):
        amount = list_of_numbers.count(str(number))
        if amount > 1:
            return False

    return True

def validate_board(board: list):
    """
    Main function

    Checks if the board is ready for the game

    >>> validate_board(["**** ****", "***1 ****", "**  3****", \
                        "* 4 1****", "     9 5 ", " 6  83  *", \
                        "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    if check_board_size(board) and \
       check_board_form(board) and \
       check_numbers(board):
            return True

    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()