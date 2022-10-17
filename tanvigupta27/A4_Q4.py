A = ['a','aa','aab','b','bb','bba','bbb']
B = 'bb'
C = ['a','b']
D = 'c'

def prefix_matching(A,B):
    
    res = []
    for index, i in enumerate(A):
        if B in i:
            res.append(index)
    if(res):
        print(res[::len(res)-1])
    else:
        print("[-1,-1")
    return
print("Output 1:")
prefix_matching(A,B)
print("Output 2:")
prefix_matching(C,D)


