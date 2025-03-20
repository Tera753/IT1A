#end = int(input("zadejte číslo jehož faktoriál chcete."))
#while end < 0:
    # end = int(input("zadejte číslo jehož faktoriál chcete"))
while True:
    end = int(input("zadejte faktoriál jehož číslo chcete"))
    if end>=0:
        break
    else:
        print("zadejte to pořádně!")

faktorial = 1
for i in range(1, end+1):
    faktorial *= i
    print(faktorial)
