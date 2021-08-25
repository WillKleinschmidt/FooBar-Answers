import copy
# copy is used to make deep copies of map so that updates to these 
# copies do not change map

def solution(map):
    min_dist = search(map)
    y = len(map)
    x = len(map[0])
    if x < 2 and y < 2: # trivial case
        return 1
    for j in range(0, y): # checking every case of removing 1 wall
        for i in range(0, x):
            next_m = next_map(map, i, j)
            next_dist = search(next_m)
            if next_dist < min_dist:
                min_dist = next_dist
    return min_dist
# @param
#   map: list of open spaces and walls
#   i: column number
#   j: row number
# @return
#   next_map: map with wall removed at i, j
def next_map(map, i, j):
    next_map = copy.deepcopy(map)
    if map[j][i] == 1:
        next_map[j][i] = 0
    return next_map
# @param
#   map: list of open spaces and walls
# @return
#   number of steps from (0,0) to (w-1, h-1) or 401 on failure
def search(map):
    src = [0, 0]
    y = len(map)
    x = len(map[0])
    dist = copy.deepcopy(map)
    dest = [x-1, y-1]
    for m in range(0, y):
        for n in range(0, x):
            if dist[m][n] == 1:
                dist[m][n] = -1
    step = []
    step.append(find_neigbors(dist, 0, 0))
    while len(step) > 0:
        N = step.pop(0)
        while len(N) > 1:
            nx, ny = N.pop(1)
            n0x, n0y = N[0]
            if [nx, ny] == dest:
                dist[ny][nx] = dist[n0y][n0x] + 1
                return (dist[ny][nx] + 1)
            if nx >= 0:
                if dist[ny][nx] == 0:
                    dist[ny][nx] = dist[n0y][n0x] + 1
                    step.append(find_neigbors(dist, nx, ny))
                    
    return 401 # longer than any possible path
# @param
#   map: list of open spaces and walls
#   i: column number
#   j: row number
# @return
#   N: i,j and a list of neigbors to i, j 
def find_neigbors(map, i, j):
    N = []
    N.append([i, j])
    N.append(is_valid_n(map, i, j+1))
    N.append(is_valid_n(map, i, j-1))
    N.append(is_valid_n(map, i+1, j))
    N.append(is_valid_n(map, i-1, j))
    return N
# @param
#   map: list of open spaces and walls
#   i: column number
#   j: row number
# @return
#   i: i if valid -1 if invalid  
#   j: j if valid -1 if invalid  
def is_valid_n(map, i, j):
    y = len(map)-1
    x = len(map[0])-1
    if i > x or i < 0:
        return [-1, -1]
    if j > y or j < 0:
        return [-1, -1]
    if map[j][i] < 0:
        return [-1, -1]
    return [i, j]
