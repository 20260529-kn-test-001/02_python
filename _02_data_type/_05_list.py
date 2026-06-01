# sequence type(시퀀스 자료형)
# str,list,tuple
# 저장된 값의 순서가 유지가 된다.
# 인덱싱, 슬라이싱 가능/순회(iterable)

# List
# - 여러 값(Literal)을 묶어서 관리한다/container 자료형
# - 동적으로 크기가 변할 수 있다(수정가능)

print("---List---")
lst=[1,2,3,4,5]
print(lst)
print(len(lst))
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3])
print(lst[4])

#list 저장 요소 추가/삭제
#List는 동적으로 크기 변경이 가능한 mutable 자료형
# -mutable: list, set, dict
# -immutable: int, float, bool, str, tuple(수정 원하면 버리고 새로 만들어서 주소값 지정하는 타입)

print("--- List Mutable check---")
print("lst:", lst)
print("추가 전 Id:",id(lst))

lst.append(12)
print(lst,id(lst))

lst.insert(1,3)
print(lst,id(lst))

#list[index]=값
lst[0] =-10
print(lst)

#특정 인덱스 값 제거
#list.pop(index):제거된 index 요소들을 한칸씩 당긴다.

print(lst.pop(1))
print(id(lst),lst)

#2차원 list
#0차원 점/1차원 선,2차원 면,3차원 입체
students =[
    ['홍길동',30],
    ['이순신',80],
    ['세종대왕',100]
]

print("students",students)
print(students[1])
print(students)
print(len(students)) #3=>3행이니까.
print(len(students[0])) #2 원소 2개
print(len(students[0][0])) #홍길동->홍길동의 글자수

#str.split(구분자)
# - str를 구분자를 기준으로 나눠서 list 형태로 반환.

data="홍길동,20,서울시,서초구" #csv(Comma Seperated Value)
data_= data.split(",")
print(data_)

name=data_[0]
age=data_[1]
addr1=data_[2]
addr2=data_[3]
print(name,age,addr1,addr2)

#list 슬라이싱(str 슬라이싱과 방법 동일)
print("--- list slicing ---")
texts= ["Hello", "안녕","곤니찌와","하이"]

print(texts[:2]) #hello, 안녕
print(texts[1:-1])
print(texts[0:3:2])

#slicing을 이용한 list값 변경
print(texts)
texts[:2]= ["aaa", "bbb"] #이런 식으로 수정을 할 수 있다.
print(texts)

texts[1:3:1]=["❤️💕👍","❤️❤️❤️"]
print(texts)

a=[10,20]
b=[30,40]
a=a+b
print(a)

print(b) # [30,40,10,20,30,40

#list 순회(순차접근, 순차반복)
#iterable(반복 가능한) 특징을 지니는 자료형만 가능.

print("---list  순회---")
lst=['a','b','c']

for v in lst:
    print(v)

for index,value in enumerate(lst):
    print(f"{index}:{value}")


#list API
print("----------list.count(값)-----------")
# list count=>같은 값이 몇개 있는가? 다른 언어와의 count와 다름.
fruits =["apple","banana","cherry","apple","Melon"]
print(fruits.count("apple"))

# sort: 정렬하다.
# list.sort()->원본 리스트 내에서 정렬(in-place)->원본 데이터 변경 / sorted(List)->list내용 복사해서 새로운 리스트 주소에 정렬한 값들을 복붙(not-in-place)
print("----list.sort():원본 변경----")
nums = [100,30, 50, 20, 70]
nums.sort()
print("nums:",nums)
print("nums.sort(reverse=True)",nums.sort(reverse=True))

fruits= ["apple", "banana", "cherry"]
fruits.sort(key=len)
print("fruits:",fruits)

def my_sort(elem):
    return len(elem), elem # tuple로 우선순위 지정

fruits.sort(key=my_sort)
print(fruits)

#solted():원본 유지 정렬(새 list 를 반환)
print("--- sorted(list)--")
nums=[9, 2, 4]
nums2=sorted(nums)
print(nums,nums2)

#list unpacking
#list ==변수의 묶음
#numbers =[10,20,30]
a,b,c=nums
print(a,b,c)
d, *e=nums # 나머지를 묶어서 넣을 때, 맨 마지막에 들어가는 e에 들어가는 갯수가 2개 초과일 경우 에러 발생
numbers =[10,20,30,40,50]
a, *b, c = numbers
print(a,b,c)

#list: [] -mutable
#tuple: () -immutable


