A = 6
B = 7
C = 4
D = 6

def gcd(A,B):
    print("A:",A,"B:",B)
    while(A!=B):
        if(A > B):
            A -= B
        else:
            B -= A
    print("GCD:",A%(10^9))
    return
gcd(A,B)
gcd(C,D)