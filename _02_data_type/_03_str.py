# str(문자형, 문자열, string)/ " ", ' ', """ """, ''' ''' 감싸서 표현

print("--- 홑따옴표, 쌍 따옴표---")
s1= 'Hello'
s2= 'World'
s3="'1234'" #홑따옴표가 문자 그 자체로 인식됨

print(type(s1),type(s2))
print(s3)

#삼중 따옴표
print("""
삼중 따옴표는 입력된 형식 그대로 문자열(str)로 변환
""")

print("""앞/뒤 엔터없이 작성하려면 
따옴표와 문자열을 딱 붙여서 작성해야해""")

#str 연산
# 1. 문자열+문자열=이어쓰기, 이어붙이기 등

print('---문자열 더하기 연산---')
a= 'apple'
b='banana'
print(a+', '+ b)
# 2. 문자열* 양의 정수= 양의 정수 크기만큼 반복하세욘
print('-' * 20)
#print('a' - 'b') 빼기 연산은 불가/중간에 오류가 나면 실행이 안되니 꼭 주석처리

# str method(str api) api:기능제공
# (참고) 함수, 메서드==기능(실행 후 기능이 반환이 된다.)

# len(객체): 파이썬 객체의 길이 반환.
# 파이썬 객체: str, list, tuple, dic, set, 임의의 class 등
print("---len---")
text="오늘 점심은 뭘 먹죠?"

print(text,len(text)) #class 거의 전역 method 객체 의존
#str.replace(old,new) # str내에서 old에 해당되는 문자를 new로 치환(변경)
today='2026-06-01'
#print(today, today.replace(old:'-', new:'/'))

# str.strip([str])
# 코드 작성법에서 []는 생략가능

#대소문자 관련 str method

origin_str = 'hELLO wORLD!'

print(origin_str.upper())         # HELLO WORLD!
print(origin_str.lower())         # hello world!
print(origin_str.capitalize())    # Hello world!
print(origin_str.swapcase())      # Hello World!
print(origin_str.title())         # Hello World!


x = 10
print("x is %d" %x)    # x is 10

y = "code"
print("y is %s" % y)    # y is code

x, y = 10, "code"

print("x is {0}".format(x))                                        # x is 10
print("x is {0} y is {1}".format(x,y))                             # x is 10 y is code
print("x is {new_x} and y is {new_y}".format(new_x=x, new_y=y))    # x is 10 and y is code

#f-string(format string)
print("---fstring---")
print(f"난 {'나무'}다")


#-----문자열 인덱싱/슬라이싱
#파이썬 문자열(str)은 text sequence(순차적인) 형태를 갖는다.
# index:순서(기본 0)

print("----문자열 indexing==")
x ="Monday"
print('x의 길이:', len(x)) #길이 6, 인덱스 0,1,2,3,4,5
#마지막 인덱스==str길이-1

print(x[0]) #대괄호/배열(나열) 기호/str 배열중 0번째 인덱스이다./파이썬은 역인덱스도 제공.
#역 인덱스:str을 거꾸로 탐색.
print(x[-1], x[-2], x[-3], x[-4], x[5], x[-6])


print("----str 슬라이싱-----") #문자열 일부를 잘라서 가져오겠다.
# str[start:stop:step]
# start:시작 인덱스/stop:종료 인덱스(미포함)/step:건너띄는 갯수(생략시 기본값 1)

test='Hello world'

print("len(test)")

print("text[0:5:1]",text[0:5:1])
print("text[0:5:]",text[0:5:])
print("text[:5]",text[:5])
print("text[:]",text[:]) #전부
print("text[6:11]:",text[6:11])
print("text[6:len(text)]:,text[6:len(text)]",text[6:len(text)])

print("text[0:11:2]:",text[0:11:2])
print("text[::2]:",text[::2]) #2개씩/ 0,2,4,6,10
print("text[::-1]:",text[::-1]) #거꾸로/


#문자열 불변타입(immutable)
#str는 한번 메모리에 값이 저장되면 수정할수 없다/만들고 지우는 건 가능
s= 'python' #s에는 'python' str 메모리 주소가 저장됨.
print("s:",s) #s에 저장된 주소를 찾아가서 파이썬 str를 참조한다.
print("변경 전 s:",id(s)) #id(s) 변수에 저장된 값의 주소를 담음.
s=s+'python Hello'
print("s:",s)
print("변경 후 s",id(s))

#in 연산자(멤버십 검사 연산자)
# -특정 값이 포함되어 있는 지 검사한다.
# -결과는 bool 형태
print("---in 연산자---")
txt2="김밥, 라면, 어묵, 떡볶이"
print("라면" in txt2)
