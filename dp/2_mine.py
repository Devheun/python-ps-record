# 개미 전사

n=int(input())
array=list(map(int,input().split()))

d=[0]*101

d[0]=array[0]
d[1]=max(array[0],array[1]) # d[1]은 처음 칸에서 식량털 때가 더 많을수도 있음 !

for i in range(2,n):
    d[i]=max(d[i-1],d[i-2]+array[i])

print(d[n-1])