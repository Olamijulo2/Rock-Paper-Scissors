import random

options = {"R":"ROCK", "P":"PAPER", "S":"SCISSORS"}

name = input("Enter your name: ") .upper()
print(f"Welcome {name.upper()}")
print("")
print("==================================")

gameOn = True
while gameOn:

    computerOption = random.choice(list(options))
    computerOption = options[computerOption]
    playerOption = input("Choose between R / P / S: ") .upper()
    
    

    print("")
    if playerOption in options:
        playerOption = options[playerOption]
        print(f"{name.upper()} ({playerOption}): CPU ({computerOption})")


    else:
        print("Kindly type the correct option")

    if computerOption == playerOption:
            print("")
            print("Tie!")
            print("==================================")
            print("")
            play_again = input ("Play again? (Y / N): ") .upper()
            if play_again != "Y":
                print ("Bye!")
                break

    elif computerOption == options["R"] and playerOption == options["S"] or computerOption == options["S"] and playerOption == options["P"] or computerOption == options["P"] and playerOption == options["R"]:
            print("")
            print("Computer Wins!!!")
            print("==================================")
            print("")
            print ("Bye")
            break

    else:
            print("")
            print(f"{name.upper()} Wins!!!")
            print("==================================")
            print("")
            print ("Bye")
            break

        
    