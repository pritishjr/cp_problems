
s=input().lower().strip()
hello_tuple = ('h', 'e', 'l', 'l', 'o')
index=0
new_s=""
for char in s:
    if index<len(hello_tuple) and char == hello_tuple[index]:
        new_s += char
        index+=1
         

if new_s == "hello":
    print("YES")
else:
    print("NO")

