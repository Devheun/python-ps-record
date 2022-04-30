# 큰 수의 법칙

## 단순 코드지만 M의 크기가 커지면 시간초과가 날 수 도 있다. ((((풀이 1))))
n,m,k=input().split()
n=int(n)
m=int(m)
k=int(k)
cnt=0 # k 관련 횟수 세는 변수
total=0 #큰 수 저장 변수

total_cnt=0
array=list(map(int,input().split()))

array.sort(reverse=True)

while True:
    total_cnt+=1
    cnt+=1
    if total_cnt>m:
        break
    if cnt>k:
        total+=array[1]
        cnt=0
    else:
        total+=array[0]
    
print(total)