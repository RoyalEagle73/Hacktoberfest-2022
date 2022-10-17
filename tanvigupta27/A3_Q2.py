A = [3,4,5]
B = [1,2,3]
C = [4,5,7,5]
def xor_of_list(A):
    res = []
    result = []
    for i in range(len(A)+1):
        for j in range(i+1, len(A)+1):
            res.append(A[i:j])
    print("res:",res)
    for i in res:
        result.extend(i) if isinstance(i, list) else result.append(i)
        ans = 0
        for i in range(len(result)):
            ans = ans^result[i]
    print(ans)
    return 
xor_of_list(A)
xor_of_list(B)
xor_of_list(C)
