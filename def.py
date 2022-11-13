#함수
#파라미터는 여러개 전달 가능하다. (콤마로 구분) 그리고 함수 내에서만 사용 가능하다.
def show_price(customer):
    print(f'사랑하는 {customer}고객님')
    print("커트가격은 10000원 입니다.")

customer1= "나장발"
show_price(customer1)

#반환값
#여러개 반환 가능(콤마로 구분, 튜플) , 반환되는 즉시 함수를 탈출한다. 즉 return 밑에 코드가 있어도 실행 안

def get_price(is_vip): #True: 단골손님, False: 일반 손님
    if is_vip == True:
        return 10000
    else:
        return 15000

price=get_price(True)
print(f'커트가격은 {price}원입니다')