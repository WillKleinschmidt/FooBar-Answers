def solution(l):
    l_split = []
    for e in l:
        l_split.append(split(e))
    l_split_major = reorder(l_split, 0)
    l_split_minor = split_list(l_split_major, 0)
    l_split_rev = []
    for major in l_split_minor:
        major = reorder(major, 1)
        minor = split_list(major, 1)
        l_split_rev.append(minor)
    inorder = []
    for minor in l_split_rev:
        for rev in minor:
            rev = reorder(rev, 2)
            for e in rev:
                version = reform(e)
                inorder.append(version)
    return inorder
    
def split(e):
    e = e + '.'
    version = []
    i = 0
    major = False
    minor = False
    rev = False
    cur = 0
    cur_str = ""
    while i < len(e):
        if e[i] == '.':
            if(major == True and minor == True and rev == False):
                version.append(cur)
                cur = 0
                cur_str = ""
                rev = True
            if(major == True and minor == False):
                version.append(cur)
                cur = 0
                cur_str = ""
                minor = True
            if(major == False):
                version.append(cur)
                cur = 0
                cur_str = ""
                major = True
        if e[i] in "1234567890":
            cur_str = cur_str + e[i]
            cur = int(cur_str)
        i = i + 1
    if(minor == False):
        version.append(-1)
    if(rev == False):
        version.append(-1)
    return version


def reorder(l, m):
    l.sort(key=lambda x: x[m],reverse=False)
    return l

def reform(version):
    version_string = str(version[0])
    if version[1] == -1:
        return version_string
    else:
        version_string = version_string + "." + str(version[1])
        if version[2] == -1:
            return version_string
        else:
            version_string = version_string + "." + str(version[2])
    return version_string

def divide(l, m):
    cur_version = l[0][m]
    l_1 = []
    l_2 = []
    for e in l:
        if e[m] == cur_version:
            l_1.append(e)
        else:
            l_2.append(e)

    return(l_1, l_2)

def split_list(l_split_cur, m):
    l_split_next = []
    while(len(l_split_cur) > 0):
        l_1, l_split_cur = divide(l_split_cur, m)
        l_split_next.append(l_1)
    return l_split_next
