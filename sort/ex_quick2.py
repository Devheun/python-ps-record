# specially useful to python

array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array)<=1: #리스트가 하나 이하의 원소만 있다 -> 종료
        return array
    
    pivot=array[0]
    remain=array[1:]
    
    left=[x for x in remain if x<=pivot] # left partition
    right=[x for x in remain if x>pivot] # right partition
    
    return quick_sort(left)+[pivot]+quick_sort(right) # 왼쪽 분할과 오른쪽 분할에서 정렬하고, 전체 리스트 반환 (리스트 덧셈 이용)

print(quick_sort(array))