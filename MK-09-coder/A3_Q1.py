a=[1,2,44,3]
max=0
for i in range(len(a)):
    for j in range(i):
        if(a[i]%a[j]>max):
            max=a[i]%a[j];
print(max)
