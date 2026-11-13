# Computer picks a number, you guess. Track attempts and save best scores.
import json
import statistics
from random import randint
from math import log2

file_path = "stats.json"

def record_stats(number:int, guess_count: int, lower: int, higher: int): # record stats to a json file
    try:
        with open(file_path, "r", encoding="UTF-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data =[]

    data.append({"number": number, "count": guess_count})

    with open(file_path, "w", encoding="UTF-8") as f:
        json.dump(data, f, indent=4) # rewrite the stats with the new game's stats

def guessing():
    minimum = int(input("Enter lower bound: "))
    maximum = int(input("Enter upper bound: "))
    random_number = randint(minimum, maximum)

    guess = 0
    guess_count = 0
    while guess != random_number:
        guess = int(input(f"Enter a number between {minimum} and {maximum} inclusive: "))
        if guess < random_number:
            print("Higher")
        elif guess > random_number: # else would print lower even if it is correct
            print("Lower")
        guess_count += 1
    print("Correct")
    record_stats(random_number, guess_count, minimum, maximum)

def show_stats(): # load stats from a json file and print
    try:
        with open(file_path, "r", encoding="UTF-8") as f:
            data = json.load(f) # loads the stats from the json file
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}  # set it to an empty list if error occurs

    numbers = []
    counts = []
    accuracies = []

    for stat in data:
        number = stat["number"]
        count = stat["count"]
        minimum = stat["minimum"]
        maximum = stat["maximum"]
        ideal_guess_count = log2(maximum - minimum + 1)
        accuracy = (ideal_guess_count / count) if count < ideal_guess_count else 100

        numbers.append(number)
        counts.append(count)
        accuracies.append(accuracy)

        print(f"Number: {number}, Count: {count}, Lower Bound: {minimum}, Higher Boud: {maximum}")

    # print useful stats
    most_common_number = statistics.multimode(numbers)
    most_common_guess_count = statistics.multimode(counts)
    average__guess_count = statistics.mean(counts)
    average_accuracy = statistics.mean(accuracies)
    median_guess_count = statistics.median(counts)
    total_guesses = sum(counts)


    print(f"Most common number: {most_common_number}")
    print(f"Most common number of guesses: {most_common_guess_count}")
    print(f"Average guess count: {average__guess_count:.2f}")
    print(f"Your average accuracy was {average_accuracy}")
    print(f"Your median guess count was {median_guess_count}")
    print(f"You took {total_guesses} total guesses.")

def main():
    print("------------------------------")
    print("-----Number Guessing Game-----")
    print("------------------------------")
    while True:
        choice = input("\n1.Play Guessing Game\n2.See Stats\nChoose what you want to do: ")

        # if the user enters a string, it raises a valueerror which stops the program so I added exception handling
        try:
            choice = int(choice)
        except ValueError:
            print("Please enter an integer")
            continue

        if not 1 <= choice <= 2:
            print("Invalid option.")
            continue

        if choice == 1:
            guessing()
        elif choice == 2:
            show_stats()

if __name__ == "__main__":
    main()