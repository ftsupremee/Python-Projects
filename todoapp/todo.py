from time import sleep

# memory with a file with all the tasks that gets loaded every start
def load_tasks(path="tasks.txt"):
    try:
        with open(path, "r") as f:
            tasks = [line.strip() for line in f if line.strip()]
        return tasks
    except FileNotFoundError:
        return []

# save the tasks to the file, rewriting everything
def save_tasks(tasks: list, path: str="tasks.txt"):
    with open(path, "w") as f:
        for task in tasks:
            f.write(task + "\n")
    
def add_task(task: str, tasks: list):
    tasks.append(task)
    print("\nUpdated!")
    show_tasks(tasks)

def remove_task(task_number: int, tasks: list):
    if len(tasks) == 0:
        print("No tasks to remove")
    try:
        tasks.pop(task_number - 1)
        print("Updated!")
        show_tasks(tasks)
    except ValueError:
        # remove raises a ValueError if the element isn't in the given list
        print("Task not in tasks.")
        sleep(1)

def clear_tasks(tasks: list):
    tasks = [] # Setting a list to empty just removes all the tasks inside, clearing it
    show_tasks(tasks)

def show_tasks(tasks: list):
    # showing tasks everytime one is added or removed improves the experience imo so I implemented it into this
    if len(tasks) > 0: # If there are no tasks it's awkward so I made a thing for a special case
        print("Your tasks are:")
        for task in tasks:
            print(task)
        print()
        sleep(1)
    else:
        print("You have no tasks")
    save_tasks(tasks)

def main():
    print("----------------------------------------")
    print("               TODO LIST                ")
    print("----------------------------------------")
    path = "tasks.txt"
    tasks = load_tasks(path=path)

    options = ["1.Add a Task", "2.Complete a Task", "3.Show your tasks", "4.Clear all tasks", "5.Quit"]
    choices_count = len(options)
    options = "\n".join(options) # Making it a string so it's easier. \n joins it to make new lines after every option

    while True:
        choice = int(input(f"\n{options}Choose what to do: "))

        # Allow only valid choices
        if not (1 <= choice <= choices_count):
            print("Invalid choice, try again!\n")
            continue

        match choice:
            case 1:
                task = input("Please enter the title of the task: ")
                add_task(task, tasks)
            case 2:
                show_tasks(tasks)
                task_number = int(input("Please enter the index of the task: "))
                remove_task(task_number, tasks)
            case 3:
                show_tasks(tasks)
            case 4:
                clear_tasks(tasks)
            case _:
                print("Thank you for using todo list")
                break
        

if __name__ == '__main__':
    main()