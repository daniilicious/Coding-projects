italian_food = ["Spaghetti Amatriciana", "Penne Arrabiata", "Fettuccine Carbonara", "Lasagna", "Pizza Margherita", "Risotto" ] #food menu

def find_meal (name, menu): #checks if meal exist in menu
  if name in menu:
    return name
  else:
    return None

def select_meal (name): #meal choosen
  return find_meal(name, italian_food) 

def display_available_meals(): #shows food available
  print("Available Italian Meals:")
  for meal in italian_food:
    print(meal)

def create_summary(name, amount): #order summary if found
  order = select_meal(name)
  if order:
    return f"You ordered {amount} {name}"
  else:
    return "Meal not found"

print("Welcome to the Food Order System!")
display_available_meals()