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