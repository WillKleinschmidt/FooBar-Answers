def solution(src, dest):
    return search(src, dest)
# @param
#   src: starting node
# @return
#   N: list of nodes that can be reached by src in 1 step
#   NOTE: N[0] stores src
def find_neigbors(src):
    N = []
    N.append(src)
    N.append(is_valid_n(src, 1, -16))
    N.append(is_valid_n(src, 2, -8))
    N.append(is_valid_n(src, 2, 8))
    N.append(is_valid_n(src, 1, 16))
    N.append(is_valid_n(src, -1, 16))
    N.append(is_valid_n(src, -2, 8))
    N.append(is_valid_n(src, -2, -8))
    N.append(is_valid_n(src, -1, -16))
    return N
# @param
#   src: starting node
#   dest: ending node
# @return
#   number of steps from src to dest and -1 on error
def search(src, dest):
    if src == dest:
        return 0
    board = [0] * 64
    step = []
    step.append(find_neigbors(src))
    while len(step) > 0:
        N = step.pop(0)
        while len(N) > 1:
            n = N.pop(1)
            if n == dest:
                board[n] = board[N[0]] + 1
                return board[n]
            if n > 0:
                if board[n] == 0:
                    board[n] = board[N[0]] + 1
                    step.append(find_neigbors(n))
    return -1
# @param
#   src: starting node
#   step1: # of spaces to move left or right
#   step2: # of spaces to move up or down
# @return
#   value of node after doing step1 and step2 from src
#   negative number if step1 or step2 is invalid
def is_valid_n(src, step1, step2):
    if step1 > 0:
        if(src + step1)%8 < (src)%8:
            return -1
        else:
            if step2 > 0:
                if src + step1 + step2 > 63:
                    return -2
            else:
                if src + step1 + step2 < 0:
                    return -3
    else:
        if(src + step1)%8 > (src)%8:
            return -4
        else:
            if step2 > 0:
                if src + step1 + step2 > 63:
                    return -5
            else:
                if src + step1 + step2 < 0:
                    return -6
    return src + step1 + step2
