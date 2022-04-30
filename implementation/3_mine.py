# 왕실의 나이트

#나이트가 갈 수 있는 방향들
steps=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

case=input()
row=int(case[1])
col=int(ord(case[0]))-96

x,y=row,col
cnt=0

for i in steps:
    if x+i[0]<1 or x+i[0]>8 or y+i[1]<1 or y+i[1]>8:
        continue
    
    cnt+=1
print(cnt)
    
    