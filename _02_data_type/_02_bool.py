# 논리형 boolean

a=True
b=False

print(a,type(a))
print(b,type(b))

# 비교 연산
# A>B: A가 B보다 크면 True/ 아니면 False
# A>=B/복합 연산 기호에선 항상 등호가 오른쪽에 위치.

# A==B: A=B이면 True/ 아니면 False
# A!=B: A와 B가 서로 같지 않으면 True

print("1 > 0.5:", 1 > 0.5)
print("1 < 0.5:", 1 < 0.5)
print("1 >= 0.5:", 1 >= 0.5)
print("1 <= 0.5:", 1 <= 0.5)
print("1 == 1:", 1 == 1)
print("1 != 1:", 1 != 1)

# 논리부정연산(not)
print(not True)
print(not False)
print(not not True)

# and 연산 (양쪽으로 값이 들어가는 연산자:이항연산자)
# -A가 참 그리고 B가 참
#  T and T ==True
#  T and F ==False
#  F and T ==False
#  F and F ==False/ and 연산은 순차적으로 진행. False 가 많이 나오는 조건을 앞에 두면, 더 짧게 하고 빠져나갈 수 있다.

print('---- and ----')
print(100>0 and 1==1) # T
print(30>20 and 123!= 123) #F
print(3 <= -13 and 12>12) #F
print(9>=9/9*9 and 12!=12+1) #T

a=9>=9/9*9
b=12!=12+1 #보기 간결해짐.
print(a and b)

#or 연산
#A 또는 B가 True 이면 결과가 True <->A와 B가 모두 F이면 F

#T or T==T
#T or F==T
#T or T==T
#F or F==F (중요)

print('----or----')
print(100>0 or 1==1) #T
print(10*10 == 100 or 1!=1) #T
print(100==0 or 10==10) #T
print(10+20*5==100 or 20/10+5==7) #T/연산 순서 기억하기!
print(10+20*5==100 or 30/10+5==2)

#60점 이상 입력시 합격(True)/불합격(False)
print("--- 합격/불합격 ---")
score= int(input('점수를 입력하세요:'))
print(score,type(score))
result =score>=60

#print("합격여부:", result)

print("합격여부:",'합격' if result == True else '불합격')

#input() 함수:키보드 입력을 받는 함수(str로 저장)
#int() 함수:str->int로 변환
