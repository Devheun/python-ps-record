# 1이 될 때까지

N,K=map(int,input().split())
cnt=0

# 1번 과정은 N에서 1을 뺀다, 2번 과정은 N에서 K를 나눈다. K가 2보다 크므로 항상 2번과정이 우선시 되는게 이득임

while N!=1:
    if N%K==0:
        N=N//K
        cnt+=1
    else:
        N-=1
        cnt+=1

print(cnt)