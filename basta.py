# Classes
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name 
    self.items = items 
    self.start_time = start_time 
    self.end_time = end_time

  def __repr__(self):
    return f"{self.name} menu available from {self.start_time} to {self.end_time}"

  def calculate_bill(self, purchased_items):
    bill = [self.items[i] for i in purchased_items]
    return sum(bill)

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address

  def available_menus(self, time):
    result = []
    for i in self.menus:
      if time > i.start_time and time < i.end_time:
        result.append(i.name)
    return result

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

# Instantiation
brunch = Menu("Brunch", {}, 1100, 1600)
brunch.items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
early_bird = Menu("Early Bird", {}, 1500, 1800)
early_bird.items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
dinner = Menu("Dinner", {}, 1700, 2300)
dinner.items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
kids = Menu("Kids", {}, 1100, 2100)
kids.items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepas_menu = Menu("Arepas", {}, 1000, 2000)
arepas_menu.items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)
arepa = Business("Take a' Arepa", arepas_place)

# Class calls
print(dinner)
print(brunch.calculate_bill(["pancakes", "home fries", "coffee"]))
print(early_bird)
print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))
print()
print(flagship_store)
print(flagship_store.available_menus(1200))
print(new_installment.available_menus(1700))
print()
print(arepa.franchises)
print(arepa.franchises.menus)
print(arepa.franchises.menus.calculate_bill(['arepa pabellon', 'guayanes arepa']))
