# with count sort

n=int(input())
array=[0]*1000001

# 가게에 있는 거 번호 입력 받아서 기록
for i in input().split():
    array[int(i)]=1

m=int(input())
x=list(map(int,input().split()))

for i in x:
    if array[i]==1:
        print("yes",end=' ')
    else:
        print("no",end=' ')