def main():
    rules= True
    str= input()
    for char in str[1:]:
        if char != char.upper(): #not uppercase
            rules=False
            break

    if rules:
        for char in str:
            if char != char.upper():
                print(char.upper(), end="")
            else:
                print(char.lower(), end="")

    else:
        print(str)

if __name__ == "__main__": 
    main()


        