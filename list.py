# A list is a collection which is ordered and changeable. Allows duplicate members.
# Create list
Numbers = [1, 2, 3, 4, 5]
Fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']
# use a constructor
# numbers2 = list((1, 2, 3, 4, 5))
# get a value
print (Fruits[1])
# get length
print (len(Fruits))
# append to list
Fruits.append ('Mangos')
# remove from list
Fruits.remove ('Grapes')
# insert into position
Fruits.insert (2, 'Strawberries')
#change value
Fruits[0] = 'Blueberries'
#remove with pop
Fruits.pop(2)
# reverse list
Fruits.reverse()
# sort list
Fruits.sort()
# reverse sort
Fruits.sort(reverse=True)
print (Fruits)