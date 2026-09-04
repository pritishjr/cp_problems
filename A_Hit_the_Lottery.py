
def main():
    
    n = int(input())
    denominations = [100, 20, 10, 5, 1]

        # if n>=100:
        #     count += n//100
        #     rem = n%100
            
        #     if rem>=20:
        #         count += rem//20
        #         rem2 = rem%20
                
        #         if rem2>=10:
        #             count +=
    count = 0

    for coin in denominations:
        count += n//coin
        n%=coin #taking the remainder 
        
    print(count)
    
if __name__ == "__main__":
    main()