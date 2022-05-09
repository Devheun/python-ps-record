# binary_search and parametric search (Parametric search는 원하는 조건을 만족하는 가장 알맞은 값을 찾을때 ! 이진탐색 반복문이 훨씬 효율적)
n,m=list(map(int,input().split()))
array=list(map(int,input().split()))

start=0
end=max(array)

result=0

while start<=end:
    total=0
    mid=(start+end)//2
    
    for x in array:
        if x>mid:
            total+=(x-mid)
    if total<m: # 떡 양이 부족할 때
        end=mid-1
    else: # 떡 양이 같거나 많을 때
        result=mid # 최대한 덜 잘랐을 때(떡이 요청한 높이에 근접할 때)가 답이므로 값 저장
        start=mid+1
    
print(result)
        
        