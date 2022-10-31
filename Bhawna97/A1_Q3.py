def flatten(input_list):
    flat_list = [num for sublist in input_list for num in sublist]
    print('flat_list:', flat_list)
    flat_list.sort()
    return flat_list

input_list = [[1], [4, 5], [2, 3, 6, 7]]

print('flat_sorted_list:', flatten(input_list))
