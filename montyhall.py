import random

win = 0
lose = 0

iteration = int(input("Zadejte počet opakování které chcete simulovat"))
for i in range(iteration):
    print(i)
    car = random.randint(1,3)
    playerChoice = random.randint(1,3)
    while True:
        montysChoice= random.randint(1,3)
        if montysChoice != car and montysChoice != playerChoice:
            break
    #print(car, playerChoice, montysChoice)
    playerOld = playerChoice   
    while True:
        playerChoice = random.randint(1,3)
        if playerChoice != montysChoice and playerChoice != playerOld:
            break
    if playerChoice == car:
        win += 1
    else:
        lose += 1
print(f"Hráč prohrál v {lose} případech a zvítězil v {win} případech \nto znamená že zvítezil v {(win/iteration)*100} % případů a prohrál v {(lose/iteration)*100} %případu.")