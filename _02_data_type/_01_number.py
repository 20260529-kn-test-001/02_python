# number(숫자형)
# -정수
# -실수
# -복소수

#type(변수명 |(or) 값 ): 변수 또는 값의 타입을 확인하는 내장 함수.

# 정수 (int):integer/
n = 123
print(n, type(n))

price =1_000_000_000;
print(price, type(price))

# 정수(int)의 최댓값.
import sys
print(sys.maxsize,type(sys.maxsize)) #8byte=64bit (1칸당 0,1/ 2**n 표현/2**64)

# 2진법,8진법,16진법
a=0b100

# 출력은 기본적으로 10진수.

b=0o23 #19(8*2+1*3)

c=0xff #0~9/a,b,c,d,e,f/   (16*15+1*15=17*15)==255

# 실수(float)
f1=123.456
print(f1,type(f1))

f2=1.01234567890123456789 #소수점 아래 16자리까지 표현이 가능하다. 정확한 소수는 아님(부동소수점 표기법)
print(f2,type(f2))

#복소수(complex) j로 표시

c=2j

print(c,type(c))

d=3+4j

print(d,type(d))

#-----------------------------------
# 산술연산(+,-,*,/,//(몫만),%(나머지,modulo,mode), **(거듭제곱))
print("----산술연산------")
print(1+2)
print(1-2)
print(1*2)
print(1/2) #나누어 떨어질때까지의 몫을 구함
print(1//2) #정수 영역에서만 몫을 구함
print(1%2) #정수 영역에서의 나머지

print(2**63) #+- 넘어가지 않도록 64-1/int 양의 최대값.