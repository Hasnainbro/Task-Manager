# Define a function to display the menu and prompt the user for input
def display_menu():
    print("TO-DO LIST MENU")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Exit Program")
    choice = input("Enter your choice (1-4): ")
    return choice

# Define a function to display the tasks in the list
def view_tasks(task_list):
    print("Tasks to be completed:")
    for i, task in enumerate(task_list):
        print(f"{i+1}. {task}")
    print()

# Define a function to add a task to the list
def add_task(task_list):
    task = input("Enter a task: ")
    task_list.append(task)
    print("Task added successfully!")
    print()

# Define a function to mark a task as completed
def mark_task_completed(task_list):
    task_index = input("Enter the number of the completed task: ")
    try:
        task_index = int(task_index) - 1
        if task_index >= 0 and task_index < len(task_list):
            del task_list[task_index]
            print("Task marked as completed successfully!")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    print()

# Define the main function to run the program
def main():
    # Create an empty list to store tasks
    task_list = []

    # Display the menu and prompt the user for input
    choice = display_menu()

    # Loop through the program until the user exits
    while choice != "4":
        if choice == "1":
            view_tasks(task_list)
        elif choice == "2":
            add_task(task_list)
        elif choice == "3":
            mark_task_completed(task_list)
        else:
            print("Invalid choice. Please try again.")
            print()

        # Display the menu and prompt the user for input
        choice = display_menu()

    # Exit the program
    print("Goodbye!")

# Call the main function
if __name__ == "__main__":
    main()
