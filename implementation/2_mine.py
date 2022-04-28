# 시각 : 00시00분00초부터 N시 59분 59초까지 3이 하나라도 포함되는 모든 경우의수 출력 (초,분 : 03,30,33, 시 : 3,13,23)
n=int(input())
cnt=0

for i in range(n+1): #시
    for j in range(60): #분
        for k in range(60): #초
            if k%10==3 or k//10==3 or j%10==3 or j//10==3 or i%10==3:
                cnt+=1
print(cnt)