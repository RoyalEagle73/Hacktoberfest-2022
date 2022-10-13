a=[3,4,5]
res=0
for i in range(0,len(a)):
    for j in range(i,len(a)):
        for k in range(i,j+1):
            res=res^a[k];
print(res)
