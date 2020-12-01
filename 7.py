'''
def personal_info(name,age,address):
  print('이름: ',name)
  print('나이: ',age)
  print('주소: ',address)

personal_info(age=30,address='서울시 용산구 이촌동',name='홍길동')

def personal_info(name,age,address):
  print('이름: ',name)
  print('나이: ',age)
  print('주소: ',address)

x = {'name':'홍길동','age':30,'address':'서울시 용산구 이촌동'}
personal_info(**x)

def personal_info(**kwargs):
  print('kwrgs123 = ',kwargs)
  for kw,age in kwargs.items():
    print(kw,' : ',age,sep='')

x = { 'name' : '홍길동'}
personal_info(**x)
print()
personal_info(age=30,address='서울시 용산구 이촌동',name='홍길동')
print()
y = {'name':'홍길동','age':30,'address':'서울 용산구 이촌동'}
personal_info(**y)

def personal_info(name,age,address='비공개'):
  print('이름 : ',name)
  print('나이 : ',age)
  print('주소 : ',address)

personal_info('홍길동',30)
personal_info('홍길동',30,'서울시용산구 이촌동')

korean, english, mathematics, science = 100, 86, 81, 91
def get_max_score(*args):
  return max(args)

max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수:', max_score)
 
max_score = get_max_score(english, science)
print('높은 점수:', max_score)

def hello(count):
  if count == 0 :
    return

  print('Hello, world!',count)
  count -= 1
  hello(count)

hello(5)

def factorial(n):
  if n==1:
    return 1
  return n*factorial(n-1)

print(factorial(5))

def is_palindrome(word):
  a=is_palindrome(word[len(word)-1:])
  b=is_palindrome(:word[:len(word)-1])
  if len(a) and len(b) == 1:
    return
  elif a!=b:
    return False

  return True

print(is_palindrome('hello'))
print(is_palindrome('level'))

def is_palindrome(word):
  print('word = ',word)
  if len(word) < 2:
    return True
  if word[0] != word[-1]:
    return False
  return is_palindrome(word[1:-1])

print(is_palindrome('hello'))
print(is_palindrome('level'))

plus_ten = lambda x : x + 10
print(plus_ten(1))

y = 10
print((lambda x: x+y)(1))

a = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x: str(x) if x%3==0 else x,a)))

a = [1,2,3,4,5]
b = [2,4,6,8,10]
print(list(map(lambda x,y:x*y,a,b)))

def f(x):
  return x>5 and x<10

a = [8,3,2,10,15,7,1,9,0,11]
print(list(filter(f,a)))

a = [8,3,2,10,15,7,1,9,0,11]
print(list(filter(lambda x:x>5 and x<10,a)))

a = [8,3,2,10,15,7,1,9,11]
print([i for i in a if i>5 and i<10])

files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']

#print(list(map(lambda files: files if files.find('.png') or files.find('.jpg') else,files)))
print(list(filter(lambda x:x.find('.jpg')!=-1 or x.find('.png')!=-1, files)))

x = 10
def a():
  x = 20
  print(x)
a()
print(x)

x = 10
def a():
  global x
  x = 20
  print(x)
a()
print(x)

def a():
  global x
  x = 20
  print(x)
a()
print(x)

def print_h():
  hello = 'Hello, world!'
  def print_m():
    print(hello)
  print_m()

print_h()

def A():
  x = 10
  def B():
    x = 20
  
  B()
  print(x)

A()

def A():
  x = 10
  def B():
    nonlocal x
    x = 20
  B()
  print(x)

A()

def A():
  x = 10
  y = 100
  def B():
    x = 20
    def C():
      nonlocal x
      nonlocal y
      x = x+30
      y = y+300
      print(x)
      print(y)
    C()
  B()
A()

x=1
def A():
  x=10
  def B():
    x=20
    def C():
      global x
      x=x+30
      print(x)
    C()
  B()
A()

def calc():
  a=3
  b=5
  def mul_add(x):
    return a*x+b
  return mul_add

c = calc()
print(c(1),c(2),c(3),c(4),c(5))

def calc():
  a=3
  b=5
  return lambda x:a*x+b

c = calc()
print(c(1),c(2),c(3),c(4),c(5))

def calc():
  a=3
  b=5
  total=0
  def mul_add(x):
    nonlocal total
    total = total + a*x+b
    print(total)
  return mul_add
c = calc()
c(1)
c(2)
c(3)

def counter():
  i=0
  def count():
    nonlocal i
    i=i+1
    return i
  return count

c = counter()
for i in range(10):
  print(c(),end=' ')
'''