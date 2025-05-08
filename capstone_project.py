"""
capstone_project

Description:
"""

import random

# List to store PINs and card numbers
pins = []
card_numbers = ["3827 1490 5763 8924", "9237 5841 6209 4518", "5739 2018 4830 7264", "1098 7453 6120 4875", "8746 3201 5369 2907"]

# Available items in the store
inventory = ["cheese", "crackers", "vegetable oil", "dragonfruit", "pasta", "eggs", "candy", "pineapple", "chicken", "water", "juice"]

# List of points associated with each food item
food_points = [15, 21, 32, 42, 50, 25, 27, 15, 25, 15, 10]

# # Randomly selects the item the user earns
food = random.choice(inventory)

# List to store the user's selected items
print(inventory) 

# Loop to allow the user to select multiple items
while True:
    selected_items = [] 
        # Ask the user what they would like to buy
    buy = input("What would you like to buy? ").lower()
        # Check if the item is in the inventory
    if buy in inventory:
        selected_items.append(buy)  
    else:       
        print("Invalid item")
        continue
    # Ask for a second item or exit
    second = input('Type in a second item, or press "done" if finished ').lower()
    if second == "done":
        pass
  # Exit the loop if the user is done
    elif second in inventory:
        selected_items.append(second)
        
    else:
        print("Invalid item")

    # If the user selected any items
    if selected_items:
        print("You selected the following items: ",','.join(selected_items))
    else:
        print("You didn't select any items.")
        
        # Randomly selects a point value for the item the user wants to purchase
    total_points = 0
    for item in selected_items:
        total_points += random.choice(food_points)
        
        # Ask how they would like to pay (cash or card)
    payment = input("Would you like to pay card or cash? ")
        
        # If they choose to pay with cash, thank them and show the points earned
    if payment == "cash":
        print("Thank you for your purchase! ")
        print("You earned " + str(total_points) + "points.")
            
        
        # If they choose to pay with a card
    elif payment == "card":
            # Prompt the user to input their card number
        user_card = input("What is your card information? ")
        #checks to see if card digit is NOT 16 characters long
        masked_card = "************" + user_card[12:] 
        if len(masked_card) == 16:
            print("Card numbers: " + masked_card)
        
        else:
            print("This is not a valid card number")
            continue
            # Check if the entered card number exists in the list of valid card numbers
        if user_card in card_numbers:
                # If valid card, prompt for the PIN
            pin = input("Please enter your PIN: ")
            pins.append(pin)
                # Check if the entered PIN matches the stored PIN for that card
            if pin in pins:
                    # If PIN is correct, process the payment and mask the card number
                print("Thank you for your purchase!")
                print("You earned", str(total_points), "points.")
                    # If the points earned are 10 or more, the user gets free items
    else:
        print("That is not a payment")
    if total_points >= 25:
        print("You earned free items:"+ str (food))
