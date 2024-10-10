# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 10/09/2024
# Description: Writing code for recording the menu items and daily sales of a lemonade stand.
'''create a class for invalid sales item error'''
class InvalidSalesItemError(Exception):
    pass

'''create a class for menu item'''
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

'''create a class for sales for day'''
class SalesForDay:
    def __init__(self, day, sales_dict):
        self._day = day
        self._sales_dict = sales_dict

    def get_day(self):
        return self._day

    def get_sales_dict(self):
        return self._sales_dict

'''create a class for Lemon Stand'''
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
        for item in sales_dict():
            if item not in self._menu:
                raise InvalidSalesItemError(f"'{item}' not in the menu")

        self._sales_record.append(SalesForDay(self._current_day, sales_dict.copy()))
        self._current_day += 1

    def sales_of_menu_item_for_day(self, day, item_name):
        for record in self._sales_record:
            if record.get_day() == day:
                sales_dict = record.get_sales_dict()
                return sales_dict.get(item_name, 0)
            return 0

    def total_sales_for_menu_item(self, item_name):
        total_sales = 0
        for record in self._sales_record:
            sales_dict = record.get_sales_dict()
            total_sales += sales_dict.get(item_name, 0)
        return total_sales

    def total_profit_for_menu_item(self, item_name):
        menu_item = self._menu.get(item_name)
        if not menu_item:
            return 0
        total_sales = self.total_sales_for_menu_item(item_name)
        profit_per_item = menu_item.get_selling_price() - menu_item.get_wholesale_cost()
        return total_sales * profit_per_item


    def total_profit_for_stand(self):
        total_profit = 0
        for item_name in self._menu:
            total_profit += self.total_profit_for_menu_item(item_name)
        return total_profit

# Main function
def main ():
    stand = LemonadeStand('Lemons R Us') # Create a new LemonadeStand called 'Lemons R Us'

# add menu items
    item1 = MenuItem('lemonade', 0.5, 1.5) # Create lemonade as a menu item (wholesale cost 50 cents, selling price $1.50)
    item2 = MenuItem('nori', 0.6, 0.8) # Create nori as a menu item (wholesale cost 60 cents, selling price 80 cents)
    item3 = MenuItem('cookie', 0.2, 1) # Create cookie as a menu item (wholesale cost 20 cents, selling price $1.00)
    stand.add_menu_item(item1) # Add lemonade to the menu for 'Lemons R Us'
    stand.add_menu_item(item2) # Add nori to the menu for 'Lemons R Us'
    stand.add_menu_item(item3) # Add cookie to the menu for 'Lemons R Us'

# Sales dictionary
    day_0_sales = {'lemonade': 5, 'cookie': 2, 'not_in_the_menu ': 1}

# Try/except block for invalid sales
    try:
        stand.enter_sales_for_today(day_0_sales)
    except InvalidSalesItemError as e:
        print(f'Error: {e}')
        
 if __name__ == '__main__':
     main()
