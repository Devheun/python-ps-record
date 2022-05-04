# 게임 개발

n,m=map(int,input().split())
a,b,direc=map(int,input().split()) #direc - 0 : 북, 1 : 동, 2 : 남, 3 : 서

array=[list(map(int,input().split())) for _ in range(n)] # 좌표 0,0 부터 시작, 1이면 바다, 0이면 육지 
# !!!!!!!!!!! array에서 int로 안바꿔줘서 한참 오류 찾음 !!!!!!!!!!!!!!!

d=[[0]*m for _ in range(n)] 
d[a][b]=1 # 초기에 서 있는 위치
result=1

dx=[-1,0,1,0]
dy=[0,1,0,-1]
cnt=0 # 4면이 바다인 경우 세는거

while True:
        # 바라보는 방향 북쪽일 때
        if direc==0: 
            direc=3
        else: 
            direc-=1
        
        nx=a+dx[direc]
        ny=b+dy[direc]
        
        if nx<0 or nx>=n or ny<0 or ny>=m:continue
        if array[nx][ny]==0 and d[nx][ny]==0: #육지면
            d[nx][ny]=1
            a=nx
            b=ny
            result+=1
            cnt=0
            continue
            
        else : #바다거나 가봤거나
            cnt+=1
        
        if cnt==4: # 네 방향 다 가본칸 or 네 방향 바다
            nx=a-dx[direc]
            ny=b-dy[direc]
                
            if array[nx][ny]==0: #뒤로 갈 수 있을 때 (바다일 때만 못가고 방문했을 때는 갈 수 있음!)
                a=nx
                b=ny
            else: # 뒤로 갈 수 없을 때
                break
            cnt=0
print(result)


            
            
                





