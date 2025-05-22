#jak dat na konec listu číslo a prohodit hodnoty
myList=list(range(1,11))
print(myList)

pos= 2 
while pos+1 <len(myList):
    myList[pos], myList[pos+1] = myList[pos+1],myList[pos]
    pos += 1
    print(myList)

    