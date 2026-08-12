import random


choices = ["rock", "paper", "scissors"]
menu_choices = ["1", "2", "3"]
retry_choices = ["yes", "no"]





def main():
    retry = "yes"




    while True:



        print("Rock Paper Scissors Game")
        print("1. Play Game (1) ")
        print("2. Show score (2)")
        print("3. Quit Game (3)")
        menu_option = input("choose an option: ")

        if menu_option not in menu_choices:
            print("please choose a valid option (1, 2, 3)")
            continue

        if menu_option == "3":
            break
        elif menu_option == "1":
            score_user = 0
            score_computer = 0
            retry = "yes"
        elif menu_option == "2":
            print(f"User score:, {score_user}")
            print(f"computer score:, {score_computer}")
            continue









        while retry == "yes":



            user_decision = input("Choose rock, paper or scissors: ").lower()
            if user_decision not in choices:
                print("invalid option!!")
                continue


            program_decision = random.choice(choices)

            result = logic(user_decision, program_decision)

            if result == "user":
                score_user = score_user + 1
                print("you won!!")
            elif result == "computer":
                score_computer = score_computer + 1
                print("the computer won, better luck next time!!")
            elif result == "draw":
                print("it was a draw!!")

            retry = input("want another go?  ")


            while retry not in retry_choices:
                retry = input("want another go?  ")

                if retry not in retry_choices:
                    print("not a valid option!! ")






def logic(user_decision, program_decision):
    if user_decision == program_decision:
        return "draw"
    elif user_decision == "rock" and program_decision == "paper":
        return "computer"
    elif user_decision == "paper" and program_decision == "scissors":
        return "computer"
    elif user_decision == "paper" and program_decision == "rock":
        return "user"
    elif user_decision == "scissors" and program_decision == "paper":
        return "user"
    elif user_decision == "scissors" and program_decision == "rock":
        return "computer"
    elif user_decision == "rock" and program_decision == "scissors":
        return "user"















main()