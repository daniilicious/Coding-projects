italian_food = ["Spaghetti Amatriciana", "Penne Arrabiata", "Fettuccine Carbonara", "Lasagna", "Pizza Margherita", "Risotto" ]

def find_meal (name, menu):
  if name in menu:
    return name
  else:
    return None
 