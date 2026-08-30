
def main():
    
    n,h= map(int, input().split())
    heights= list(map(int, input().split()))
    
    flag = 0
    for height in heights:
        
        if height > h:
            flag += 1
         
    total = n + flag
    print(total)

if __name__ == "__main__":
    main()