array=[7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)): # 첫번째 데이터는 그 자체로 정렬되어있다고 판단
    for j in range(i,0,-1):
        if array[j]<array[j-1]:
            array[j],array[j-1]=array[j-1],array[j]
        else:
            break

print(array)