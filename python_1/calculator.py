print("welcome to the new calculator on the market !")
n1 = input("Number 1 : ")
op = input("\n+, -, /, *, % ? ")
n2 = input("\nNumber 2 : ")
if op == "+":
    print(int(n1)+int(n2))
elif op == "-" :
    print(int(n1) - int(n2))
elif op == "*" :
    print(int(n1) * int(n2))
elif op == "/":
    print(int(n1) / int(n2))
elif op == "%":
    print(int(n1) % int(n2))
else :
    print("ERROR")