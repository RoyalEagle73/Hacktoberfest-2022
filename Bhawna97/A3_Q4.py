def primeNo(N):
    print("Output:")
    if (N>=1 and N <=300):
        for i in range(2,N+1):
            flag = 0
            for j in range(2,i):
                if(i%j == 0):
                    flag = 1
                    break
            if(flag == 0) and (i!= 1):
                print(i)
    else:
        print("Exit: N > 300")
    return

primeNo(5)
primeNo(10)
primeNo(360)
