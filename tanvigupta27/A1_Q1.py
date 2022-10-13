input = [1,2,3,4,5,6,7,8,9,10]
n = 2

# Approach 1
def  replace_cube(input, n):
    for i in range(0,len(input),n):
        input[i-1] = input[i-1]*input[i-1]*input[i-1]
    print(input)
replace_cube(input, n)

# Approach 2
input = [1,2,3,4,5,6,7,8,9,10]
n = 2
def replace_list(input,n):
    ans = [input[i]**3 if i%n!=0 else input[i] for i in range(len(input))]
    print(ans)
replace_list(input,n)
