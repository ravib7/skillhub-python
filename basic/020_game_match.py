print("1 Rock")
print("2 Paper")
print("3 Scessior")
print("Please Choose Option 1 or 2 or 3")

player1 = int(input("Enter Your Choice"))
player2 = int(input("Enter Your Choice"))

match True:
    #   👇 _ walidcard
    case _ if player1 == player2: 
        print("draw")
    case _ if player1 == 1 and player2 == 2:
        print("player 2")
    case _ if player1 == 1 and player2 == 3:
        print("player 1")
    case _ if player1 == 2 and player2 == 1:
        print("player 1")
    case _ if player1 == 2 and player2 == 3:
        print("player 2")
    case _ if player1 == 3 and player2 == 1:
        print("player 1")
    case _ if player1 == 3 and player2 == 2:
        print("player 1")
    case _ :
        print("invalid choice")