def main():
    s,n =map(int,input().split())
    x,y=[],[]
    for i in range(n):
        x_i,y_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)
        continue

    paired = list(zip(x,y))
    paired.sort()
    x,y=zip(*paired) # or can use: x=[i[0] for i in paired], y=[i[1] for i in paired]
    
    for i in range(len(x)):
        if s>x[i]:
            s+=y[i]
        else:
            print("NO")
            quit()

    if s>=x[n-1]:
        print("YES")
    
if __name__ == "__main__":
    main()