# a = 2    #각각 메모리로 감 ex.0x0001
# b = 3
# c = a + b    #변수들로 새로운 변수를 만들 수 있음
# c = 1        #위에서 아래로 읽음 -> 1출력
# a = 1
# b = 10       #c는 안변함
# print(c)

# my_age = 88

#2.2
# Data types
# a = 654    #number
# print(a)
# my_name = "nico"    #text
# b = "1231231234"
# print(my_name)

# #boolean - True/False
# #대문자 필수
# c = True  #1, ON
# d = False #0, OFF

#2.3
# my_name = "hoon"
# age = 27
# dead = False
# print("Hello my name is", my_name)
# print("and I'm", age, "years old")

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
