with open('recipes.txt', encoding = 'utf8')  as file:
    dishes_dict = {}
    for line in file:
        dish_name = line.strip()
        ingr_count = int(file.readline())
        igr = []
        for i in range(ingr_count):
            ingr = file.readline().strip()
            dish, count, unit = ingr.split(' | ')
            igr.append({"ingredient_name": dish, "quantity": count, "measure": unit})

        dishes_dict[dish_name] = igr
        file.readline()



def get_shop_list_by_dishes(dishes, person_count=0):
    d = []
    l = []
    s= []
    for i in dishes_dict.keys():
        for j in dishes:
            if i == j:
                l += dishes_dict[i]
    for id in l:
        for key, value in list(id.items()):
            if key == 'ingredient_name':
                d.append(value)

    for i in l:
        s.append({'measure': i['measure'],'quantity': int(i['quantity'])*person_count})

    zipped = list(zip(d,s))
    last_dict = {}
    next_dict = {}
    for i,j in zipped:
        if i not in last_dict.keys():
            last_dict[i]=j
        else:
            next_dict[i]=j
    for a,b in last_dict.items():
        for c,d in next_dict.items():
            if a == c :
                b['quantity']+=d['quantity']
            
    print(dict(sorted(last_dict.items())))


       
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет','Картошка'], 2)



