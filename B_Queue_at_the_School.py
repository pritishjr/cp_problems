
def main() -> None:
    
    n,t = map(int, input().split())
    s = str(input())
    
    #clarity: all the boys can switch positions at the same time and it is not sequential.
    
    #my attempt: (first principle)
    #for every number of time periods, we:
    #1. identify ("B","G") pairs from the string
    #2. swap and create the resultant-updated string
    #3. this updated string becomes the new string. fin.
    
    #put all the elements of s in a list so its easy.
    list_elements = [i for i in s]
    
    for _ in range(t):
        i = 1
        
        while i < n: 
            if list_elements[i-1] == "B" and list_elements[i] == "G":
                #swap:
                list_elements[i-1],list_elements[i] = list_elements[i],list_elements[i-1]
            
                #we must jump 2 steps ahead to perform this operation again:
                i += 1
        
            i+=1
        
    print(''.join(list_elements))
    
if __name__ == "__main__":
    main()