# Script for interactive ordering system from food truck menu
# Adapted from UNCC AI Bootcamp Day 3 Activity (code for printing a menu)
# Jamie Bond submission for Python Challenge 1 (MOD 2)

# --------- INITIALIZING ORDER SYSTEM --------- 

# Menu items by menu catagory
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# Menu display support
menu_dashes = "-" * 42

#Initialize customer list
customer_order = []
# --------- TAKING CUSTOMER ORDER --------- 

# Greet customer to signal start of engagment
print("Welcome to the variety food truck.")

# Create continuous loop to stay in order-taking mode until order complete
place_order = True 
while place_order:
    # Prompt customer to select a menu category from which to order
    print("\nWhich menu can I show you? ")

    # Create a variable for the menu item number
    i = 1

    # Create a dictionary to store the menu for later retrieval 
    menu_items = {}
   
    # Print menu catagory options to choose from menu keys
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1
 
    # Capture menu catagory input from customer
    menu_category = input("\nPlease select menu number to view or 'c' to cancel: ")
    
    # Exit the loop if user typed 'c' to cancel
    if menu_category == 'c':
        break
    
    # 3) Validate input. Confirm menu_category is a number.
    #    If menu_category is not a number, print error
    #    If menu_category is a number, convert input string to integer 
    elif menu_category.isdigit():

        # 4A) Use valid menu_category to check if its in the keys for menu_items dictionary
        #     If menu_catagory input is a digit cast input digit as an integer before comparing
        #     If menu_category is not in the keys, print error message
        #     If menu_category is in the keys, store name from menu_items as item_ordered

        if int(menu_category) in menu_items.keys():

            # Save the menu category name to a variable by indexing menu_item list     
            menu_category_name = menu_items[int(menu_category)]

            # Print out the menu category name they selected
            print(f"\nYou selected {menu_category_name}")

            # creates dictionary to hold items and prices from submenu selected 
            submenu_selected = {}

            # Print out the menu options from the menu_category_name
            print(f"\nWhat {menu_category_name} item would you like to order?")
            i = 1

            print("\nItem # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
 
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1



            menu_selection_number = input(f"\nPlease select the {menu_category_name} number you would like: ")
            
            if menu_selection_number.isdigit():
                if int(menu_selection_number) in menu_items.keys():

                    #Saves selected submenu       
                    item_ordered = menu_items[int(menu_selection_number)]
                    print(item_ordered)
                # Save the menu category name to a variable by indexing menu_item list     
                    menu_category_name = menu_items[int(menu_category)]
                    #item_ordered = menu(menu_category_name)[menu_items[int(menu_selection_number)]]

                    # Save the menu selection name to a variable by indexing menu_item list     
                    # menu_selection_name = menu_items[int(menu_category)][menu_category_name]
                    # menu_selection_price = [menu][menu_items[int(menu_selection)]]
                    
                    # Print out the menu category name they selected
                    print(f"\nYou selected {item_ordered.get('Item name')}")

                    # 4B) Ask customer for quanity of item_ordered and save to quanity (variable)
                    #     Add note that default quantity will be 1 for invalid inputs
                    #     Validate quantity is a number
                    #     If quanity is not a number set quantity = 1 
                    #     If quanity is a number, convert quanity input string to integer value
                    #     REQUIREMENT: customer prompted for quantity, defaults to 1 
                    quantity = input(f"\nEnter the quanity of {item_ordered.get('Item name')} to order? (Note: quanty will be 1 if input is invalid): ")
                    if quantity.isdigit():
                        quantity_ordered = int(quantity)
                    else:
                        quantity_ordered = 1
                    # Print out the menu category name they selected
                    print(f"\nQuantity of {item_ordered.get('Item name')} ordered: {quantity_ordered}")

                    # 4C)  Append customer order to customer_order in dictionary format
                    #      Use "Item Name", "Price", and "Quantity" as keys (Price foudn in items_menu)
                                  
                    customer_order.append({"Item name": item_ordered.get('Item name'),"Price": item_ordered.get('Price'), "Quantity": quantity_ordered}  )
        else: 
            print("\nError. This is not a valid selection.")
    else: 
        print("\nError. This is not a valid selection.")

    # 5) Prompt the customer to keep ordering using y/n option and continous while loop
    #    use lowercase method to convert input to lower case 
    #    Use match:case statement to check for "y" or "n"
    #    If invalid, tell customer enter valid "y" or "n" input
    #    If continue_order is "y" set place_order to True and break from continous while loop
    #    If "n" set place_order to False, print "Thank you for your order." and brake loop

    keep_ordering = input("\nWould you like to keep ordering? (Y)es or (N)o ")
    # Check the customer's input
    match keep_ordering.lower():
        # Customer chose yes
       case 'y':
            # Keep ordering
            place_order = True
            # Exit the keep ordering question loop
            #break
        # Customer chose no
       case 'n':
            # Complete the order
           place_order = False
            # Since the customer decided to stop ordering, thank them for their order
           print("\nThank you for your order.")
            # Exit the keep ordering question loop
           break
        # Customer typed an invalid input
       case _:
            # Tell the customer to try again
            print("\nI didn't understand your response. Please try again.")

    # Print out the customer's order
print("\nThis is what we are preparing for you.")
print (customer_order)
    # --------- ORDER RECEIPT ---------

print("\nItem name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6) Use for loop to loop through order menu_selection list
for key3, value3 in [customer_order].items():

    # 7) For Loop Code Block: save each key as variables (item_name, price and quanity)
    # 8) Determine character count needed for item_column, price_column, quanity_column
    # 9) Use string mulitplication to create space strings as own variable
    # 10) Print the line for reciept using format below

    # Item name                 | Price  | Quantity
    # --------------------------|--------|----------
    # Apple                     | $0.49  | 1
    # Tea - Thai iced           | $3.99  | 2
    # Fried banana              | $4.49  | 3


    print (f"{key3}{item_spaces} | ${value3}  | {quantity_ordered}")
    customer_order[menu_category_name] = {
        "Item name": key2 + " - " + key3,
        "Price": value3 + " - " + key3,
        "Quantity": value3 + " - " + key3
    }
    i += 1

price_list = [Price for Price in customer_order]
quantity_list = [quantity_ordered in customer_order]
total_cost = list(map(lambda x, y: x * y, price_list, quantity))
print(total_cost)

    # 11) When exiting for loop, calcute and display total price of order 
    #     Use list comprehension and sum() function (remember: price * quantity)
    #     REQUIREMENT: list comprehension used to calcuate total price
    #     REQUIREMENT: total price printed to screen
    # 
    
