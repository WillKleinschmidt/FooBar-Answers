import numpy as np

def solution(l):
    count = 0
    map = np.zeros((len(l)))
    for i in range(0, len(l)):
        for j in range(i+1, len(l)):
            if l[j]%l[i] == 0:
                map[j] = map[j] + 1
                count = count + map[i]
    return int(count)
