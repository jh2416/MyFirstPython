a = 2    #각각 메모리로 감 ex.0x0001
b = 3
c = a + b    #변수들로 새로운 변수를 만들 수 있음
c = 1        #위에서 아래로 읽음 -> 1출력
a = 1
b = 10       #c는 안변함
print(c)

my_age = 88

#2.2
Data types
a = 654    #number
print(a)
my_name = "nico"    #text
b = "1231231234"
print(my_name)

#boolean - True/False
#대문자 필수
c = True  #1, ON
d = False #0, OFF

#2.3
my_name = "hoon"
age = 27
dead = False
print("Hello my name is", my_name)
print("and I'm", age, "years old")

#2.4
#function : 코드 조각 같은것, 반복해서 사용가능, print()도 function
print("hello")
print(True)
print(12)
print("hello", True, 12)

name = "nico"
#make function
def say_hello():
  print("hello how r u?")
  #say_hello를 호출할때마다 hello how r u?를 출력해라

say_hello()
say_hello()
say_hello()

#2.5
#indentation : 
#코드가 어떤 것 안에 들어있는 것을 표시할때 2칸의 공백필요(자바 중괄호의 역할)

def say_hello():
  print("hello how r u?")

def say_bye():
  print("bye bye")
  say_hello()

say_hello()

#2.6 Parameters
#다양한 출력을 원함 -> 데이터가 들어갈 공간(placeholder) 제공 필요
def say_hello(user_name):  #user_name : parameter
  print("hello", user_name, "how r u?")

#user_name : parameter
#nico, matt, lynn, lewis : arguments
say_hello("nico")
say_hello("matt")
say_hello("lynn")
say_hello("lewis")


#2.7 Multiple Parameters
def say_hello(user_name, user_age):  
  print("hello", user_name)
  print("you are", user_age, "years old")

#say_hello("nico")    #error! - missing 'user_age' argument
say_hello("nico", 12)

print(1,2,3,4,5,6,7,8,9)


#2.8 Recap
def tax_calculator(money, tax_rate):
  print(money * tax_rate)

print("your tax: ")
tax_calculator(10000000000, 0.1)


#2.9 Default Parameters
# def say_hello(user_name):
#   print("hello", user_name, "\b!")

# say_hello("nico")
# say_hello()  #error!

#익명의 유저에게 hello를 하려면? user_name="anonymous"와 같은 방식으로 작성해주면 됨
def say_hello(user_name="anonymous"):
  print("hello", user_name,"\b!")

say_hello("nico")
say_hello()    #hello anonymous! 출력

#challenge
def plus(a=0, b=0):
  print(a + b)

def minus(a=0, b=0):
  print(a - b)

def multiply(a=0, b=0):
  print(a * b)

def divide(a=0, b=1):
  print(a / b)

def power_of(a=0, b=1):
  print(a**b)

plus(1,2)       #3
minus(3,1)      #2
multiply(4,5)   #20
divide(6,2)     #3
power_of(4,3)   #64


#2.10 Return Values
#출력 + 함수로부터 값 받기
def tax_calculator(money):
  #print(money * 0.35)
  return money * 0.35

#tax_calculator(1500000000)

def pay_tax(tax):
  print("Thank you for paying", tax)

to_pay = tax_calculator(150000000)  #money입력
#tax_calculator에서 세금 얼마인지 받아옴
pay_tax(to_pay)                     #to_pay = tax