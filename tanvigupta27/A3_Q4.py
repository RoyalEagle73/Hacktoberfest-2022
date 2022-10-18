def prime_no(N):
    if (N>=1 and N <=300):
        print("N:",N)
        print("Output:")
        for i in range(2,N+1):
            flag = 0
            for j in range(2,i//2):
                if(i%j == 0):
                    flag = 1
                    break
            if(flag == 0) and (i!= 1):
                print(i)
    else:
        print("Exit: N > 300")
    return
# if (N>=1 and N <=300):
prime_no(5)
prime_no(10)
prime_no(350)
