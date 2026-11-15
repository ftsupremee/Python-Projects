# URL Shortener (very simple version): Takes a long URL and creates a short code that maps back to it (store the mapping in a file)
# we get a shortened url, we return a random word (maybe use a 5 letter string from password generator) and map it to the larger file

import csv
import string
import random

def save_url_mapping(short_url: str, long_url: str) -> None:
    path = "url_maps.csv"
    with open(path, mode = "a", newline = "", encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([short_url, long_url])
    print("Succesfully saved to file")

def shorten_url(base_url: str, long_url: str) -> str:
    # generate a random sequence of characters and slice out first 6 
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%-._"

    all_characters = list(lowercase_letters + uppercase_letters + digits + symbols)
    random.shuffle(all_characters)
    new_key = "".join(all_characters)

    shortened_url = new_key[:6]

    # save it to a file to retrieve later on
    save_url_mapping(shortened_url, long_url)
    return base_url + shortened_url + "\n"

def expand_url(base_url: str, short_url: str) -> str:
    url_relations = load_urls()
    return url_relations[short_url] + "\n" if short_url in url_relations else "No record of that short url found sorry. :("

def load_urls() -> dict[str, str]:
    with open("url_maps.csv", "r", newline = "", encoding = "utf-8") as f:
        reader = csv.reader(f)
        next(reader)

        short_url, long_url = list(zip(*reader))[:2]

    url_relations = dict(zip(short_url, long_url))
    return url_relations

def main() -> None:
    width = 40
    print("-" * width)
    print("URL Shortener".center(width))
    print("-" * width)

    base_url = input("Enter the base URL: ") + "/"
    options = ["1.Shorten a URL",
               "2.Expand a shortened URL",
               "3.Show all shortened URLS with expanded versions",
               "4.Quit"]
    options = "\n".join(options)

    while True:
        choice = int(input(f"{options}\nChoose what to do: "))
        match choice:
            case 1:
                long_url = input("Enter the url to shorten: ")
                print(shorten_url(base_url, long_url))
            case 2:
                short_url = input("Enter the url to expand: ")
                print(expand_url(base_url, short_url))
            case 3:
                print(f"The URLs are\n{load_urls()}\n")
            case 4:
                print("Thank you for using this URL shortener")
                break
            case _:
                print("Not a valid choice\n")
                continue
        
if __name__ == "__main__":
    main()