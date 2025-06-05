def main():
    cislo1 = int(input("zadejte první číslo"))
    cislo2 = int(input("zadejte druhé číslo"))
    print(cislo1, cislo2)
    print(soucet(cislo1, cislo2))
    print(nasobeni(cislo1, cislo2))
    
def soucet(a, b):
    vysledek = a+ b 
    return vysledek

def nasobeni(a:int, b:int):
    vysledek = 0
    for i in range(b):
        vysledek = soucet(a,vysledek)
        return vysledek
      
main()