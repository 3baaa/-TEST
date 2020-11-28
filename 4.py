'''
a = [38,21,53,62,19]
smallest = a[0]
for i in a:
  if i < smallest:
    smallest = i;
print(smallest)

a.sort()
print(a[0])
a.sort(reverse=True)
print(a[0])
print(min(a))
print(max(a))

a = [10,10,10,10,10]
x = 0
for i in a:
  x+=i
print(x)
print(sum(a))

a = [i for i in range(10)]
print(a)
b = list(i for i in range(10))
print(b)
c = [i+5 for i in range(10)]
print(c)
d = [i*2 for i in range(10)]
print(d)

a = [i for i in range(10) if i%2 ==0]
print(a)
b = [i+5 for i in range(10) if i%2==1]
print(b)

a = [i*j for j in range(2,10) for i in range(1,10)]
print(a)

a = [1.2,2.5,3.7,4.6]
#for i in range(len(a)):
#  a[i] = int(a[i])
#print(a)
a = list(map(int,a))
print(a)

a = map(int,input().split())
print(list(a))

a = (38,21,53,62,19,53)
print(a.index(53))
print(a.count(20))
for i in a:
  print(i,end=' ')

a = tuple(i for i in range(10) if i%2==0)
print(a)

a = (1.2,2.5,3.7,4.6)
a = tuple(map(int,a))
print(a)

a=(38,21,53,62,19)
print(min(a))
print(max(a))
print(sum(a))

a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b = [i for i in a if len(i)==5]
print(b)

a = [ i**2 for i in range(10)]
print(a)

a = [[10,20],[30,40],[50,60]]
for x,y in a:
  print(x,y)

a = [[0]*2 for i in range(3)]
print(a)

a = [[0]*i for i in [3,1,3,2,5]]
print(a)

students = [
    ['john', 'C', 19],
    ['maria', 'A', 25],
    ['andrew', 'B', 7]
]
print(sorted(students,key=lambda student: student[1]))

a = [[[0]*3]*4]*2
print(a)

print('Hello, world!'.replace('world','python'))

s = 'Hello, world!'
s = s.replace('world!','Python')
print(s)

table = str.maketrans('abc','123')
print('abczzz'.translate(table))

print('a b c d e'.split())

print('a,b,c,d,e'.split(','))

print(' '.join(['a','b','c']))
print('-'.join(['a','b','c']))

print('python'.upper())
print('PYTHON'.lower())
print('     Python    '.lstrip())
print('     Python    '.rstrip())
print('     Python    '.strip())

print(', python.'.lstrip(',.'))
print(', python.'.rstrip(',.'))
print(', pyhton.'.strip(',.'))

print('python'.ljust(10))
print('python'.rjust(10))
print('python'.center(10))

print('python'.rjust(10).upper())

print('35'.zfill(4))
print('3.5'.zfill(6))
print('hello'.zfill(10))

print('abc abc'.find('bc')
print('abc abc'.find('z'))

print('abc abc'.rfind('bc'))
print('abc abc'.rfind('x'))

print('abc abc'.index('bc'))
print('abc abc'.rindex('bc'))

print('abc abc'.count('bc'))

name='a'
print('i am %s.'%name)
print('i am %d year old.'%20)

print('%10s'%'python')
print('%-10s'%'python')

print('Today is %d %s.'%(3,'April'))

print('Hello, {0}'.format('world!'))
print('Hello, {0}'.format(100))

print('Hello, {0}'.format('world!'))
print('Hello, {0} {2} {1}'.format('python','script',3.6))

print('{0} {0} {1} {1}'.format('Python','Script'))

print('Hello, {} {} {}'.format('Python','Script',3.6))

print('Hello,{language} {version}'.format(language='Python',version=3.6))

language = 'Python'
version = 3.6
print(f'Hello, {language} {version}')

print('{0:<10}'.format('python'))
print('{0:>10}'.format('python'))
print('{:>10}'.format('python'))

print('%03d'%1)
print('{0:03}'.format(35))
print('{0:0<10}'.format(15))
print('{0:0>10}'.format(15))

path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
filename=path[path.rfind('\\')+1:]
print(filename)
a=r'C:\a'
print(a)
'''
