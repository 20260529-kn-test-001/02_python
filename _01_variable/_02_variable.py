#변수(variable)
# - 값(literal)을 저장하는 메모리 상의 공간
# - 각 변수마다 이름이 지정되어있다.(이름을 불러서 사용할 거임)

# 변수선언방법
# 변수명 =값
a=10 #a라는 메모라상의 공간에 10이라는 literal을 대입.
b='홍길동'

print("a=", a)
print("b=", b)

# 대입 연산자(=)
# -우항의 값을 좌
num= 100
print("num=", num)

#변수는 저장된 값이 변할 수 있다.
num=999
print("num=", num)

num="abcdefq"
print("num=", num)

team_name = "오지라퍼스"
print(team_name)    # 오지라퍼스

Team_name = "Ohgiraffers"
print(team_name)    # 오지라퍼스
print(Team_name)    # Ohgiraffers

밥조="4조"

print(밥조)
# 1_team_name="밥조"
# print(1_team_name) //문법 오류 발생-숫자로 시작
# 굳이 숫자로 시작하고 싶으면 '_' 이거 맨 앞에 붙여라. e.g)_1_test

# 123455="test"- 변수명이 숫자로만 이뤄져서 오류
print(123455) # 얜 그냥 됨
#특수문자는 _ 빼고는 사용 물가/!,@,#,$,- 등등 ->No

# team-name=12/ '-' 불가
# email@test/'@' 불가
# ctrl+ D 한줄 복사.

#예약어는 변수명으로 사용불가(e.g. for, else, if, while, range 등등)

#파이썬 예약어 종류 확인.

import keyword
print(keyword.kwlist) #키워드 리스트(예약어) 출력/ 이거 보고 참고해라.




#2. 변수명은 snake_case를 이용한다. (소문자 + _)
# 단 대문자도 사용가능하고, 인터프리터가 구분이 가능하다.
