# 계수정렬은 데이터 크기 범위가 제한되어 정수형태로 표현할 수 있을 때만 -> 리스트 선언해야하기 때문에

array=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2] #모든 원소의 값이 0보다 크거나 같다

count=[0]*(max(array)+1) #모든 범위를 포함하는 리스트 (0부터 9까지니까 크기는 10으로)

for i in range(len(array)):
    count[array[i]]+=1

for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')