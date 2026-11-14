# Password Generator: Generate random passwords with options (length, include numbers/symbols)

import string
import csv
import random

def generate_password(site: str, username: str, length: int = 12) -> str:
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%-._"

    all_characters = list(lowercase_letters + uppercase_letters + digits + symbols)
    random.shuffle(all_characters)
    new_key = "".join(all_characters)

    if length >= len(new_key):
        return "Too many characters"

    password = new_key[:length]
    save_password(site, username, password)
    return f"Your password for {site} with the account {username} is:\n{password}"

def save_password(website: str, account: str, password: str) -> None:
    with open("passwords.csv", mode = "a", newline='', encoding='utf-8') as f: 
        # we use append instead of write because we won't need to rewrite everything
        writer = csv.writer(f)
        # the format is website, account, password so we will follow that
        writer.writerow([website, account, password]) # needs to be a list
    print("Succesfully saved")

def load_passwords(all: bool = True) -> list:
    with open('passwords.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
    
        # Unpacks the first three columns into separate tuples
        website, account, password = list(zip(*reader))[:3]

    credentials = list(zip(website, account, password))
    if all:
        return credentials
    count = int(input("How many credentials from start: "))
    return credentials[:count]

def search_for_password(website: str, username: str):
    with open('passwords.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
    
        # Unpacks the first three columns into separate tuples
        site, acc, password = list(zip(*reader))[:3]

    for i in range(len(site)):
        if site[i] == website:
            if acc[i] == username:
                return password[i]


def main():
    print("----------------------------------------")
    print("           PASSWORD GENERATOR")
    print("----------------------------------------")

    # list of all actions a user can do
    choices = ["1.Create a new password",
               "2.Search for a specific password",
               "3.Save a password",
               "4.See passwords",
               "5.Quit"]
    choices = "\n".join(choices) # easier while taking input

    while True:
        choice = input(f"\n{choices}\nChoose what to do: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Please enter an integer")
            continue

        match choice:
            case 1:
                website = input("Enter the site: ")
                username = input("Enter username in that site: ")
                length = int(input("Enter length of password: "))
                password  = generate_password(website, username, length)
                print(password)

            case 2:
                website = input("Enter the site: ")
                username = input("Enter username in that site: ")
                print(search_for_password(website, username))

            case 3:
                website = input("Enter the site: ")
                username = input("Enter username in that site: ")
                password = input("Enter the password: ")
                (save_password(website, username, password))

            case 4:
                all = bool(input("Do you want to see all passwords(Click enter without typing anything for no): "))
                print(load_passwords(all))

            case 5:
                print("Thank you for using our password manager")
                break

            case _:
                print("Not a valid range")
                continue
            
if __name__ == "__main__":
    main()