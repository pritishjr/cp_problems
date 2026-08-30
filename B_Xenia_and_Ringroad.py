#n number of houses and m numebr of tasks

def main():
    n,m= map(int, input().split())
    a= list(map(int, input().split()))
    time=0
    pos=1
    for i in range(m):
        if(a[i]>pos):
            time += (a[i] - pos)%n
            pos = a[i]
        elif(a[i]<pos):
            time += (a[i]-pos+n)%n
            pos = a[i]
    
    print(time)

if __name__ == "__main__":
    main()
