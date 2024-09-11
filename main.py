# This project is to replicate the classic "loves me, loves me not" game.
# Given a certain amount of petals, return "loves me" or "loves me not" in order.
# The final petal should output "LOVES ME" in all-caps.

# REMEMBER: 1. first phrase is always "loves me" 2. return a string.

no_love = "loves me not"
love = "loves me"


# Start the game.
def start_game():

    # Find out how many petals are in the flower.
    # *Need to fix error later*
    # *Need to provide error message if a string it input*
    flower_petals = int(input("how many petals are in the flower? "))

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


start_game()
