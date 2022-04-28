# 시각

n=int(input())

cnt=0

# 매 시각을 문자열로 바꿔서 '3'이 포함되어있는지 확인
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):cnt+=1

print(cnt)