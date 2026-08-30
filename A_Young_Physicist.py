n = int(input())
x_t,y_t,z_t=0,0,0
for i in range(n):
    x,y,z=map(int,input().split())
    x_t+=x
    y_t+=y
    z_t+=z

if (x_t==0 and y_t==0 and z_t==0):
    print("YES")
else:
    print("NO")

