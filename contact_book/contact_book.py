import json

path = "contact_book.json"

def save_data(data: list[dict[str, str]]) -> str:
    try:
        with open(path, "w", encoding="UTF-8", newline="") as f:
            json.dump(data, f, indent = 4) # append the data
        return "Successfully saved"
    except (FileNotFoundError, json.JSONDecodeError):
        return "An error occurred. Could not save"

def add_contact(first_name: str, last_name: str, number: str) -> str:
    data = load_contacts()
    data.append({"First Name": first_name, "Last name": last_name, "Number": number})
    return save_data(data)
        
def load_contacts() -> list[dict[str, str]]:
    try:
        with open(path, "r", encoding="UTF-8") as f:
            data = json.load(f) # loads the stats from the json file
    except (FileNotFoundError, json.JSONDecodeError):
        data = []  # set it to an empty dictionary if error occurs
    return data

def search_contact(first_name: str, last_name: str) -> str:
    contacts = load_contacts()

    same_name = [contact["Number"] for contact in contacts if contact["First Name"] == first_name and contact["Last name"] == last_name]
    return f"The people with the same first and last name have the number(s) {same_name}"

def delete_contact(first_name: str, last_name: str, number: str) -> str:
    data = load_contacts()
    
    new_data = [contact for contact in data if not(
        contact["First Name"] == first_name and
        contact["Last name"] == last_name and
        contact["Number"] == number
    )]

    if len(data) == len(new_data):
        return "No such contact"

    saved = save_data(new_data)
    if saved == "An error occurred. Could not save":
        return saved
    return "Deleted"
    

def main():
    width = 30
    print("-" * width)
    print("CONTACT BOOK".center(width))
    print("-" * width)

    options = "\n".join(["1.Add a contact",
               "2.Search for a contact",
               "3.Delete a contact",
               "4.View all contacts",
               "5.Quit"])
    

    while True:
        choice = int(input(f"\n{options}\nChoose what to do: "))

        match choice:
            case 1:
                first_name = input("Enter their first name: ")
                last_name = input("Enter their last name: ")
                number = input("Enter their number: ")
                add_contact(first_name, last_name, number)
            case 2:
                first_name = input("Enter their first name: ")
                last_name = input("Enter their last name: ")
                print(search_contact(first_name, last_name))
            case 3:
                first_name = input("Enter their first name: ")
                last_name = input("Enter their last name: ")
                number = input("Enter their number: ")
                print(delete_contact(first_name, last_name, number))
            case 4:
                print(load_contacts())
            case 5:
                print("Thank you for using our program")
                break
            case _:
                print("Invalid option\n")
                continue

if __name__ == "__main__":
    main()
