def solution(n):
        saved = {}
        right_height = 0
        right_sum = 0
        return part(n, right_height, right_sum, saved)


def part(n, right_height, right_sum, saved):
    parts = []
    layer = 0
    count = 0
    parts.append(valid_parts(n, right_height, right_sum))
    while len(parts) > 0:
        layer = parts.pop(0)
        count = count + len(layer)
        while len(layer) > 0:
            p = layer.pop(0)
            if p in saved:
                count = count + saved[p]
            else:
                valid_p = valid_parts(n, p[0], p[1])
                if len(valid_p) > 0:
                    parts.append(valid_p)
                    saved[p] = part(n, p[0], p[1], saved)
    return count

def valid_parts(n, right_height, right_sum):
    parts = []
    left_sum = n - right_sum
    i = 0
    while i < left_sum/2:
        if i > right_height:
            parts.append((i, i+right_sum))
        i = i + 1
    return parts
