#tuple
#변경불가(immutable)한 list
#sequence type(indexing, slicing, iterable)
#함수 반환값, 안전한 데이터 집합 생성, 신뢰성있는 데이터

print("---tuple---")
t1=() #비어있는 튜플
t2=(10,) #(10)은 int로 인식된다./ , 사용해야 튜플타입 인식
t3=10,20 #()생략한 튜플->자동 패킹

#tuple indexing, 수정불가/읽기 전용

#인덱스 통해 수정하려고 해도(e.g. tpl[2]= 9/ 변경이 되지 않는다. 에러가 뜨긴 하나, 일단 변경하지 않은 튜플 값을 준다)

tpl=('a','b','c','d','e')

#tuple 슬라이싱
print("----tuple 슬라이싱----")
print(tpl[0:3])
print(tpl[::2])

#unpacking
q,w,e,r,t=tpl
*rf, d=tpl
print(rf,d) #list형 하지만 튜플 내부라서 수정불가
print(q,w,e,r,t)

#tuple 이용한 변수값 할당
num1,num2=100,200 #괄호 생략된 튜플
print(num1,num2)

num1,num2=num2,num1 #대입연산은 오른쪽이 선, python 특유


