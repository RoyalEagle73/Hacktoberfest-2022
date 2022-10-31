def check_equal(str1, str2):
    str2 = list(str2)
    for elem in str1:
        str2.remove(elem)
    if len(str2) == 0:
        print("Same")
    else:
        print("Not Same")

str1 = 'abcde'
str2 = 'bcdea'
check_equal(str1,str2)
