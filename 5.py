'''
x = {'a':10,'b':20,'c':30,'d':40}
#print(x.setdefault('e'))
#rint(x.setdefault('f',100))
#print(x)
x.update(a=90)
print(x)
x.update(e=50)
print(x)
x.update(a=900,f=60)
print(x)

y = {1:'one', 2:'two'}
print(y)
y.update({1:'ONE', 3:'THREE'})
print(y)
y.update([[2,'TWO'],[4,'FOUR']])
print(y)
y.update(zip([1,2],['one','two']))
print(y)

x = {'a':10,'b':20,'c':30,'d':40}
print(x.pop('a'))
print(x)
print(x.pop('z',0))
print(x.popitem())
print(x)
x.clear()
print(x)

x = {'a':10,'b':20,'c':30,'d':40}
#print(x.get('a'))
#print(x.get('z',0))
print(x.items())
print(x.keys())
print(x.values())

keys = ['a','b','c','d']
x = dict.fromkeys(keys,100)
print(x)

x = {'a':10,'b':20,'c':30,'d':40}
print(x.items())
print(x.keys())
print(x.values())
for i in x:
  print(i,end=' ')
for k,v in x.items():
  print(k,v)
for k in x.keys():
  print(k)
for v in x.values():
  print(v,end=' ')

keys = ['a','b','c','d']
x = {key: value for key,value in dict.fromkeys(keys).items()}
print(x)

x = {'a':10,'b':20,'c':30,'d':40}
for k,v in x.items():
  if v == 20:
    del x[k]

print(x)

x = {'a':10,'b':20,'c':30,'d':40}
x = {k:v for k,v in x.items() if v != 20}

maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
average = sum(maria.values())/len(maria)
print(average)

fruits = {'st','gr','or','pi','ch'}
print(fruits)

fruits = {'or','or','ch'}
print(fruits)

fruits = {'st','gr','or','pi','ch'}
print('or' in fruits)
print('or' not in fruits)

b = set(range(5))
print(b)

c = set()
print(c)

a = {1,2,3,4}
b = {3,4,5,6}

print(a | b)
print(set.union(a,b))
print(a & b)
print(set.intersection(a,b))
print(a-b)
print(set.difference(a,b))
print(a^b)
print(set.symmetric_difference(a,b))

a = {1,2,3,4}
a |= {5}
print(a)
a = {1,2,3,4}
a.update({5})
print(a)

a = {1,2,3,4}
a &= {0,1,2,3,4}
print(a)
a = {1,2,3,4}
a.intersection_update({0,1,2,3,4})
print(a)

a = {1,2,3,4}
a -= {3}
print(a)
a = {1,2,3,4}
a.difference_update({3})
print(a)
'''