A = "23545"
B = "999"

def next_palindrome(string):
    num = int(string)
    if(num>0 and num<9):
        print(num+1)
    elif(num>0 and num>=9):
        num+=1
        while(num):
            if(str(num) == str(num)[::-1]):
                print(num)
                break
            num += 1
    return

next_palindrome(A)
next_palindrome(B)
next_palindrome('7')
next_palindrome('9')
