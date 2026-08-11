import random


choices = ["rock", "paper", "scissors"]



def main():

    retry = "yes"
    score_user = 0
    score_computer = 0

    while retry == "yes":



        user_decision = input("Choose rock, paper or scissors: ").lower()
        if user_decision not in choices:
            print("invalid option!!")
            return


        program_decision = random.choice(choices)

        result = logic(user_decision, program_decision)

        if result == "user":
            score_user = score_user + 1
        elif result == "computer":
            score_computer = score_computer + 1
        retry = input("want another go?  ")



def logic(user_decision, program_decision):
    if user_decision == program_decision:
        print("it was a draw")
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