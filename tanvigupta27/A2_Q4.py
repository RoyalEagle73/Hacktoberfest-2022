n = int(input("Enter number: "))
print(n)
def prime_factor(n):
    c = 2
    while(n > 1):
        if(n % c == 0):
            print(c, end=" ")
            n = n / c
        else:
            c = c + 1
    return
prime_factor(n)