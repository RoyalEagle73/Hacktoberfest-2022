actual_labels = ['Dog','Dog','Cat','Cat','Cat']
predicted_labels = ['Cat','Dog','Cat','Dog','Cat']
def calc_acc(actual_labels,predicted_labels):
    res = 0
    l = len(actual_labels)
    for i in range(l):
        if actual_labels[i] == predicted_labels[i]:
            res +=1
    
    print(res/l*100)
calc_acc(actual_labels,predicted_labels)   