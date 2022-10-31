def gcd(A,B):
    while(A!=B):
        if(A > B):
            A -= B
        else:
            B -= A
    return A%(10^9)

A = 4
B = 6
C = 6
D = 7
print('Output1: \n', gcd(A,B))
print('Output2: \n', gcd(C,D))
