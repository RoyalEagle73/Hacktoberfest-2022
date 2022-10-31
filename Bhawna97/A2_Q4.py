def prime_factor(n):
    res = []
    c = 2
    while(n > 1):
        if(n % c == 0):
            res.append(c)
            n = n / c
        else:
            c = c + 1
    return res
            
n = int(input("Enter number: "))
print(prime_factor(n))
