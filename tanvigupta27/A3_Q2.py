# Approach 1
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

# Approach 2: O(n)
def xor_of_sublist(array,N):
    res = 0
    for i in range(N):
        value = (i+1)*(N-i)
        if(value%2 == 1):
            res = res^array[i]
    return res
    
print("Output 1: ")    
array = [1,2,3]
N = len(array)
print(xor_of_sublist(array,N))

print("Output 2: ")    
array = [4,5,7,5]
N = len(array)
print(xor_of_sublist(array,N))
