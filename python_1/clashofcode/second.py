_str = "Hello World !"
a = 0
i = 0
for i in range(len(_str)):
    if _str[i].lower == 'a' or _str[i].lower == 'e' or _str[i].lower == 'u' or _str[i].lower == 'o' or _str[i].lower == 'i' or _str[i].lower == 'y':
        a+=1
print(a)