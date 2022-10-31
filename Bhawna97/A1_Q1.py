def replace_cube(L, N):
    if(int(N)>len(L)):
        print('Index multile of ',N,' does not exist')
    else:
        for i in range(len(L)):
            if((i+1)%int(N) == 0):
                L[i] = int(L[i])**3
    return L

input_query = 'Y'

while input_query == 'Y' or input_query == 'y':
    input_list = input('Enter elements of a list separated by space ')
    print("\n")
    user_list = input_list.split()
    
    input_number = input('Enter Number ')
    
    print('list: ', replace_cube(user_list, input_number),"\n")
    
    input_query = input('Enter Y if want to continue else enter N ')
