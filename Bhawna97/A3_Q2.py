def xor_of_sublist(array,N):
    res = 0
    for i in range(N):
        value = (i+1)*(N-i)
        if(value%2 == 1):
            res = res^array[i]
    return res
    
array = [1,2,3]
N = len(array)
print("Output 1: \n", xor_of_sublist(array,N))

array = [4,5,7,5]
N = len(array)
print("Output 2: \n", xor_of_sublist(array,N))
