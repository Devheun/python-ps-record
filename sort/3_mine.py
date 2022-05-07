# 두 배열의 원소 교체

n,k=map(int,input().split())
array_a=list(map(int,input().split()))
array_b=list(map(int,input().split()))

# 바꿔치기 -> a배열은 오름차순, b배열은 내림차순 정렬한 후 0번 인덱스부터 k-1번 인덱스까지 교환
array_a.sort()
array_b.sort(reverse=True)

for i in range(k):
    if array_a[i]<array_b[i]: # 무조건 a의 원소가 b의 원소보다 작을때만 교환 !!!
        array_a[i],array_b[i]=array_b[i],array_a[i]
    else : break
        
print(sum(array_a))
    