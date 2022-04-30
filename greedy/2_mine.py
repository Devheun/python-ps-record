# 숫자 카드 게임(answer와 비슷하므로 2_answer.py 생략)
n,m=input().split()
n=int(n)
m=int(m)
max_integer=0

for i in range(n):
    array=list(map(int,input().split()))
    min_integer=min(array)
    max_integer=max(max_integer,min_integer)
print(max_integer)