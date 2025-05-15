myList = ["pomeranač", "jablko", "banan", "mandarinka", "hrozno", "meloun", "švestky"]
print(myList)
print(len(myList))
print(myList[2])
#print(myList[int(input("zadejte pozici"))])
dupList = myList[2:5]
print(myList)
print(dupList)

if "jablko" in myList:
    print("jablko tam je")

myList[-2] = "Samice hrabáče"
print(myList)

myList.append("grep")#přidání veci
print(myList)

myList.insert(1, "ananas")
print(myList)

mylist2 = ["paprika","mrkev", "okurka"]
myList.extend(mylist2)#spolejí 2 listu
print(myList)

myList.remove("ananas")#odstranení
print(myList)

myList.pop(2)
print(myList)

print(mylist2)#čištení
mylist2.clear()
print(mylist2)

del mylist2#smazámí
#print(myList)

for i in myList:#podívá se do listu a jednotlive vypíše vsechny veci v listu 
    print(i)

for i in range(len(myList)):#vypíše určité pozice
    print(i, myList[i])

abeceda =["F", "G", "A", "D", "C"] 
print(abeceda)
abeceda.sort()#sorvá podle abecedy
print(abeceda)

abeceda.sort(reverse=True)#srovná podle abecedy ale pozpátku
print(abeceda)

myList.sort(key=str.lower)#vypíše list + neřeší velký malí písmenka
print(myList)

nums=[1,2,30,56,99,89,44]
print(nums)
nums.sort()
print(nums)

nums.reverse()
print(nums)

mylist2 = myList#vypíšou se stejne
print(myList)
print(mylist2)

mylist2[0] = "rajče"
print(myList)
print(mylist2)

copyList = myList.copy()
copyList[0] = "pistácie"
print(myList)
print(copyList)