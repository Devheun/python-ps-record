# 성적이 낮은 순서로 학생 출력하기

n=int(input())
array=[]

for _ in range(n):
    input_data=input().split()
    array.append((input_data[0],int(input_data[1])))
    
array=sorted(array,key=lambda array:array[1]) #람다 함수 이용하거나 함수만들어서 key값 세팅

for i in array:
    print(i[0],end=' ')