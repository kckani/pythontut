# A dictionary is a collection which is unordered, changeable and indexed. no duplicate members.
# create dict
person = {'first_name': 'john', 'last_name': 'doe', 'age': 30}
# use constructor
# person2 = dict(first_name = 'sara', last_name = 'williams')
# get value
print (person['first_name'])
print (person.get('last_name'))
# add key/value
person['phone'] = '555-555-555'
# get dict keys
print (person.keys())
# get dict items
print (person.items())
# copy dict
person2 = person.copy()
person2 ['city'] = 'boston'
# remove item
del (person['age'])
person.pop('phone')
# clear
person.clear()
# get length
print (len(person2))
# list of dict
people = [{'name': 'martha', 'age': 30,}, {'name': 'kevin', 'age': 25}]
print(people[1]['name'])
