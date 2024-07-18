todo_list = ["groceries", "study"]

if not todo_list:
    print("Your ToDo list is empty")
else:
    index = 1
    for task in todo_list:
        print(f"{index}.{task}")
        index += 1   
