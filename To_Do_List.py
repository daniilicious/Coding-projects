todo_list = ["groceries", "study"]

while True:
   new_task = input("Enter the task:")
   todo_list.append(new_task)
   print(f"Task {new_task} added successfully")

   if not todo_list:
      print("Your ToDo list is empty")
   else:
    index = 1
    for task in todo_list:
        print(f"{index}. {task}")
        index += 1 
   print("Options:")
   print("1) Add a task")
   print("2) Remove a task")
   print("3) Quit the program")

   choice = input("Choose a number from the menu: ")
   break