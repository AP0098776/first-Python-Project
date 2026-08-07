import random


choices = ["rock", "paper", "scissors"]



def main():

    retry = "yes"

    while retry == "yes":



        user_decision = input("Choose rock, paper or scissors: ").lower()
        if user_decision not in choices:
            print("invalid option!!")
            return


        program_decision = random.choice(choices)

        logic(user_decision, program_decision)
        retry = input("want another go?  ")


def logic(user_decision, program_decision):
    if user_decision == program_decision:
        print("it was a draw")
    elif user_decision == "rock" and program_decision == "paper":
        print("computer wins!!")
    elif user_decision == "paper" and program_decision == "scissors":
        print("computer wins")
    elif user_decision == "paper" and program_decision == "rock":
        print("you win!!")
    elif user_decision == "scissors" and program_decision == "paper":
        print("you win!!")
    elif user_decision == "scissors" and program_decision == "rock":
        print("computer wins!!")
    elif user_decision == "rock" and program_decision == "scissors":
        print("you win!!")









main()