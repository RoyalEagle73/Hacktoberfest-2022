from collections import Counter
str1 = 'abcde'
str2 = 'bcdea'

# Approach 1
def sort_string(str):
    li = list(str1)  
    for i in range(0,len(str1)):
    	for j in range(0,len(str1)):
    		if li[i]<li[j]:
    			li[i],li[j]=li[j],li[i]
    # print(li)
print("Approach: 1")
if sort_string(str1) == sort_string(str2):
    print("Same")
else:
    print("Not Same")

# Approach 2
# Using sorted function
def sort_function(str1, str2):
    if sorted(str1) == sorted(str2):
        print("Same")
    else:
        print("Not Same")
print("Approach: 2")
sort_function(str1, str2)

# Approach 3
# Compare based on number of characters/length
def comapre_length(str1, str2):
    count1 = len(str1)
    count2 = len(str2)
    return count1 == count2
print("Approach: 3")
print(comapre_length("abcde", "bcdea"))

# Approach 4
def compare(str1, str2):
    print("Result:")
    return Counter(str1) == Counter(str2)
print("Approach: 4")
print(compare(str1, str2))

# Approach 5
def compare(str1, str2):
    str2 = list(str2)
    for elem in str1:
        str2.remove(elem)
    if len(str2) == 0:
        print("Same")
    else:
        print("Not Same")
print("Approach: 5")
compare(str1,str2)



