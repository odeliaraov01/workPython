# name = "연탄"
# animal = "강아지"
# age= 4
# hobby = "산책"
# is_adult = age>= 3
#
# print("우리집"+ animal +"의 이름은" + name + "예요")
# print(name +"는 "+str(age)+"살이며 " + hobby +"을 좋아해요")
# print(name,"는",age,"살이며",hobby,"을 좋아해요")
# # '+'로 묶으면 문자열이 되기 때문에 띄어쓰기 없이 이어붙일 수 있다. 대신 str 문자형만 가능함
# # ','로 묶으면 문자형이 아니어도 이어붙일 수 있으나 띄어쓰기가 하나씩 붙음
# print(name +"는 어른일까요?" + str(is_adult))
#
# #주석은 command + / 하면 한번에 주석 처리 가능함
# '''
# 길게 주석하기
# '''
#
# station = "사당"
# print(station, "행 열차가 들어오고 있습니다.)
import random
# print(1+1)
# print(3-2)
# print(2**3)
# print(5%3) #나머지
# print(5/2) #나누기
# print(5//2) #몫
#
# print(abs(-5)) # 절댓값
# print(max(5,12,533))
# print(min(5,12,544))
# print(round(3.14))

from random import *
print(random()) #0.0~1.0 미만의 난수를 출력

day = randint(4,28) #randint(a,b) a부터 b를 포함해서 그 사이 숫자를 리턴
print("오프라인 스터디 모임 날짜는 매월"+str(day)+"일로 선정되었습니다")

sentence = "나는 소년이다"
print(sentence)
sentence2= """
나는 소년이고 
파이썬은 쉬워요 
그쵸?"""
print(sentence2)

#슬라이싱
jumin = "990120-1234567"

print("성별: "+ jumin[7])
print("연: "+ jumin[0:2]) # a[0:n+1] 0부터 2 직전까지
print("월:" + jumin






