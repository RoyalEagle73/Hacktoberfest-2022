def flatten_list(nums):
    result = []
    for i in nums:
        result.extend(i) if isinstance(i, list) else result.append(i)
    result.sort()
    return result     
n_list = [10,[40,20],30,50]

print(flatten_list(n_list))

def flatten_list_updt(L):
    new_ = []
    for i in L:
        if type(i) is type(L):
            #new_.extend(i)
            for j in i:
                new_.append(j)
        else:
            new_.append(i)
    new_.sort()
    print(new_)
    return
L = [10,[40,20],30,50]
flatten_list_updt(L)

