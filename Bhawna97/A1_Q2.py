def update_menu(menu, dishes_list, percent):
    updated_menu = []
    for dish in menu:
        if dish[0] in dishes_list:
            dish[1] = dish[1] + (dish[1]*percent/100)
            updated_menu.append(dish)
        else:
            updated_menu.append(dish)
    return updated_menu

menu = [['Sweet_Corn_Soup', 300.0], ['Cream_of_Tomato_Soup', 100.0], ['Bacon_and_Cheese', 150.0],['Honey_Mustard', 230.0],['Hot_Coffee', 50.0], ['Cold_Coffee', 50.0], ['Egg_Sandwiches', 130.0], ['Tacos', 40.0]]

dishes_list = ['Hot_Coffee', 'Cold_Coffee', 'Tacos']

percent = 10

print (update_menu(menu, dishes_list, percent))
