T = int(input("Enter T:"))

def sort_array(n1,n2,A1,A2):
    i = 0
    j = 0
    k = 0
    result = []
    while(i<n1 and j<n2):
        if(A1[i]<A2[j]):
            result.append(A1[i])
            i += 1
        else:
            result.append(A2[j])
            j += 1
    while(i<n1):
        result.append(A1[i])
        i += 1
    while(j<n2):
        result.append(A2[j])
        j += 1
    print("Sorted Array: ",result)
    
    return
if(T >= 1 and T <= 10):
    for n in range(T):
        n1 = int(input("length of Array 1:"))
        A1 = list(map(int,input("\nEnter the numbers : ").split()))[:n1]
        n2 = int(input("length of Array 2:"))
        A2 = list(map(int,input("\nEnter the numbers : ").split()))[:n2]
        sort_array(n1,n2,A1,A2)
