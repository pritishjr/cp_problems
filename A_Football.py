def main():
    n=int(input())
    dictionary={}
    for i in range(n):
        name=input()
        dictionary[name]=dictionary.get(name,0)+1

    sorted_items = sorted(dictionary.items(),key=lambda x: -x[1])
    print (sorted_items[0][0])
if __name__ == "__main__":
    main()
