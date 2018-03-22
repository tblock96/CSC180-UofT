"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 20, 2016
"""

def is_empty(board):
    for i in board:
        for j in i:
            if j == "b" or j == "w":
                return False
    return True

def is_bounded(board, y_end, x_end, length, d_y, d_x):
    res = 0
    if not y_end + d_y in range(len(board)) or\
    not x_end + d_x in range(len(board[0])):
        res += 1
    elif board[y_end + d_y][x_end + d_x] != " ":
        res += 1
    if not y_end - (length * d_y) in range(len(board)) or\
    not x_end - (length * d_x) in range(len(board[0])):
        res += 1
    elif board[y_end - (length * d_y)][x_end - (length * d_x)] != " ":
        res += 1
    return ["OPEN", "SEMIOPEN", "CLOSED"][res]
    
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    open_seq_count, semi_open_seq_count = 0, 0
    row = [[],[],[]]
    for i in range(min((len(board) - y_start * d_y), \
    (len(board[0]) - len(board[0]) * int(d_x < 0) - x_start * d_x))):
        row[0].append(board[y_start + i * d_y][x_start + i * d_x])
        row[1].append(y_start + i * d_y)
        row[2].append(x_start + i * d_x)
    row[0].append(' ')
    seq_length = 0
    for j in range(len(row[0])):
        if row[0][j] == col:
            seq_length += 1
        else:
            if seq_length == length:
                bounded = is_bounded(board, row[1][j-1], row[2][j-1], length, d_y, d_x)
                open_seq_count += (bounded == "OPEN")
                semi_open_seq_count += (bounded == "SEMIOPEN")
                if length == 5:
                    open_seq_count += 1
            seq_length = 0
    # print("detect_row: y_start =", y_start,"; x_start =", x_start,"; d_y =", d_y,"; d_x =", d_x)
    # global waitCount
    # print("Iteration:", waitCount)
    # waitCount += 1
    return open_seq_count, semi_open_seq_count

            
'''def is_bounded(board, y_end, x_end, length, d_y, d_x):
    res = 0
    if not y_end + d_y in range(len(board)) or\
    not x_end + d_x in range(len(board[0])):
        res += 1
    elif board[y_end + d_y][x_end + d_x] != " ":
        res += 1
    if not y_end - (length * d_y) in range(len(board)) or\
    not x_end - (length * d_x) in range(len(board[0])):
        res += 1
    elif board[y_end - (length * d_y)][x_end - (length * d_x)] != " ":
        res += 1
    return ["OPEN", "SEMIOPEN", "CLOSED"][res]
    
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    open_seq_count, semi_open_seq_count = 0, 0
    row = [[],[],[]]
    for i in range(min((len(board) - y_start * d_y), \
    (len(board[0]) - len(board[0]) * int(d_x < 0) - x_start * d_x))):
        row[0].append(board[y_start + i * d_y][x_start + i * d_x])
        row[1].append(y_start + i * d_y)
        row[2].append(x_start + i * d_x)
    seq_length = 0
    for j in range(len(row[0])):
        if row[0][j] == col:
            seq_length += 1
        else:
            if seq_length == length:
                bounded = is_bounded(board, row[1][j-1], row[2][j-1], length, d_y, d_x)
                open_seq_count += (bounded == "OPEN")
                semi_open_seq_count += (bounded == "SEMIOPEN")
            seq_length = 0
    return open_seq_count, semi_open_seq_count'''
    
def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0
    for i in range(len(board)):
        results = detect_row(board, col, i, 0, length, 0, 1)
        open_seq_count += results[0]
        semi_open_seq_count += results[1]
        if i < len(board) - 2:
            results = detect_row(board, col, i, 0, length, 1, 1)
            open_seq_count += results[0]
            semi_open_seq_count += results[1]
        if i == 0:
            for j in range(len(board[0])):
                results = detect_row(board, col, i, j, length, 1, 0)
                open_seq_count += results[0]
                semi_open_seq_count += results[1]
                if j > 0:
                    results = detect_row(board, col, i, j, length, 1, 1)
                    open_seq_count += results[0]
                    semi_open_seq_count += results[1]
                if j > 1:
                    results = detect_row(board, col, i, j, length, 1, -1)
                    open_seq_count += results[0]
                    semi_open_seq_count += results[1]
                if j == len(board[0]) - 1:
                    for k in range(len(board)-1):
                        results = detect_row(board, col, k, j, length, 1, -1)
                        open_seq_count += results[0]
                        semi_open_seq_count += results[1]
    
    return open_seq_count, semi_open_seq_count
    
def search_max(board):
    top_score = -100000
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                board[i][j] = 'b'
                prev_top, top_score = top_score, max(top_score, score(board))
                board[i][j] = 'w'
                top_score = max(top_score, -score(board))
                if prev_top != top_score:
                    move_y, move_x = i, j
                # for colour in ['b', 'w']:
                #     board[i][j] = colour
                #     prev_top, top_score = top_score, max(top_score, \
                #     (int(colour == 'b') * 2 - 1) * score(board))
                #     if prev_top != top_score:
                #         move_y, move_x = i, j
                board[i][j] = " "
    return move_y, move_x

# def search_max(board, col):
#     top_score = -100000
#     other_col = get_other_col(col)
#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             if board[i][j] == " ":
#                 board[i][j] = col
#                 prev_top, top_score = top_score, max(top_score, score(board))
#                 board[i][j] = other_col
#                 top_score = max(top_score, -score(board))
#                 if prev_top != top_score:
#                     move_y, move_x = i, j
#                 # for colour in ['b', 'w']:
#                 #     board[i][j] = colour
#                 #     prev_top, top_score = top_score, max(top_score, \
#                 #     (int(colour == 'b') * 2 - 1) * score(board))
#                 #     if prev_top != top_score:
#                 #         move_y, move_x = i, j
#                 board[i][j] = " "
#     return move_y, move_x
    
# def get_other_col(col):
#     if col == 'b':
#         return 'w'
#     return 'b'

def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])   

    
def is_win(board):
    if score(board) == 100000:
        return "Black won"
    if score(board) == -100000:
        return "White won"
    for i in board:
        for j in i:
            if j == " ":
                return "Continue Playing"
    return "Draw"


def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
                


def analysis(board):
    # for c, full_name in [["b", "Black"], ["w", "White"]]:
    #     print("%s stones" % (full_name))
    #     for i in range(2, 6):
    #         open, semi_open = detect_rows(board, c, i);
    #         print("Open rows of length %d: %d" % (i, open))
    #         print("Semi-open rows of length %d: %d" % (i, semi_open))
    pass
        
    
    

        
    
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        # print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
            
            
        
        # # EXTRA ###
        # print_board(board)
        # #
        # print("Your move (w):")
        # move_y = int(input("y coord: "))
        # if move_y not in range(len(board)):
        #     return "User exited"
        # move_x = int(input("x coord: "))
        move_y, move_x = search_max(board)
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
            
            
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 5, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0, x, length, d_y, d_x) == (1,1):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    board[2][4] = "w"
    print_board(board)
    if detect_rows(board, col, length) == (1,0) and detect_rows(board, col, 2) == (3, 0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


  
            
if __name__ == '__main__':
    print(play_gomoku(25))
    
