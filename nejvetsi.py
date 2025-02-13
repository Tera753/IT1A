max = 0
for i in range(10):
    print("zadejte číslo")
    cislo =  int(input())
    if cislo > max:
        max = cislo
print("nejvetší zadané číslo bylo: " + str(max))
