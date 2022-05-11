# 바닥 공사

# f(1)=1 f(2)=3 f(3)=5 -> a_i=a_(i-1)+2 -> wrong answer!

#n=int(input())
#d=[0]*1001
#d[1]=1
#for i in range(2,n+1):
    #d[i]=(d[i-1]+2)%796796
#print(d[n])

#a_i=a_(i-1)+a_(i-2)*2 -> right answer!

n=int(input())
d=[0]*1001
d[1]=1
d[2]=3

for i in range(3,n+1):
    d[i]=(d[i-1]+d[i-2]*2)%796796

print(d[n])
