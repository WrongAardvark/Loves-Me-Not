import time

no_love = "loves me not"
love = "loves me"


# Start the game.
def start_game():

    # Find out how many petals are in the flower.
    while True:
        flower_petals = input("How many petals are in the flower? ")

        if flower_petals.isnumeric():
            flower_petals = int(flower_petals)
            break  # Exit the loop once a valid number is entered.
        else:
            print("Please use a number...")

    # Counting the petals
    for petal in range(flower_petals):

        # For final petal
        if petal == flower_petals - 1:
            if petal % 2 == 0:
                print(f"{love.upper()}!")
            else:
                print(f"{no_love.upper()}!")
        # For 1st, and all odd numbered, petals
        elif petal % 2 == 0:
            print(love)
        # For 2nd, and all even numbered, petals
        else:
            print(no_love)
        time.sleep(0.75)


start_game()
