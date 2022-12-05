t = "slKDIEJmop45;;"
a = 0
b = 0
c= 0
d = 0

for i in t:
    if i.isdigit():
        c += 1
    elif i.isalpha():
        if i.islower():
            a += 1
        else:
            b += 1
    else:
        d += 1
res = str(a) + str(b) + str(c) + str(d)

print(res.replace("0", ""))