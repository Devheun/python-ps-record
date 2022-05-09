# 떡볶이 떡 만들기 (절단기 높이 최대값 구하기)

def binary_search(array,short,long):
    
    global height
    while short<=long:
        mid=(short+long)//2
        for i in range(n):
            if array[i]-mid>0: # 음수 더해주는것 때문에 처음에 답 안나옴 !!!!
                height+=(array[i]-mid)
            else:
                continue
            
        if height==m:
            return mid
        elif height>m:
            short=mid+1
            height=0
        else:
            long=mid-1
            height=0            


# n은 떡의 개수, m은 요청한 떡 길이
n,m=list(map(int,input().split()))
ttuk=list(map(int,input().split()))

tall_ttuk=max(ttuk)
height=0

result=binary_search(ttuk,0,tall_ttuk)
print(result)