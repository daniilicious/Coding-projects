todo_list = []

while True:
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
   if choice == "1":
    new_task = input("Enter the task:")
    todo_list.append(new_task)
    print("Adding task")
   elif choice == "2":
    if not todo_list:
      print("Your ToDo list is empty")
    else:
      todo_list.pop(-1)
      print("Removing task")
   elif choice == "3":
    print("Quitting program")
    break
