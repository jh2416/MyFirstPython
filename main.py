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


#4.9 Recap
from requests import get

websites=[
  "google.com",
  "https://httpstat.us/502",
  "https://httpstat.us/404",
  "https://httpstat.us/300",
  "https://httpstat.us/200",
  "https://httpstat.us/101"
]
#https://httpstat.us/xxx is service for generating HTTP codes

results={}

for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  code = get(website).status_code
  if code >= 500:
    results[website] = "5xx / server error"
  elif code >= 400:
    results[website] = "4xx / client error"
  elif code >= 300:
    results[website] = "3xx / redirection "
  elif code >= 200:
    results[website] = "2xx / successful"
  elif code >= 100:
    results[website] = "1xx / informational response"
  
print(results)


#5.2 Installation
#모든 웹사이트가 스크래핑이 가능한건 아님
#데이터 추출해가는 걸 원치 않는 웹사이트들이 있음 ex)코드인증, 봇 방지 프로그램 등으로 막음
#이용약관에 명시하는 웹사이트들도 있음

#5.3 Initial Request
#weworkremotely.com 스크래핑
#url이 제일 중요
from requests import get

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"

#weworkremotely.com에서 python으로 검색한 페이지 접근
response = get(f"{base_url}{search_term}")

if response.status_code != 200:
  print("Can't request website")
#print(response) #확인
else:
  print(response.text) #HTML코드 출력


#5.4 BeautifulSoup
#원하는 text 찾기 - beautifulsoup사용
#find_all : list로 만들어줌
#soup.find_all("title") - title이라는 HTML태그 모두 가져옴, 
#soup.find_all("a", class_="sister") - class가 sister인 링크 가져옴
from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
  print("Can't request website")
else:
  soup = BeautifulSoup(response.text, "html.parser")
  jobs = soup.find_all('section', class_="jobs")
#response.text : html text,
#"html.parser" : beautifulsoup한테 html을 보내준다고 말해주는거


#5.5 Keyword Arguments
def say_hello(name, age):
  print(f"Hello {name}, you are {age} years old.")

say_hello("nico", 12)
say_hello(age=12, name="nico")

#soup.find_all에서 class_를 쓰는 이유: class는 이미 파이썬에서 쓰고있는 Keyword이기 때문에 _를 붙여줌

#5.6 Job Posts
from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
  print("Can't request website")
else:
  soup = BeautifulSoup(response.text, "html.parser")
  jobs = soup.find_all('section', class_="jobs")
  print(len(jobs)) #job이라는 class를 가진 section이 몇개가 있는지 출력
  #section안의 ul안에 있는 li내용을 받아오고 싶음
  for job_section in jobs:
    job_posts = job_section.find_all("li")
    job_posts.pop(-1) #list의 마지막 항목 제거
    #print(job_posts)
    for post in job_posts:
      print(post)
      print("/////////////") #seperator
    #li"view-all" : 버튼, 제외돼도 됨 -> line19
   

#5.7 Job Extraction
#링크, 회사이름, job title, position, region등 중요한 정보만 빼와야 편함
from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
  print("Can't request website")
else:
  soup = BeautifulSoup(response.text, "html.parser")
  jobs = soup.find_all('section', class_="jobs")
  #print(len(jobs)) 
  for job_section in jobs:
    job_posts = job_section.find_all("li")
    job_posts.pop(-1) 
    for post in job_posts:
      anchors = post.find_all("a")
      anchor = anchors[1]
      link = anchor['href']
      #print(anchor['href'])#link만 가져옴
      company, kind, region = anchor.find_all('span', class_="company")
      #print(company, kind, region)
      title = anchor.find('span', class_="title")
      print(company, kind, region, title)
      print("//////////////////")
      print("//////////////////")
    

"""python에서 object의 list를 가지고 있고 list의 길이를 안다면 list에서 object를 가져오는 쉬운 코드가 있음: 
list_of_numbers : list의 각 요소를 변수로 만들어줄 수 있음
ex) first, second, third = list_of_numbers
"""


#5.8 Saving Results
#span에서 text 추출 - .string method사용 - 텍스트만 추출
from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"#python대신 java, react등 원하는 검색어로 검색 가능
#java로 검색할때 javascript도 검색되는데 javascript를 제한 할 방법은 있을까?

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
  print("Can't request website")
else:
  result = []
  soup = BeautifulSoup(response.text, "html.parser")
  jobs = soup.find_all('section', class_="jobs")
  #print(len(jobs)) 
  for job_section in jobs:
    job_posts = job_section.find_all("li")
    job_posts.pop(-1) 
    for post in job_posts:
      anchors = post.find_all("a")
      anchor = anchors[1] #0번째 list제외
      link = anchor['href']
      #print(anchor['href'])#link만 가져옴
      company, kind, region = anchor.find_all('span', class_="company")
      #print(company, kind, region)
      title = anchor.find('span', class_="title")
      #print(company.string, kind.string, region.string, title.string)

      job_data = {
        'company': company.string,
        'region': region.string,
        'position': title.string
      }
      result.append(job_data) #이렇게 하지 않으면 for문을 돌면서 데이터가 사라짐. 그래서 result라는 빈 list를 만들고 for 문 안에서 append를 통해 계속 추가해주는것
      
      #print("//////////////////")
      #print("//////////////////")
  for result in result:
    print(result) #dictionary로 가득찬 list출력!!
    print("//////////////")



#5.9 Recap
#import
from requests import get
from bs4 import BeautifulSoup

#바뀌지 않는 url
base_url = "https://weworkremotely.com/remote-jobs/search?term="
#검색어
search_term = "python"

#두개 합쳐서 전체 url response
response = get(f"{base_url}{search_term}")

#status code확인
if response.status_code != 200:
  print("Can't request website")
else:
  result = []
  soup = BeautifulSoup(response.text, "html.parser")#방금얻은 웹사이트의 코드를 BeautifulSoup에 줘서 python 데이터구조로 이용할 수 있게 함 ex.아래처럼 코드로 검색
  jobs = soup.find_all('section', class_="jobs") #section태그의 class_="jobs"인 모든걸 찾아
  for job_section in jobs:
    job_posts = job_section.find_all("li") #그 안에서 li태그 찾아
    job_posts.pop(-1) #맨 마지막 li지워 (쓸데없는 내용)
    for post in job_posts:
      anchors = post.find_all("a") #그 안에서 a태그 찾아
      anchor = anchors[1] #첫 번째 a제외
      link = anchor['href'] #link저장(url부분)
      #print(anchor['href'])#link만 가져옴
      company, kind, region = anchor.find_all('span', class_="company") #span태그의 class_="company"인 모든걸 찾아서 list를 얻음(list의 모든 값을 꺼내서 저장)
      #company = list[0]
      #kind = list[1] .... 이런식으로 귀찮게 저장할 필요가 없음
      
      title = anchor.find('span', class_="title")

      #dictionary만들기
      job_data = {
        'link' : link,
        'company': company.string, #.string: 태그안에 있는 텍스트를 줌(보기에 안좋은 쓸데없는 코드 삭제)
        'region': region.string,
        'position': title.string
      }
      result.append(job_data) #result라는 list에 하나씩 추가
      
  for result in result:
    print(result) #dictionary로 가득찬 list출력!!
    print("//////////////")


#5.10 Refactor
#시작하기 전에 wwr.py로 #5.9까지 작성한 코드(weworkremotely에서 직업찾기) 함수로 저장
#폴더, 파일명 확인!
from requests import get
from bs4 import BeautifulSoup
#기존 스크래퍼랑 다른점은 return값을 받는것, 검색어를 함수의 argument로 작성하기 때문에 코드내에 작성할 필요가 없는것 정도 
#extractors폴더의 wwr에 있는 함수 extract_jobs를 import 
from extractors.wwr import extract_wwr_jobs

jobs = extract_wwr_jobs("python")
print(jobs)# refactoring done


#5.11 Recursive(재귀: 반복되는) (5.12랑 같이보기)
#폴더, 파일명 확인!
#from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs
"""
base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
  print("Can't request page")
else:
  print(response.text) #실행하는데 Can't request page나옴 왜지? url복사해서 이동하면 정상작동하는데 지금코드 실행하면 에러남"""
"""
indeed에서 bot으로 추정되는 것들은 막고 있습니다.
( 1:50초까지 작업한 내용들을 실행시키면 403에러 발생으로 실행되지 않습니다. )

니콜라스 선생님도 영상 올리고 난 후 이 사실을 알게 되었고,
이를 해결하기 위해 다음 강의에서 Selenium을 이용한 우회 방법을 설명하십니다.

그러니 1:50초까지만 강의를 들으시고, 다음 강의 들으신 수강 진행해 주시면 됩니다. 댓글에도 두 강의 이해 하기 쉽게 각 강의마다 수강생 분들이 글을 남겨 두었으니 읽어보실 추천합니다. :)

---

[ 다음 강의랑 연동해서 보면 좋은 코드 ]

soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = (soup.find("ul", class_="jobsearch-ResultsList"))
jobs = job_list.find_all('li', recursive=False)
# print(len(jobs))
for job in jobs:
print(job)

---
"""
#5.12 Indeed 403 fix (5.11이랑 같이보기)

# indeed.com에서 어떤 페이지를 요청하려면 selenium 을 배워야 할 필요가 있음
# 5.11강 처럼 진행하면 indeed.com에서 나를 봇으로 판단해서 봇이 아님을 확인하는 페이지로밖에 못 넘어감
# selenium : 브라우저를 자동화(automate)할 수 있는 프로그램 - 이게 어떻게 해결하는데?
# -> 구글 크롬 브라우저를 열고 브라우저로 해당 페이지에 방문, 검색까지 자동으로 진행시킴

# selenium사용하려면 replit에 셀레니움 설치, 브라우저 설치가 모두 필요함
# Files - 점3개 - show hidden files - replit.nix - deps[]안에 pkgs.chromium, pkgs.chromedriver 작성

from requests import get
#import selenium이거 먼저하고 설치 끝나면 밑에줄 코드로 바꿈
from selenium import webdriver
#webdriver : 파이썬에서 브라우저를 시작할 수 있는 방법
from selenium.webdriver.chrome.options import Options

#옵션 두개는 replit에서 실행하기 위한 코드임 - 무시
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

browser.get("https://kr.indeed.com/jobs?q=python&limit=50") 

#print(browser.page_source) 정상적으로 실행

#5.11로 돌아와서
"""status_code프로퍼티(property)는
request라이브러리(https://pypi.org/project/requests/)의
프로퍼티이므로 더이상 사용 못함
그래서 200인지 확인하는 If문 로직을 제거하고 진행"""
soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = soup.find("ul", class_="jobsearch-ResultsList")
jobs = job_list.find_all("li", recursive=False)#ul 바로 아래의 li만 원하기 때문에 그 다음것들을 찾지 않을 방법이 필요한데 그게 recursive=False 
#print(len(jobs))

for job in jobs:
 print(job)
 print("//////////")
 print("//////////")
# recursive = False => 바로 아래만 찾아줌
# mosaic zone까지 바로 포함되는 문제점있음 - 5.13강

#보기 쉽게 한번에 코드 정리
"""
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome(options=options)

base_url = "https://kr.indeed.com/jobs"
search_term = "python"

browser.get(f"{base_url}?q={search_term}")
soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = soup.find("ul",class_="jobsearch-ResultsList")
jobs = job_list.find_all('li', recursive=False)
print(len(jobs))
for job in jobs:
 print(job)
 print("//////////")
 print("//////")
"""


#5.13 None
#None: 데이터 타입, 변수 혹은list, dict에도 넣을수 있음 None != False
# None : Something isn't there
# False : Something isn't True

  from bs4 import BeautifulSoup
  from selenium import webdriver
  from selenium.webdriver.chrome.options import Options

  options = Options()
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-dev-shm-usage")
  browser = webdriver.Chrome(options=options)

  browser.get("https://kr.indeed.com/jobs?q=python&limit=50")
  soup = BeautifulSoup(browser.page_source, "html.parser")
  job_list = soup.find("ul",class_="jobsearch-ResultsList")
  jobs = job_list.find_all('li', recursive=False)

  for job in jobs:
    zone = job.find("div", class_="mosaic-zone")
    if zone == None: #find는 찾은 element 아니면 None을 줌
      print("job li")
    else:
      print("mosaic li")
    #AttributeError: 'NoneType' object has no attribute 'find_all' -> 검색 결과가 없어서 


#5.14 Select
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome(options=options)

browser.get("https://kr.indeed.com/jobs?q=python&limit=50")
soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = soup.find("ul",class_="jobsearch-ResultsList")
jobs = job_list.find_all('li', recursive=False)

for job in jobs:
  zone = job.find("div", class_="mosaic-zone")
  if zone == None:
    #h2 = job.find("h2", class_="jobTitle")
    #a = h2.find("a")
    anchor = job.select_one("h2 a")
    title = anchor['aria-label']
    link = anchor['href']
    print(title, link)
    print("/////////\n//////////")