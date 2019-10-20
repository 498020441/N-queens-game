def num_placements_all(n):
    fact_n = 1
    fact_r = 1
    fact_n_minues_r = 1
    for i in range(1, n*n+1):
        fact_n = fact_n*i

    for i in range(1, n+1):
        fact_r = fact_r*i

    for i in range(1, n*n-n+1):
        fact_n_minues_r = fact_n_minues_r*i

    return int(fact_n/(fact_r*fact_n_minues_r))


def num_placements_one_per_row(n):
    return n**n


def n_queens_valid(board):
    check_list = []
    counter = 0
    for element in board:
        if element in check_list:
            return False
        else:
            check_list.append(element)
            counter += 1
            ctr = 1
            for i in range(counter, len(board)):
                if (check_list[counter-1]+ctr == board[i]) or (check_list[counter-1]-ctr == board[i]):
                    return False
                ctr += 1
    return True

#dfs searching
def n_queens_solutions(n):
    global solution_list
    solution_list = []
    n_queens_helper(n, [])
    result = (elem for elem in solution_list)
    return result


def n_queens_helper(n, board):
    if len(board) == n:
        solution_list.append(board[:])
    else:
        for i in range(n):
            board.append(i)
            if not n_queens_valid(board):
                board.pop()
            else:
                n_queens_helper(n, board)
                board.pop()
