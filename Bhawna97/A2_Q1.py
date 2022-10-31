import math as m

def compute_dist(lis,pnt):
    sorted_nearest = []
    nearest_five = []
    for i in range(len(lis)):
        sorted_nearest.append((i,m.dist(pnt,lis[i])))
    sorted_nearest.sort(key = lambda  x:x[1])
    count = 0
    for i in sorted_nearest:
        if count < 5:
            index = i[0]
            nearest_five.append(lis[index])
        count += 1
    return nearest_five

pnt = [0,0]
n = 6
lis = [[5,5],[1,1],[2,2],[3,3],[4,4],[6,6]]
print(compute_dist(lis,pnt))
