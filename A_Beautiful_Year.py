
def main():
    
    year = int(input())
    
    y = year+1
    while True:
        
        y_num = str(y)
        array = []
        for char in y_num:
            array.append(int(char))
        
        res_set = set(array)
        
        if len(res_set) == len(array):
            print(int(y_num))
            break
        else:
            y+=1

if __name__ == "__main__":
    main()