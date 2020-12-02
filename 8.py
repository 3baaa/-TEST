'''
class Person:
  def greeting(self):
    print('Hello')

james = Person()
james.greeting()

class Person:
  def __init__(self):
    self.hello = '안녕하세요'
  
  def greeting(self):
    print(self.hello)

james = Person()
james.greeting()

class Person:
  def __init__(self,name,age,address):
    self.hello = '안녕하세요'
    self.name = name
    self.age = age
    self.address = address
  
  def greeting(self):
    print('{0} 저는 {1}입니다.'.format(self.hello,self.name))

maria = Person('마리아',20,'서울시 서초구 반포동')
maria.greeting()

print('이름 : ',maria.name)
print('나이 : ',maria.age)
print('주소 : ',maria.address)

class Person:
  def __init__(self,name,age,address,wallet):
    self.hello = '안녕하세요'
    self.name = name
    self.age = age
    self.address = address
    self.__wallet = wallet
  
maria = Person('마리아',20,'서울시',10000)
maria.__wallet -= 10000

class Person:
  def __init__(self,name,age,address,wallet):
    self.hello = '안녕하세요'
    self.name = name
    self.age = age
    self.address = address
    self.__wallet = wallet
  
  def pay(self,amount):
    if amount > self.__wallet:
      print('x')
      return
    self.__wallet -= amount
    print('이제 {0}원 남았네요.'.format(self.__wallet))
    
maria = Person('마리아',20,'서울시',10000)
maria.pay(3000)

class Person:
  def __greeting(self):
    print('Hello')
  
  def hello(self):
    self.__greeting()

james = Person()
#james.__greeting()

class Knight:
  def __init__(self,health,mana,armor):
    self.health=health
    self.mana=mana
    self.armor=armor

  def slash(self):
    print('베기')

x = Knight(health=542.4, mana=210.3, armor=38)
print(x.health, x.mana, x.armor)
x.slash()

class Person:
  bag = []

  def put_bag(self,stuff):
    Person.bag.append(stuff)

james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)
print(Person.bag)

class Person:
  def __init__(self):
    self.bag = []
    
  def put_bag(self,stuff):
    self.bag.append(stuff)
  
james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)

class Knight:
  __item_limit = 10

  def print_item_limit(self):
    print(Knight.__item_limit)

x = Knight()
x.print_item_limit()

#print(Knight.__item_limit)

class Calc:
  @staticmethod
  def add(a,b):
    print(a+b)
  
  @staticmethod
  def mul(a,b):
    print(a*b)

Calc.add(10,20)
Calc.mul(10,20)

class Person:
  count = 0

  def __init__(self):
    Person.count += 1
  
  @classmethod
  def print_count(cls):
    print('{0}명 생성되었습니다.'.format(cls.count))
  

james = Person()
maria = Person()

Person.print_count()

class Date:
  @staticmethod
  def is_date_valid(s):
    a=s.split('-')
    month=int(a[1])
    day=int(a[2])
    if 0<month<13 and 0<day<32:
      return True
    else:
      return False

if Date.is_date_valid('2000-10-31'):
    print('올바른 날짜 형식입니다.')
else:
    print('잘못된 날짜 형식입니다.')

class Date:
  @staticmethod
  def is_date_valid(s):
    year,month,day=map(int,s.split('-'))
    return month<=12 and day <= 31
if Date.is_date_valid('2000-10-31'):
    print('올바른 날짜 형식입니다.')
else:
    print('잘못된 날짜 형식입니다.')

class Person:
  def greeting(self):
    print('안녕하세요.')

class Student(Person):
  def study(self):
    print('공부하기')

james = Student()
james.greeting()
james.study()

class Person:
  def __init__(self):
    print('Person __init__')
    self.hello = '안녕하세요.'
    
class Student(Person):
  def __init__(self):
    print('Student __init__')
    super().__init__()
    self.school = '파이썬 테스트'

james = Student()
print(james.school)
print(james.hello)
'''