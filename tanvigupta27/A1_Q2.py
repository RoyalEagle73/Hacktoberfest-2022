Menu = [['Sweet_Corn_Soup', 300.0], ['Cream_of_Tomato_Soup', 100.0], ['Bacon_and_Cheese', 150.0], ['Honey_Mustard', 230.0], 
        ['Hot_Coffee', 50.0], ['Cold_Coffee', 50.0], ['Egg_Sandwiches', 130.0], ['Tacos', 400.0]]

input = ['Hot_Coffee', 'Cold_Coffee', 'Tacos']
res = []
# for i in input:
for name in Menu:
    if name[0] in input:
        name[1] = name[1] + (name[1]*0.1)
        # name[1] = name[1]*1.1     #1.00000000
        res.append(name)
    else:
        res.append(name)
print (res)


