from random import randint
computer_win_count , player1_win_count, draw_count, total = 0,0,0,0

print("--------------------------------------")
print("1 Rock")
print("2 Paper")
print("3 Scessior")
print("4 Exit")
print("Please Choose Option 1 or 2 or 3")
print("--------------------------------------")


while True:
    player1 = int(input("Enter Your Choice "))
    computer = randint(1,3)
    total += 1
    print(player1, computer)
    if(player1  == 4):
        break

    print("------------------- winner -------------------")
    match True:
        case _ if player1 == computer:
            print("draw")
            draw_count += 1
        case _ if player1 == 1 and computer == 2:
            print("computer")
            computer_win_count += 1
        case _ if player1 == 1 and computer == 3:
            print("player 1")
            player1_win_count += 1
        case _ if player1 == 2 and computer == 1:
            print("player 1")
            player1_win_count += 1
        case _ if player1 == 2 and computer == 3:
            print("computer")
            computer_win_count += 1
        case _ if player1 == 3 and computer == 1:
            print("computer")
            computer_win_count += 1
        case _ if player1 == 3 and computer == 2:
            print("player 1")
            player1_win_count += 1
        case _ :
            print("invalid choice")

    print(f"Total: {total} | Draw: {draw_count} | Computer: {computer_win_count} | You: {player1_win_count}")
    print("------------------- Winner -------------------")