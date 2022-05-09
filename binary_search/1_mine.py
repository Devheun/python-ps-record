# 부품 찾기

def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            print("yes",end=' ')
            return
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    print("no",end=' ')


n=int(input())
remain=list(map(int,input().split()))

remain.sort()

m=int(input())
req=list(map(int,input().split()))

for i in range(len(req)):
    binary_search(remain,req[i],0,n-1)