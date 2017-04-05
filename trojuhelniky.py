# Skrypt č. 1 - trojúhelníky
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a == b and b == c:
    print("Je rovnostranný.")
elif a == b or b == c or a == c:
    print("Je rovnostranný rovnoramenný.")
else:
    if a > b and a > c:
        prepona = a
        odvesna1 = b
        odvesna2 = c
    elif b > a and b > c:
        prepona = b
        odvesna1 = a
        odvesna2 = c
    else:
        prepona = c
        odvesna1 = a
        odvesna2 = b

    if odvesna1**2 + odvesna2**2 == prepona**2:
        print("Je to pravoúhlý trojúhelník.")
    else:
        print("Je pravoúhlý trojúhelník.")
