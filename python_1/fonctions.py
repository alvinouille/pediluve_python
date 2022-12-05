def say_hi(name, age):
    print("Hi user " +name+ ", you are " +str(age))

say_hi(input(""), 45)

def cube(number):
    return (number *3)

print(cube(5))

#CONDITIONS

is_male = True
is_tall = False

if is_male and not (is_tall):
    print("You are a short male")
elif is_male or is_tall :
    print("Haha flemme")
else:
    print("YOU ARE NOTHING!")

# comparaisons :

def max_num(num1, num2, num3):
    if num1 >= num 2 and num1 >= 3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else :
        return num3

print(max_num(1, 2, 3))

def triplenb(nb, multiple=0):
    #si on passe pas de valeur a multiple :
    if multiple == 0:
        newnb = nb*3
    return nb, str(newnb)
    #on peut retourner plusieurs valeurs, a stocker dans
    #plusieurs variables, en les convertissant si besoin


