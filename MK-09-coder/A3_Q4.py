a=10
for i in range(a+1):
    flag=False
    if(i!=1 and i!=0):
        for count in range(2,i):
            if(i%count==0):
                flag=True
                break
        if(flag==False):
            print(i)
        
