# 효율적인 화폐 구성 (그리디에서는 화폐 가치가 배수관계지만 여긴 X)

n,m=map(int,input().split()) #n은 화폐 종류, m 가치의 합
array=[]
d=[10005]*(m+1)
d[0]=0
for _ in range(n):
    k=int(input())
    array.append(k)

for i in range(n):
    for j in range(array[i],m+1): #핵심은 적은 금액부터 큰 금액까지를 차례대로 dp (구현에서 막힘)
        if d[j-array[i]]!=10005:
            d[j]=min(d[j],d[j-array[i]]+1)

if d[m]==10005:
    print(-1)
else:
    print(d[m])
        
