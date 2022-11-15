#문자열 처리함수

python = "Python is Amazing"
print(python.lower()) # 소문자로
print(python.upper()) # 대문자로
print(python[0].isupper()) #대문자인지 확인
print(len(python)) #문자열 갯수
print(python.replace("Python","Java")) #문자열을 대체

index = python.index("n")
print(index) #첫번째 문자열의 위치를 알려줌
index = python.index("n", index +1)
print(index) #그 다음 두번째 문자열의 위치를 알려줌
print(python.find("Java")) # 원하는 값이 없으므로 -1이 반환됨
# print(python.index("Java")) #에러 발생해서 중단됨

print(python.count("n")) #N의 갯수

# print("a" + "b")
# print("a", "b")

#방법 1
print("나는 %d살입니다" % 20) #정수값
print("나는 %s을 좋아해요" %"파이썬") #문자열값
print("Apple은 %c로 시작해요." %"A") #문자 한글자만

# %s로 하면 정수, 문자열, 문자 모두 할 수 있다.

print("나는 %s색과 %s색을 좋아해요" %("파란","빨간"))

#방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란","노란"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란","노란"))

#방법 3
print("나느 {age}살이며,{color}색을 좋아해요".format( age =20, color="빨간"))

#방법 4(3.6이상부터)
age= 20
color ="빨간"
print(f"나는 {age}살이며,{color}색을 좋아해요")

#탈출 문자
#\n : 줄바꿈
#\",\' : 문장 내에서 따옴표
print("백문이 불여일견\n백견이 불여일타")
print('저는 "나도코딩"입니다')
print("저는 \"나도코딩\"입니다")
# \\ : 문장 내에서 \
print("C:\\Users\\Nadocoding\\Desktop\\Python")

# \r : 커서를 맨 앞으로
print("Red Apple\rPine")
# \b :한 글자 삭제
print("Redd\bApple")

#\t : 탭
print("Red\tApple")

#퀴즈

domain = "http://daum.com"
index = domain.index(".")
#print(index)
password = domain[7:index]
password = password[0:3] + str(len(password)) + str(password.count("e")) + "!"
print( f"생성된 비밀번호 : {password}")


# 정답
url ="http://daum.com"
my_str = url.replace("http://","")
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(url,password))








