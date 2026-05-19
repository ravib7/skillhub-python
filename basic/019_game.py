print("1 Rock")
print("2 Paper")
print("3 Scessior")
print("Please Choose Option 1 or 2 or 3")

player1 = int(input("Enter Your Choice"))
player2 = int(input("Enter Your Choice"))

if(player1 < 1 or player1 > 3 or player2 < 1 or player2 > 3):
    print("Kahi pn type nako karu")

if(player1 == player2):
    print("Match Draw")
elif(player1 == 1 and player2 == 2):
    print("winner player 2")
elif(player1 == 1 and player2 == 3):
    print("winner player 1")
elif(player1 == 2 and player2 == 1):
    print("winner player 1")
elif(player1 == 2 and player2 == 3):
    print("winner player 2")
elif(player1 == 3 and player2 == 1):
    print("winner player 2")
elif(player3 == 3 and player2 == 2):
    print("winner player 2")