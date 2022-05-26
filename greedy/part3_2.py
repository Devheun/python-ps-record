# 곱하기 혹은 더하기 (모든 연산은 왼쪽에서부터 순서대로. 곱하기가 더하기보다 먼저 X)

s=map(int,input())
result=0 # 결과 담는 변수

for i in s:
    if result<=1 or i<=1:
        result+=i
    else:
        result*=i
print(result)
        