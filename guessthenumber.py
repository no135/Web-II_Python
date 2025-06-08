import random
def main():
    number = random.randint(1,100)
    print("guess the number game")
    
    while True:
        guess = int(input("Enter the guess: "))

        if guess < 1 or guess > 100:
            print("please guess the number between 1 and 100")
        elif guess < number:
            print("the number is higher")
        elif guess > number:
            print("the number is lower")
        else:
            print(f"you guessed it right") 
            break


if __name__ == "__main__":
    main()    
    