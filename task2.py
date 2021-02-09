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