def main():
    while True:   
        tvar = input("S jakým tvarem si přejete pracovat? Čtverec/obdélník/trojúhelník: ").strip().lower()
        if tvar == "čtverec":
            strana = int(input("Zadejte délku strany: "))
            volba = input("Přejete si obsah, nebo obvod? (obsah/obvod): ").strip().lower()
            if volba == "obsah":
                print(f"Obsah čtverce je: {strana ** 2}")
            elif volba == "obvod":
                print(f"Obvod čtverce je: {4 * strana}")
            else:
                print("Špatné zadání, zkuste to znovu.")

        elif tvar == "obdélník":
            a = int(input("Zadejte délku strany a: "))
            b = int(input("Zadejte délku strany b: "))
            volba = input("Přejete si obsah, nebo obvod? (obsah/obvod): ").strip().lower()
            if volba == "obsah":
                print(f"Obsah obdélníku je: {a * b}")
            elif volba == "obvod":
                print(f"Obvod obdélníku je: {2 * (a + b)}")
            else:
                print("Špatné zadání, zkuste to znovu.")

        elif tvar == "trojúhelník":
            a = int(input("Zadejte délku strany a: "))
            b = int(input("Zadejte délku strany b: "))
            c = int(input("Zadejte délku strany c: "))
            if a + b > c and a + c > b and b + c > a:
                print("Lze sestavit trojúhelník.")
            else:              
                    print("Trojúhelník nelze sestavit.")

        else:
            print("Špatné zadání, zkuste to znovu.")
            continue


        pokracovat = input("Chcete pokračovat? Stiskněte Enter pro pokračování, nebo zadejte něco pro ukončení: ")
        if pokracovat != "":
            break

if __name__ == "__main__":
    main()
