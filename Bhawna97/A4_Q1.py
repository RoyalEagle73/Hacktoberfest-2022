def next_smallest_palindrome(A):
    N = int(A)
    if(N>0 and N<9):
        print(N+1)
    elif(N>0 and N>=9):
        N+=1
        while(N):
            if(str(N) == str(N)[::-1]):
                print(N)
                break
            N+=1

next_smallest_palindrome("23545")
next_smallest_palindrome("999")
next_smallest_palindrome('8')
