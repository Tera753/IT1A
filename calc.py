while True:
    clen1 = int(input("zadejte první číslo"))
    clen2 = int(input("zadejte druhé číslo"))
    """
    print("1. Součet")
    print("2. Součin")
    print("3. Rozdíl")
    print("4. Podíl")
    """
    print("1. Součet\n2. Součin\n3. Rozdíl \n4. Podíl")

    operace = int(input("Vyverte číslo početní operace, kterouz chcete."))

    match operace:
        case 1:
              soucet = clen1 + clen2
              print("Součet je: " + str(soucet))
        case 2:
              soucin = clen1 * clen2
              print("soucin je: " + str(soucin))
        case 3:
              rozdíl = clen1 - clen2
              print("rozdíl je: " + str(rozdíl))
        case 4:
            if clen2 == 0 :
                print("nelze delit 0")
            else:
                podil = clen1 / clen2
                print("podil je : " + str(podil))
        case _:
              print ("takovou operaci nemáme! ")

              

    konec = input ("přejete si ukoncit program? Y/N")
    if konec == "Y" or konec == "y" :
        break
    elif konec == "N" or konec == "n":
         print("jdeme na další výpočet")
    else:
         print("neplatné zadání, program se hroutí")
         break
    