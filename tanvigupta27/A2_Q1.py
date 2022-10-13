import math as m
pnt = [0,0]
n = 6
ans = []
lst = [[5,5],[1,1],[2,2],[3,3],[4,4],[6,6]]
print(lst)

def compute_Dist(lst,pnt):
    res = []
    result = []
    for i in range(n):
        res.append((i,m.dist(pnt,lst[i])))
    res.sort(key = lambda  x:x[1])
    count = 0
    for i in res:
        if count < 5:
            index = i[0]
            result.append(lst[index])
            print(lst[index])
        count += 1
    print(result)

compute_Dist(lst,pnt)
