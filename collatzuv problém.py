num = int(input("zadejte prirozené číslo"))
counter = 0

while num != 1:
    if num%2 == 0:
        num = num / 2
    else:
        num = (num * 3) + 1
    counter += 1
    print(num)

print("Pro vyřešení problému bylo potřeba " + str(counter) + "kroku.")