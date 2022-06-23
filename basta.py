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

brunch = Menu("Brunch", {}, "11am", "4pm")
brunch.items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

early_bird = Menu("Early Bird", {}, "3pm", "6pm")
early_bird.items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

dinner = Menu("Dinner", {}, "5pm", "11pm")
dinner.items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

kids = Menu("Kids", {}, "11am", "9pm")
kids.items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

print(dinner)
print(brunch.calculate_bill(["pancakes", "home fries", "coffee"]))
print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))
print()

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address

  def available_menus(self, time):
    result = []
    if time 

flagship_store = Franchise("1232 West End Road", ["brunch", "early_bird", "dinner", "kids"])
new_installment = Franchise("12 East Mulberry Street", ["brunch", "early_bird", "dinner", "kids"])

print(flagship_store)
