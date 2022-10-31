def man_of_the_match(records):
    for i in records:
        strike_rate = i[1]/i[3]
        if strike_rate >4 and i[2]>2:
            return i[0]
        elif strike_rate >2 and strike_rate<4 and i[2]>4:
            return i[0]

records = [['Arun',25,3,7],['Nihal',50,5,12],['Sanjay',10,4,3]]
dic = {}
for i in range(len(records)):
    dic[records[i][0]]= []
    dic[records[i][0]].append(records[i][1:])
    
print(dic,"\n",man_of_the_match(records))
