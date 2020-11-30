'''
a = {1,2,3,4}
a.add(5)
print(a)
a.remove(3)
print(a)
a.discard(2)
print(a)
a.discard(3)
print(a)

a = {1,2,3,4}
print(a.pop())
print(a)
a.clear()
print(a)

a = {1,2,3,4}
print(len(a))

a = {1,2,3,4}
for i in a:
  print(i)

a = {i*3 for i in range(1,100) if i*3<101}
b = {i*5 for i in range(1,100) if i*5<101}

print(a&b)

a = {i for i in range(1,101) if i%3==0}
b = {i for i in range(1,101) if i%5==0}

print(a&b)

print(dict.fromkeys(['a','b','c','d']).keys())

file = open('hello.txt','w')
file.write('Hello, world!')
file.close()

file = open('hello.txt','r')
s = file.read()
print(s)
file.close()

with open('hello.txt','r') as file:
  s = file.read()
  print(s)

with open('hello.txt','w') as file:
  for i in range(3):
    file.write('Hello, world! {0}\n'.format(i))

lines = ['안녕하세요.\n','파이썬\n','테스트입니다.\n']

with open('hello.txt','w') as file:
  file.writelines(lines)

with open('hello.txt','r') as file:
  lines = file.readlines()
  print(lines)

with open('hello.txt','r') as file:
  line = None
  while line != '':
    line = file.readline()
    print(line.strip('\n'))

with open('hello.txt','r') as file:
  for line in file:
    print(line.strip('\n'))

with open('words.txt','r') as file:
  count = 0
  for line in file:
    if len(line.strip('\n'))<=10:
      count+=1
  print(count)

word = input('단어를 입력하세요:')

is_p=True
for i in range(len(word)//2):
  if word[i] != word[-1-i]:
    is_p=False
    break

print(is_p)

text = 'Hello'

for i in range(len(text) - 1):
  print(text[i],text[i+1],sep='')

text = 'this is python script'
words = text.split()

for i in range(len(words) - 1 ):
  print(words[i],words[i+1])

text = 'this is python script'
words = text.split()
print(list(zip(words,words[1:],words[2:])))

n = int(input())
text = input()
words = text.split()

if n>len(words):
  print('wrong')
else:
  n_gram = [ (words[i],words[i+1],words[i+2],words[i+3],words[i+4],words[i+5],words[i+6]) for i in range(4) ]
  for i in n_gram:
    print(i)

def hello():
  print('Hello, world!')
hello()

def add(a,b):
  print(a+b)
add(10,20)

def add(a,b):
  return a+b
x = add(10,20)
print(x)

def not_ten(a):
  if a==10:
    return
  print(a,'입니다.',sep='')
not_ten(5)
not_ten(10)

def add_sub(a,b):
  return a+b,a-b
x,y = add_sub(10,20)
print(x)
print(y)

def mul(a,b):
  c=a*b
  return c
def add(a,b):
  c=a+b
  print(c)
  d=mul(a,b)
  print(d)

x=10
y=20
add(x,y)

x = 10
y = 3
def get_quotient_remainder(x,y):
  return x//y,x%y

quotient, remainder = get_quotient_remainder(x, y)
print('몫: {0}, 나머지: {1}'.format(quotient, remainder))

def print_n(a,b,c):
  print(a)
  print(b)
  print(c)

x=[10,20,30]
print_n(*x)

def print_n(*args):
  for arg in args:
    print(arg)
x=[10]
print_n(*x)
y=[10,20,30,40]
print_n(*y)
print_n(1,2)
print_n(1,2,3,4)
'''