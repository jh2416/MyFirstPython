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

#2.11 Return Recap
my_name = "nico"
my_age = 12
my_color_eyes = "brown"
#위 3개를 한꺼번에 string으로 만들고 싶어
#f : format
print(f"Hello I'm {my_name}, I am {my_age} years old, and {my_color_eyes} is my eye color.")

#juicemaker
def make_juice(fruit):
  return f"{fruit} + 🥤"
  #return 이후의 코드는 실행하지 않음
  print("blablablablablabla")

def add_ice(juice):
  return f"{juice} + 🧊"

def add_sugar(iced_juice):
  return f"{iced_juice} + 🍬"

juice = make_juice("🍎")
#print(juice)
cold_juice = add_ice(juice)
#print(cold_juice)
perfect_juice = add_sugar(cold_juice)


print(perfect_juice)

#3.0 If
#function처럼 indentation, :
#기본 틀
#if condition:
#  "write the code to run"

#변수- =, 등호- ==, 부등호- <=, >=
a = 5

if a == 5:
  print("True!")

b = "nico"
if b == "nico":
  print("True!")


#3.1 Else & Elif
password_correct =False 

if password_correct:
  print("Here is yout money")
else:
  print("Incorrect password!")

winner = 10

if winner >10:
  print("Winner is greater than 10")
elif winner <10:
  print("Winner is less than 10")
else:
  print("Winner is 10")


#3.2 Recap
password_correct =False

winner = 100

if winner <= 10:#if만 쓰는것도 가능
  print("If")
elif winner <= 25: #또 다른 조건도 확인가능
  print("Elif")
elif winner == 0:
  print("Elif2")
elif winner == 50: #위에서 true가 나오면 그 밑은 무시
  print("Elif3")
else: #위 코드에 대한 대안
  print("Else")


#3.3 And & Or
age = int(input("How old are you?"))

print(type(age)) #age의 자료형이 무엇인지 출력
print(age)

if age < 18:
  print("You can't drink.")
elif age>=18 and age <35:
  print("You drink beer! ")
elif age == 60 or age == 70:
  print("Birthday party!")
else: 
  print("Go ahead!")


#and
True and True == True
False and True == False
True and False == False
False and False == False

#or 
True or True == True
True or False == True
False or True == True
False or False == False


#3.4 Python Standard Library
#Python Casino
from random import randint  #'randint' func from 'random' module
#import random만 하고 밑에서 pc_choice = random.randint(1,50) 로 쓰는것도 가능
user_choice = int(input("Choose number."))
pc_choice = randint(1,50)


if user_choice == pc_choice:
  print("You won!")
elif user_choice > pc_choice:
  print("Lower! PC chose ", pc_choice)
elif user_choice < pc_choice:
  print("Higher! PC chose ", pc_choice)


"""블로그에 추가
한줄 주석문 : #
덩어리 주석문 : """ """
"""

#3.5 While

#if문은 한번만 실행
if True:
  print("Hi im True")

#while은 if와 같지만 멈추지 않음, 멈추려면 False가 돼야함
"""while True:
  print("Hi im True")"""

distance = 0

while distance < 20:
  print("I'm running:", distance, "km")
  distance = distance + 1


#3.6 Python Casino
from random import randint  

print("Welcome to Python Casino!")
pc_choice = randint(1,50)

playing = True

while playing:
  user_choice = int(input("Choose number: "))
  if user_choice == pc_choice:
    print("You won!")
    playing = False
  elif user_choice > pc_choice:
    print("Lower!")
  elif user_choice < pc_choice:
    print("Higher!")

#3.7 Recap
#built-in function : int, input, print같은 언제든 쓸 수 있는 함수


#4.0 Methods
#data structure
mon = "Mon"
tue = "Tue"
wed = "Wed"
thur = "Thur"
fri = "Fri"
#...얘네들은 list가 아님, list는 한개의 variable에 모두 저장되어야 함

#days_of_week = "Mon,Tue,Wed,Thur,Fri"
#print(days_of_week)
#이렇게 하면 list가 되긴 하지만 특정 요일을 고르는 기능을 실행할 수 없음
days_of_week = ["Mon","Tue","Wed","Thur","Fri"]
print(days_of_week)

#Method설명
# .뒤에 오는 것(function)들은 name이라는 variable에 결합(bounded)되어있음, string, number같은 것들에 bounded된 function들을 method라고 함:쉽게 말하면 데이터 뒤에 결합/연결된 function, 데이터를 변환시켜줄 수 있음
# print같이 혼자 아무데서나 아무렇게 쓸 수 있는 것들은 unbounded function
name = "nico"
print(name.upper()) #대문자(uppercase)로 변환
print(name.capitalize()) #맨 앞만 대문자로
print(name.startswith("n")) #n으로 시작하는지 확인
print(name.replace("o","🍔"))
#공식문서에서 다양한 method 확인 가능


#4.1 Lists
#Data Modifying이 용이해짐, Method사용이 가능해져서 생산적임, Data structures로 작업을 하기 용이
#하나의 list에 숫자, 문자, boolean, list모두 섞어서 사용할 수 있음
#뒤에서부터 접근도 가능함 : 가장 마지막 item부터 -1, -2, -3, ......
whatever = [1,2,3,True,False,"hi","hello",[0,1,2,[True,False]]]
days_of_week = ["Mon","Tue","Wed","Thur","Fri"]

print(days_of_week.count("Wed"))

days_of_week.append("Sat")
days_of_week.append("Sun")
print(days_of_week)

#특정 item접근(0부터 시작)
print(days_of_week[0])

days_of_week.remove("Wed")

days_of_week.reverse()  #순서 뒤집어서 출력
print(days_of_week)

print(days_of_week.clear()) #None출력, print 하기전에 실행 후 print 하면 []출력

days_of_week.reverse()  #[]출력, 함수 내에서 실행된 clear도 후에 영향을 계속 줌
print(days_of_week)


#4.2 Tuples
#Lists
days_list = ["Mon","Tue","Wed"]
#Tuples - 차이점 : 불변(immutable)!, method중 count, index만 사용가능, 만들어진 이후 변경 불가
#접근은 list와 같은 방식으로([]) 가능
days = ("Mon","Tue","Wed")
print(days[-2])


#4.3 Dicts
#key value fair
player = {
  'name': 'nico',  #string key-value
  'age': 12,       #int key-value
  'alive': True,   #boolean key-value
  'fav_food': ['🍕', '🍔']
}
print(player.get('name'))  #key로 접근
print(player.get('fav_food'))
#dictionary는 많은 속성을 가진 데이터를 만들때 사용
print(player['fav_food'])

print(player)   
player.pop('age')  #key가 age인 데이터를 지움
print(player)

#데이터 추가
player['xp'] = 1500 #key - xp, value - 1500
print(player)
player['fav_food'].append("🍜") #dict안의 list에 항목 추가
print(player.get('fav_food'))
print(player['fav_food'])


#4.4 Recap
print("nico".endswith("a"))

numbers = [5,2,1,3,4,6,8,"True",True,12]
numbers.append(["🍔","🍟"])
numbers.append("🍕")

print(numbers[-1])

nums = (1,2,3,4,5,True,"xxxxx")
print(nums[4])

player = {
  'name':'nico',
  'age':12,
  "alive":True,
  "fav_food":("🍔","🍟"),
  'friend':{
    'name':'lynn',
    'fav_food':["🍮"]
  }
}

print(player["friend"]["fav_food"])
print(player["fav_food"][1])
print(player["fav_food"][-2])

player['fav_food']='🍅'
player.pop('alive')
player['friend']['fav_food'].append('🍌')
print(player)


#4.5 For Loops
websites = (  #tuple, list여도 밑에 for문 가능
  "google.com",
  "airbnb.com",
  "twitter.com",
  "facebook.com",
  "tiktok.com"
)

for potato in websites: #보통 for website in websites 같은 식으로 사용하면 표현하기 쉬움
  print("hello")  
  #각각의 웹사이트에 대해 print실행
  #현재 처리중인 item이 뭔지 알 수 없음
  print("potato is equals to", potato)


#4.6 URL Formatting
websites = (  
  "google.com",
  "airbnb.com",
  "https://twitter.com",
  "facebook.com",
  "https://tiktok.com"
)

for website in websites: 
  # if website.startswith("https://"):
  #   print("good to go")
  # else:
  #   print("we have to fix it")
  if not website.startswith("https://"):
    print("we have to fix it")
    # 위랑 같은 코드
    # if website.startswith("https://") == False:
    #   print("we have to fix it")
    website = f"https://{website}" #string 추가
  print(website) # print all website
  

#4.7 Requests
# pypi.org : standard library말고 다른 사람들이 만든 library쓰고싶을 때, request도 여기에 있음
#request : 내 브라우저가 google 서버에 request를 보내고 google서버는 나한테 웹사이트를 보내줌
# 컴퓨터에 설치하려면 $ python -m pip install requests
# replit에서 설치할때는 package배너에서 검색

from requests import get #get website

websites = (  
  "google.com",
  "airbnb.com",
  "https://twitter.com",
  "facebook.com",
  "https://tiktok.com"
)

for website in websites: 
  if not website.startswith("https://"):
    website = f"https://{website}" 
  print(website) 


#4.8 Status Codes
#get : response를 return
#response : 웹사이트의 응답
from requests import get #get website

websites = (  
  "google.com",
  "airbnb.com",
  "https://twitter.com",
  "facebook.com",
  "https://tiktok.com"
)

results = {}

for website in websites: 
  if not website.startswith("https://"):
    website = f"https://{website}" 
  response = get(website)
  #print(response) 
  # <Response [200]> 5줄 출력됨 -> 웹사이트가 성공적으로 응답했다는 의미; 
  #200 : OK 리소스를 불러와서 메시지 바디에 전송되었습니다.
  print(response.status_code)
  if response.status_code == 200:
    results[website] = "OK" #위에 dict에 key생성
    print(f"{website} is OK")
  else:
    print(f"{website} is not OK")
    results[website] = "FAILED" #위에 dict에 key생성

print(results)



