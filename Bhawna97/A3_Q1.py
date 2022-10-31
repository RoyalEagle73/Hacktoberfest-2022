def maxmod(A):
    res = 0
    for i in A:
        for j in A:
            if (i%j > res):
                res = i%j
    return res

A1 = [1,2,44,3]
A2 = [2,6,4]
print('Output1:', maxmod(A1))
print('Output2:', maxmod(A2))
