italian_food = ["spaghetti amatriciana", "penne arrabiata", "fettuccine carbonara", "lasagna", "pizza margherita", "risotto" ] #food menus
indian_food = ["veggie samosa", "tandoori chicken", "mutter paneer", "chicken tikka masala", "mutton korma", "naan"]
def find_meal (name, menu): #checks if meal exist in menu
  if name in menu:
    return name
  else:
    return None

def select_meal (name, food_type): #meal choosen
  if food_type.lower() == "italian":
    return find_meal(name, italian_food) 
  elif food_type.lower() == "indian":
    return find_meal(name, indian_food) 
  else:
    return None 

def display_available_meals(food_type): #shows food available in each menu
  if food_type == "italian":
    print("Available Italian Meals:")
    for meal in italian_food:
      print(meal)
  elif food_type == "indian":
    print("Available Indian Meals:")
    for meal in indian_food:
      print(meal)
  else:
    print("Invalid food type")
def create_summary(name, amount, food_type): #order summary if found
  order = select_meal(name, food_type)
  if order:
    return f"You ordered {amount} {name}"
  else:
    return "Meal not found"

print("Welcome to the Food Order System!")
type_input = input("Choose the type of cuisine: ")
display_available_meals(type_input)
name_input = input("Please enter your meal choice: ")
amount_input = int(input("Please enter your order quantity:"))
result = create_summary(name_input, amount_input, type_input)
print(result)