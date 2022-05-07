# 위에서 아래로

n=int(input())
array=[]

for _ in range(n):
    a=int(input())
    array.append(a)

array.sort(reverse=True)

for i in array:
    print(i,end=' ')