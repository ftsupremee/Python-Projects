from time import sleep

# memory with a file with all the tasks that gets loaded every start
def load_tasks(path: str="tasks.txt"):
    try:
        with open(path, "r") as f:
            tasks = [line.strip() for line in f if line.strip()]
        return tasks
    except FileNotFoundError:
        return []

# save the tasks to the file, rewriting everything
def save_tasks(tasks: list, path: str="tasks.txt"):
    with open(path, "w") as f:
        if len(tasks) == 0:
            return
        for task in tasks:
            f.write(task + "\n")
    
def add_task(tasks: list):
    task = input("Enter task you want to add: ")
    tasks.append(task)
    print("\nUpdated!")
    show_tasks(tasks)

def remove_task(tasks: list):
    show_tasks(tasks)
    task_number = int(input("Please enter the index of the task: "))

    if len(tasks) == 0:
        print("No tasks to remove")
    try:
        tasks.pop(task_number - 1)
        print("Updated!")
        show_tasks(tasks)
    except IndexError:
        # pop raises a IndexError if the element index isn't in the list
        print("Task index not in tasks.")
        sleep(1)

def show_tasks(tasks: list):
    if len(tasks) > 0: # If there are no tasks it's awkward so I made a thing for a special case
        print("Your tasks are:")
        for task in tasks:
            print(task)
        sleep(1)
    else:
        print("You have no tasks")
    save_tasks(tasks) # as show_tasks() is called in basically every choice

def clear_tasks(tasks: list):
    tasks = [] # Setting a list to empty just removes all the tasks inside, clearing it
    show_tasks(tasks)

def update_task(tasks: list):
    show_tasks(tasks)
    task_number = int(input("Please enter the index of the task: "))
    task = input("Enter what to update it as: ")

    if len(tasks) == 0:
        print("No tasks to edit")
        return
    
    try:
        tasks[task_number - 1] = task
    except IndexError:
        print("Index out of range")
    show_tasks(tasks)



def main():
    print("----------------------------------------")
    print("               TODO LIST                ")
    print("----------------------------------------")
    path = "tasks.txt"
   

    options = ["1.Add a Task", "2.Complete a Task", "3.Show your tasks", "4.Clear all tasks", "5.Edit Task", "6.Quit"]
    choices_count = len(options)
    options = "\n".join(options) # Making it a string so it's easier. \n joins it to make new lines after every option

    while True:
        tasks = load_tasks(path = path)
        choice = int(input(f"\n{options}\nChoose what to do: "))

        # Allow only valid choices
        if not (1 <= choice <= choices_count):
            print("Invalid choice, try again!\n")
            continue

        match choice:
            case 1:
                add_task(tasks)
            case 2:
                remove_task(tasks)
            case 3:
                show_tasks(tasks)
            case 4:
                clear_tasks(tasks)
            case 5:
                update_task(tasks)
            case _:
                print("Thank you for using todo list")
                break
        

if __name__ == '__main__':
    main()