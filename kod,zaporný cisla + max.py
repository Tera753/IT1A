max = input("zadejte číslo.")
for i in range(9):
    cislo = input("zadejte číslo. ")
    if cislo > max:
        max = cislo 
print("nejvetší zadané číslo bylo" + str(max))