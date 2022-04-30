# 답안 코드 : 1 빼는 개수를 한번에 구해서 시간 절약하기

N,K=map(int,input().split())
cnt=0

while True:
    target=(N//K)*K #가장 가까운 나누어 떨어지는 수 구하기
    cnt+=(N-target) #1 빼주는 개수 한번에 더하기
    N=target
    
    if N<K:break #N이 K보다 작을땐 반복문 탈출하고 1번방법 횟수 더해주기
    
    cnt+=1
    N//=K

cnt+=(N-1)
print(cnt)