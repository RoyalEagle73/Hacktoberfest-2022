def calc_acc(actual_labels,predicted_labels):
    correctly_predicted = 0
    total = len(actual_labels)
    for i in range(total):
        if actual_labels[i] == predicted_labels[i]:
            correctly_predicted +=1
    accuracy_score = correctly_predicted/total*100
    return round(accuracy_score)
    
actual_labels = ['Dog','Dog','Cat','Cat','Cat']
predicted_labels = ['Cat','Dog','Cat','Dog','Cat']

print('The Accuracy score is', calc_acc(actual_labels,predicted_labels))
