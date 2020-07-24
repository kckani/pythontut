# strings in python are sourounded by either single or double quotation marks. lets lookat string formatting and some sting methods
name="brad"
age=37
# concatenate
print ('hello, my name is ' + name + ' and i am ' + str(age))
#string formatting
#Arguments by position
print ('My name is {name} and i am {age}'.format(name=name,age=age))
# f-string (3.6+)
print (f'hello, my name is {name} and i am {age}')
#string method
s='helloworld'
# Capitalize string
print (s.capitalize())
# make all uppercase
print (s.upper())
# make all lower
print (s.lower())
# swap case
print (s.swapcase())
# get length
print (len(s))
#replace
print (s.replace('world', 'everyone'))
#count
sub = 'h'
print (s.count (sub))
#start with
print (s.startswith ('hello'))
# ends with
print (s.endswith ('d'))
# split into a list
print (s.split())
# find position
print (s.find ('r'))
# is all alphanumeric
print (s.isalnum())
# is all alphabetic
print (s.isalpha())
# is all numeric
print (s.isnumeric())
