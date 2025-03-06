while True:                        #cyklus, který bude probíhat pořád
    cislo = input("Zadejte číslo:")
    if cislo.lstrip("-").isdigit():
       max = int(cislo)
       break                     # vyskočím ven z cyklu  
    else:
        print("nezadali jste číslo: ")

while input("Pro ukončení zadejte pismeno K") != "K":
    cislo = input("zadejte číslo: ")
    if cislo.lstrip("-").isdigit():
        cislo = int(cislo)
        if max < cislo:
            max =  cislo
    else:
        print("nezadali jste číslo: ")

print("nejvetší číslo bylo: " + str(max)) 