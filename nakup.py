# Doma
nakup = []
for i in range(10):
    nakup.append(input())
    
print("běž na nákup!")

# V obchodě
print("---OBCHOD---")

for i in range(len(nakup)):
    zbozi = input("> ")

    if zbozi in nakup:
        print("OK")
        nakup.remove(zbozi)
    else:
        print("Měl jsi ale koupit něci jiného.")
