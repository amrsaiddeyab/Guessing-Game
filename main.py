# My First Python Project (2026-3-10 / Tuesday)

import random
import sys

def string_validation(playing_type):
    while True:
        playing_type = playing_type.lower()

        if playing_type in ('no','yes'):
            return playing_type
          
        print("You must type 'No' or 'yes'")

        playing_type = input("For playing with me enter ('Yes'), for playing with frined enter('No'): ")

def name_validation(name):
    while True:
        if name.isalpha():
            return name
        
        print("You must enter letters only")
        
        name = input("Please enter your name: ")

def digit_validation(number):
    while True:
        if number.isdigit():
            return int(number)
        
        else:
            print("You must enter numbers, and they must be positive.")

        number = input("enter the number again: ")

def number_in_range_validation(target, number, t):
    while True:
        if t == 'e':
            if target > number :
                print("You can not choose number bigger than the number that represents the ending of the guessing range")
                    
                number = digit_validation(input("Enter the number that represents the ending of the guessing range: "))

            else :
                return number
                 
        else:
            if target < number:
                print("You can not choose number smaller than the number that represents the starting of the guessing range")

                number = digit_validation(input("Enter the number that represents the beginning of the guessing range: "))

            else:
                return number 

def number_validation (number, previous, startnig, ending, guessor=0):
    while True:
            try:
                number = int(number)
                if startnig <= number <= ending:

                    if number not in previous:
                        return number
                    
                    else:
                        print(f"You guessed {number} already before, try choose another number")
                
                else:
                    print(f"Invalid input, it must be between {startnig} and {ending}.")

            except ValueError:
                print("Invalid input, it must be only numbers.")

            if guessor != 0:
                number = input(f"{guessor}, Please enter a number: ")
                continue

            number = input("Please enter a number: ")

def difficult_validation(difficulty):
    while True:
        if difficulty.isdigit():
            d = int(difficulty)

            if d == 1:
                return 100, 10
            
            elif d == 2:
                return 250, 7
            
            elif d == 3:
                return 500, 5
                
        elif difficulty.isalpha():
            d = difficulty.lower()

            if d == "normal":
                return 100, 10
            
            elif d == "hard":
                return 250, 7
            
            elif d == "extreme":
                return 500, 5

        print("you must type (1, 2, 3) or (Normal, Hard, Extreme)")
        difficulty = input("Please Choose the difficulty level: ")

def random_generate(r) :
    return random.randint(0, r)
    
def checker (number, target) :
    diff = target - number

    if diff == 0:
        hint = "correct!"

    elif 0 < diff <= 10:
        hint = "Low"

    elif 10 < diff:
        hint = "Too low"

    elif -10 <= diff < 0:
        hint = "High"

    else:
        hint = "Too high" 

    return hint

def matching(previous, number, hint, target, trying, starting, ending):
    previous.append(number)

    while hint != "correct!":
        print(hint)

        trying = attempts(trying)

        if trying <= 0:
            return 0
        
        print(f"Remaining attempts: {trying}")

        number = input("Please enter a number: ")
        number = number_validation(number, previous, starting, ending)

        hint = checker(number, target)

        previous.append(number)
        
    return trying

def attempts(trying):
    return trying -1     

def again_validation():
    again = input("Do you want to play again? ('yes' or 'no') ")

    while True:
        again = again.lower()
        if again in ('yes', 'no'):
            if again == 'yes':
                main()
    
            else:
                print("See you!")
                sys.exit()

        else:
            print("You must type 'yes' or 'no'")

        again = input("Do you want to play again? ('yes' or 'no') ")

# Main
def main():
    print("Welcome to the guessing game!")
    print("Do you want to play with me or with your friend?")

    playing_type = string_validation(input("For playing with me enter ('Yes'), for playing with friend enter('No'): "))

    if playing_type == 'no':
        print("The person who will choose the number: ")
        chooser = name_validation(input("Please enter your name: "))

        print("The person who will try to guess the number: ")
        guessor = name_validation(input("Please enter your name: "))

        print(f"Ok, now {chooser} will choose the number that {guessor} will try to guess!")
        print("Good luck!")

        print(f"Please {guessor}, close your eyes..")

        target = digit_validation(input(f"Ok {chooser}, what is the number? "))

        starting_range = digit_validation(input("Enter the number that represents the beginning of the guessing range: "))
        starting_range = number_in_range_validation(target,starting_range, 's')

        ending_range = digit_validation(input("Enter the number that represents the ending of the guessing range: "))
        ending_range = number_in_range_validation(target,ending_range, 'e')

        setting_attempts = digit_validation(input(f"How many attempts you want to give it to {guessor}? "))

        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n" * 100)
        
        print(f"Ok {guessor}, open your eyes now and lets start the game!")

        previous = []

        number = input(f"{guessor}, Please enter a number: ") #getting the number from the user
        number = number_validation(number, previous, starting_range, ending_range, guessor)

        hint = checker(number, target)

        trying = setting_attempts

        remain = matching(previous, number, hint, target, trying, starting_range, ending_range)

        if remain > 0:
            print("correct!")
            print(f"You guessed the number in {setting_attempts-remain} attempts! It was {target}.")
            print(f"Your attempts were: {previous}")

            again_validation()

        else :
            print(f"GAME OVER!!\nYour attempts are over!!\nIt was {target}.")

            again_validation()

    else :

        print("1-Normal: (0-100) 10 attempts\n2-Hard: (0-250) 7 attempts\n3-Extreme: (0-500) 5 attempts")
        ran, attempt = difficult_validation(input("Please choose the difficulty level: "))

        print(f"You have {attempt} attempts to guess the number.\nGood luck!")
        trying = attempt
        previous = [] 

        target = random_generate(ran)

        number = input("Please enter a number: ") #getting the number from the user
        number = number_validation(number, previous, 0, ran)

        hint = checker(number, target)

        remain = matching(previous, number, hint, target, trying, 0, ran)

        if remain > 0:
            print("correct!")
            print(f"You guessed the number in {attempt-remain} attempts! It was {target}.")
            print(f"Your attempts were: {previous}")

            again_validation()

        else :
            print(f"GAME OVER!!\nYour attempts are over!!\nIt was {target}.")
            
            again_validation()
            
if __name__ == "__main__":
    main()