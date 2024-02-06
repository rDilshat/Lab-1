import random

def randomnum():
    random.randint(1, 20)

def main():
    number = randomnum()
    print("Hello! What is your name?")
    name = str(input())
    print("Well,", name, end=", I am thinking of a number between 1 and 20.")
    print()
    print("Take a guess.")
    attempt = int(input())
    count = 1
    while(attempt != number):
        print("Your guess is too low.")
        print("Take a guess.")
        attempt = int(input())
        if(attempt == number):
            break
        count+=1
        break

    print("Good job,", name, end="! You guessed my number in " + str(count) + " guesses!")
main()