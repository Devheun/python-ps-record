# with Hoare Partition (First data is pivot)
array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end): # quicksort는 분할 가능할때까지 분할
    if start>=end: #원소가 1개일때는 분할 불가이므로 종료
        return
    pivot=start
    left=start+1
    right=end
    
    while left<=right:
        
        while left<=end and array[left]<=array[pivot]: #pivot보다 큰 데이터 찾을때까지
            left+=1
        while right>start and array[right]>=array[pivot]: #pivot보다 작은 데이터 찾을때까지
            right-=1
        if left>right: #엇갈렸으면 작은 데이터와 피벗 위치 교환
            array[right],array[pivot]=array[pivot],array[right]
        else: #엇갈리지 않았으면 작은 데이터와 큰 데이터 교환
            array[left],array[right]=array[right],array[left]
    
    quick_sort(array,start,right-1) #분할 이후 왼쪽 파티션
    quick_sort(array,right+1,end) #분할 이후 오른쪽 파티션
            

quick_sort(array,0,len(array)-1)
print(array)