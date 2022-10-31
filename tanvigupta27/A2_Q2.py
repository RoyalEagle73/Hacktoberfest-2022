input = [['Arun',25,3,7],['Nihal',50,5,12],['Sanjay',10,4,3]]
dic = {}
for i in range(len(input)):
    #  if input[i][0] in dic.keys():
    #      dic[input[i][0]].append(input[i][1:])
    #  else:
    dic[input[i][0]]= [] # create empty list
    dic[input[i][0]].append(input[i][1:]) 
print(dic)

for i in input:
    strike_rate = i[1]/i[3]
    if strike_rate >4 and i[2]>2:
        print( i[0])
    elif strike_rate >2 and strike_rate<4 and i[2]>4:
        print(i[0])