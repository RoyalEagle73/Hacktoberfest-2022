def prefix_matching(A,B):
    res = []
    for index, i in enumerate(A):
        if B in i:
            res.append(index)
    if(res):
        return res[::len(res)-1]
    else:
        return [-1,-1]
    return

A = ['a','aa','aab','b','bb','bba','bbb']
B = 'bb'
C = ['a','b']
D = 'c'
print("Output 1:\n", prefix_matching(A,B))
print("Output 2:\n", prefix_matching(C,D))
