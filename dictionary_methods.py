WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}
ANS = WORDS.copy()

def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} left!")
        guess = input("Guess a word: ")

        if guess == "GRAPHIC":
            WORDS.clear() # .clear() removes all items (key-value pairs) from a dictionary
            print("You've won!")

        elif guess in WORDS.keys(): # Loop over each key, .key() returns every key in the dictionary
            points = WORDS.pop(guess) # .pop("key", "default") removes a specified key from a dictionary and returns its corresponding value.
            print(f"Good job! You scored {points} points.")

    print("That's the game!")

    print("=" * 50)
    print("Welcome to Spelling Bee!")
    print("Here are yesterday's answers:")

    for word, points in ANS.items(): # returns a dynamic view object containing the key-value pairs of a dictionary as a list of individual tuples
        print(f"{word} was worth {points} points.")


main()