'''
class Person:
  def __init__(self):
    print('Person __init__')
    self.hello = '안녕하세요.'

class Student(Person):
  pass

james = Student()
print(james.hello)

class Person:
  def greeting(self):
    print('안녕하세요.')

class Student(Person):
  def greeting(self):
    print('안녕하세요. 파이썬')

james = Student()
james.greeting()

class Person:
  def greeting(self):
    print('안녕하세요.')

class Student(Person):
  def greeting(self):
    super().greeting()
    print(' 파이썬')

james = Student()
james.greeting()

class Person:
  def greeting(self):
    print('안녕하세요.')

class University:
  def manage_credit(self):
    print('학점 관리')

class Undergraduate(Person,University):
  def study(self):
    print('공부하기')

james = Undergraduate()
james.greeting()
james.manage_credit()
james.study()

class A:
  def greeting(self):
    print('안녕하세요. A입니다.')

class B(A):
  def greeting(self):
    print('안녕하세요. B입니다.')

class C(A):
  def greeting(self):
    print('안녕하세요. C입니다.')

class D(B,C):
  pass

x = D()
x.greeting()

from abc import *

class StudentBase(metaclass=ABCMeta):
  @abstractmethod
  def study(self):
    pass
  
  @abstractmethod
  def go_to_school(self):
    pass

class Student(StudentBase):
  def study(self):
    print('공부하기')

  
  def go_to_school(self):
    print('학교가기')
james = Student()
james.study()
james.go_to_school()

class AdvancedList(list):
  def replace(self,b,c):
    for i,v in enumerate(self):
      if v==b:
        self[i]=c

x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x)

class AdvancedList(list):
  def replace(self,old,new):
    while old in self:
      self[self.index(old)] = new

x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x)

import math

class Point2D:
  def __init__(self,x,y):
    self.x=x
    self.y=y

p1 = Point2D(x=30,y=20)
p2 = Point2D(x=60,y=50)

print('p1: {} {}'.format(p1.x,p1.y))
print('p2: {} {}'.format(p2.x,p2.y))

a = p2.x - p1.x
b = p2.y - p1.y

#c = math.sqrt((a*a) + (b*b))
c = math.sqrt(math.pow(a,2) + math.pow(b,2))
print(c)

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
 
rect = Rectangle(x1=20, y1=20, x2=40, y2=30)

a=rect.x2-rect.x1
b=rect.y2-rect.y1
area=a*b

print(area)

def ten_div(x):
  return 10/x

print(ten_div(0))

try:
  x = int(input('나눌 숫자를 입력하세요:'))
  y = 10 / x
  print(y)
except:
  print('예외가 발생했습니다.')

y=[10,20,30]

try:
  index,x=map(int,input('인덱스와 나눌 숫자를 입력하세요: ').split())
  print(y[index]/x)
except Exception as e:
  print('예외가 발생했습니다.',e)
except ZeroDivisionError as e:
  print('숫자를 0으로 나눌 수 없습니다.',e)
except IndexError as e:
  print('잘못된 인덱스입니다.',e)

try:
  x = int(input('나눌 숫자를 입력하세요: '))
  y = 10/x
except ZeroDivisionError:
  print('숫자를 0으로 나눌 수 없습니다.')
else:
  print(y)
finally:
  print('코드 실행이 끝났습니다.')

try:
  x = int(input('3의 배수를 입력하세요: '))
  if x%3 !=0:
    raise Exception('3의 배수가 아닙니다.')
  print(x)
except Exception as e:
  print('예외가 발생했습니다.',e)

def three_multiple():
  x = int(input('3의 배수를 입력하세요: '))
  if x % 3 != 0:
    raise Exception('3의 배수가 아닙니다.')
  print(x)

try:
  three_multiple()
except Exception as e:
  print('예외가 발생했습니다.',e)

def three_multiple():
  try:
    x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0:
      raise Exception('3의 배수가 아닙니다.')
    print(x)
  except Exception as e:
    print('three_multiple 함수에서 예외가 발생했습니다.',e)
    raise

try:
  three_multiple()
except Exception as e:
  print('스크립트 파일에서 예외가 발생했습니다.',e)

def three_multiple():
  try:
    x = int(input('3의 배수를 입력하세요: '))
    assert x % 3 == 0, '3의 배수가 아닙니다.'
    print(x)
  except Exception as e:
    print('three_multiple 함수에서 예외가 발생했습니다.',e)
    raise

try:
  three_multiple()
except Exception as e:
  print('스크립트 파일에서 예외가 발생했습니다.',e)

class NotThreeMultipleError(Exception):
  def __init__(self):
    super().__init__('3의 배수가 아닙니다.')

def three_multiple():
  try:
    x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0:
      raise NotThreeMultipleError
  except Exception as e:
    print('예외가 발생했습니다.',e)

three_multiple()

try:
  file = open('maria.txt','r')
except FileNotFoundError:
  print('파일이 없습니다.')
else:
  s=file.read()
  file.close()

a='level'
b='hello'

def z(s):
  try:
    if len(s)<2:
      return True
    assert s[0]==s[-1]
    return z(s[1:-1])
  except Exception:
    print('no')

print(z(a))
'''

