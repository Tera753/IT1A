myList = ["pomeranač", "jablko", "banan", "mandarinka", "hrozno", "meloun", "švestky"]
print(myList)
print(len(myList))
print(myList[2])
print(myList[int(input("zadejte pozici"))])
dupList = myList[2:5]
print(myList)
print(dupList)

if "jablko" in myList:
    print("jablko tam je")

myList[-2] = "Samice hrabáče"
print(myList)