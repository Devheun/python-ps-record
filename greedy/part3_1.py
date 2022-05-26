# 모험가 길드

n=int(input())

ghost=list(map(int,input().split()))

ghost.sort()

result=0
cnt=0 # 현재 그룹에 포함된 모험가 수

for i in ghost:
    cnt+=1
    if cnt>=i:
        result+=1
        cnt=0
print(result)
    