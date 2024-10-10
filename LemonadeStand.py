# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 10/09/2024
# Description: Writing code for recording the menu items and daily sales of a lemonade stand.
class InvalidSalesItemError(Exception):
    pass

class MenuItem:

    def __init__(self, name, wholesale_cost, selling_price):
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self):
        return self._name

    def get_wholesale_cost(self):
        return self._wholesale_cost

    def get_selling_price(self):
        return self._selling_price

class SalesForDay:

    def __init__(self, day, sales_dict):
        self._day = day
        self._sales_dict = sales_dict

    def get_day(self):
        return self._day

    def get_sales_dict(self):
        return self._sales_dict

class LemonadeStand:

    def __init__(self, name):
        self._name = name
        self._current_day = 0
        self._menu = {}  # dictionary of MenuItem objects
        self._sales_record = []  # list of SalesForDay objects

   def get_name(self):
        return self._name

   def add_menu_item(self, menu_item):
       self._menu[menu_item.get_name()] = menu_item

    def enter_sales_for_today(self, sales_dict):
        for item in sales_dict:
            if item not in self._menu:
                raise InvalidSalesItemError(f"'{item}' not in the menu")

        sales_for_today = SalesForDay(self._current_day, sales_dict)
        self._sales_record.append(sales_for_today)
        self._current_day += 1

    def sales_of_menu_item_for_day(self, day, item_name):
        if day < len(self._sales_record):
            sales_dict = self._sales_record[day].get_sales_dict()
            return sales_dict.get(item_name, 0)
        return 0

    def total_sales_for_menu_item(self, item_name):
        total_sales = 0
        for sales_day in self._sales_record:
            sales_dict = sales_day.get_sales_dict()
            total_sales += sales_dict.get(item_name, 0)
        return total_sales

    def total_profit_for_menu_item(self, item_name):
        total_sales = self.total_sales_for_menu_item(item_name)
        if item_name in self._menu:
            item = self._menu[item_name]
            profit_per_item = item.get_selling_price() - item.get_wholesale_cost()
            return total_sales * profit_per_item
        return 0

    def total_profit_for_stand(self):
        total_profit = 0
        for item_name in self._menu:
            total_profit += self.total_profit_for_menu_item(item_name)
        return total_profit

# Main function
def main ():
    stand = LemonadeStand('VH Lemons stand')

# add menu items
    item1 = MenuItem('iced lemonade', 0.5, 1.5)
    item2 = MenuItem('water bottle', 0.25, 1)
    item3 = MenuItem('icecream ', 1, 3)
    stand.add_menu_item(item1)
    stand.add_menu_item(item2)
    stand.add_menu_item(item3)

# Sales dictionary
    day_0_sales = {'iced lemonade': 5, 'water bottle': 2, 'not_in_the_menu ': 1}

# Try/except block for invalid sales
    try:
    stand.enter_sales_for_today(day_0_sales)
   print(f"lemonade profit = {stand.total_profit_for_menu_item('iced lemonade')}")
