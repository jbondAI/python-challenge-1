# Script for interactive ordering system from food truck menu
# Adapted from UNCC AI Bootcamp Day 3 Activity (code for printing a menu)
# Jamie Bond submission for Python Challenge 1 (MOD 2)

# --------- ORDER SYSTEM --------- 
# 1A) Create an empty list for storing customer's order
#     REQUIREMENT: initialize order list 
menu_selection = []


# 1B) Use list to store customer order dictionary
[
  {
    "Item name": "string",
    "Price": float,
    "Quantity": int
  },
  {
    "Item name": "string",
    "Price": float,
    "Quantity": int
  },
]

# 2) Prompt customer to enter selection from menu saving and save to menu_selection variable
#    REQUIREMENT: save customer input to menu_selection 


# 3) Validate input. Confirm menu_selection is a number.
#    If menu_selection is not a number, print error
#    If menu_selection is a number, convert input string to integer 
#    REQUIREMENT: validate input and print error
#    REQUIREMENT: convert to integer  

# 4A) Use valid menu_selection to check if its in the keys for menu_items dictionary
#     If menu_selection is not in the keys, print error message
#     If menu_selection is in the keys, store name from menu_items as item_ordered
#     REQUIREMENT: if-else used to check if menu_selection is in menu_items keys and error printed 
#     REQUIREMENT: item name is extracted from menu_items and stored as variable 

# 4B) Ask customer for quanity of item_ordered and save to quanity (variable)
#     Add note that default quantity will be 1 for invalid inputs
#     Validate quantity is a number
#     If quanity is not a number set quantity = 1 
#     If quanity is a number, convert quanity input string to integer value
#     REQUIREMENT: customer prompted for quantity, defaults to 1 

# 4C)  Append customer order to menu_selection in dictionary format
#      Use "Item Name", "Price", and "Quantity" as keys (Price foudn in items_menu)
#      REQUIREMENT: customer selected item, price and quantity appended to order list dictionary

# 5) Prompt the customer to keep ordering using y/n option and continous while loop
#    use lowercase method to convert input to lower case 
#    Use match:case statement to check for "y" or "n"
#    If invalid, tell customer enter valid "y" or "n" input
#    If continue_order is "y" set place_order to True and break from continous while loop
#    If "n" set place_order to False, print "Thank you for your order." and brake loop
#    REQUIREMENT: match-case converts input to lower or upper case before checking case
#    REQUIREMENT: match-case used to check if customer would like to keep ordering w/default case



# --------- ORDER RECEIPT ---------

# 6) Use for loop to loop through order menu_selection list
#    REQUIREMENT: for loop used to loop through order

# 7) For Loop Code Block: save each key as variables (item_name, price and quanity)
#    REQUIREMENT: key values saved to variables

# 8) Determine character count needed for item_column, price_column, quanity_column
#    Use subtract len() from total character count to maintain column alignment
#    REQUIREMENT: number of formating spaces correctly calculated

# 9) USe string mulitplication to create space strings as own variable
#    REQUIREMENT: space string created using string multiplication
#    NOTE TO SELF: look up string multiplication

# 10) Print the line for reciept using format below

# Item name                 | Price  | Quantity
# --------------------------|--------|----------
# Apple                     | $0.49  | 1
# Tea - Thai iced           | $3.99  | 2
# Fried banana              | $4.49  | 3

#    REQUIREMENT: order printed with item name, price and quantity

# 11) When exiting for loop, calcute and display total price of order 
#     Use list comprehension and sum() function (remember: price * quantity)
#     REQUIREMENT: list comprehension used to calcuate total price
#     REQUIREMENT: total price printed to screen
#     NOTE TO SELF: Look up list comprehension





# --------- STARTER CODE --------- 

# Menu dictionary (Note TO SELF: Determine if menu needs to be menu_items)
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

# 1. Set up order list. Order list will store a list of dictionaries for




# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
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
            # 2. Ask customer to input menu item number


            # 3. Check if the customer typed a number

                # Convert the menu selection to an integer


                # 4. Check if the menu selection is in the menu items

                    # Store the item name as a variable


                    # Ask the customer for the quantity of the menu item


                    # Check if the quantity is a number, default to 1 if not


                    # Add the item name, price, and quantity to the order list


                    # Tell the customer that their input isn't valid


                # Tell the customer they didn't select a menu option

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input

                # Keep ordering

                # Exit the keep ordering question loop

                # Complete the order

                # Since the customer decided to stop ordering, thank them for
                # their order

                # Exit the keep ordering question loop


                # Tell the customer to try again


# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order

    # 7. Store the dictionary items as variables


    # 8. Calculate the number of spaces for formatted printing


    # 9. Create space strings


    # 10. Print the item name, price, and quantity


# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
