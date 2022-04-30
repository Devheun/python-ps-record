## 수학적으로 접근하면 시간초과 X
n,m,k=input().split()
n=int(n)
m=int(m)
k=int(k)
array=list(map(int,input().split()))
array.sort(reverse=True)
count=0

#가장 큰 수가 더해지는 횟수 계산 (k+1)은 수열의 길이.
count+=(m//(k+1))*k
count+=(m%(k+1))

result=0
result+=count*array[0]
result+=(m-count)*array[1]
print(result)
