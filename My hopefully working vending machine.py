class my_beautiful_and_hopefully_working_vendingmachine:
    def __init__(vend): #im using "__init__(self)" to create an object that will automatically be called
        # making a dictionary of the menu with item code, item price, and item name of the products
        vend.menu = {
            "1a": {"name": "Pocari Sweat", "price": 1.50},
            "2b": {"name": "7up", "price": 1.30},
            "3c": {"name": "Water", "price": 0.50},
            "4e": {"name": "Biscuit", "price": 2.99},
            "5f": {"name": "HelloPanda!", "price": 3.50},
            "6g": {"name": "SB mocha latte", "price": 7.50},
        }
        vend.balance = 0.0  #making a variable for the current balance of the user

    def display_menu(vend):#to output the welcome message and menu of the vending machine
        print("Welcome to my hopefully working Vending machine")
        print("PLEASE BUY SOMETHING RAAAAHH")
        print("Menu:")
        for code, item in vend.menu.items():
            print(f"{code}. {item['name']} - ${item['price']:.2f}")

    def select(vend):#this is so the user is able to select the item they want
        while True:
            selection = input("type the code of the item you want to buy :")
            if selection in vend.menu: #checks if the item code is in the machine
                item = vend.menu[selection]
                print(f"Good choice. You selected {item['name']} for ${item['price']:.2f}.")
                return selection #stores the item selected
            else:
                print("Thats not a item code. Please enter a valid item code.") #if the user doesn't put the right item code

    def money(vend):#makes the user input a number so they can pay
        while True:
            try:
                amount = float(input("Insert money: $")) #inputs the users money
                vend.balance += amount #to add the amount given to the current user balance
                print(f"You've inserted ${amount:.2f}. Current balance: ${vend.balance:.2f}")
                return
            except ValueError:
                print("Invalid input. Please enter real money.")

    def change(vend, selected_code):  # this will check if the user has enough balance and if they have change
        item = vend.menu[selected_code]
        while vend.balance < item["price"]:  # loop until the user balance is enough
            required_amount = item["price"] - vend.balance
            print(f"Not enough mula. give me at least ${required_amount:.2f} more.")
            try:
                additional_money = float(input("Insert additional money: "))
                if additional_money > 0:
                    vend.balance += additional_money
            except ValueError:
                print("Please enter a number.")
        change = vend.balance - item["price"]  # stores change if there is change to be given
        print(f"Dispensing your {item['name']} enjoy your {item['name']}")
        if change > 0:  # checks if there's change to be returned
          print(f"And don't forget, here's your change bro: ${change:.2f}")
        else:
          print("No change to return.")
        return True

    def run(vend):#This function is to call every function I made to run the vending machine.
        while True:
            vend.display_menu()#display the menu to the user
            selected_code = vend.select() #stores the selected item
            vend.money()#add money to the current users balance
            if not vend.change(selected_code): #compares if there is change return and if user have enough balance
                continue
            while True: #this will a create a loop that will allow the user to buy more items
                more_items = input("Do you want to buy more items? (y/n): ").lower()
                if more_items == "y":
                    break #loops back to start
                elif more_items == "n":
                    print("Thank you for using my beautiful and hopefully working vending machine. GET OUT!")
                    return #stop the loop 
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
# creating a variable that will call the class and run it
print("""
 _    _  ____  __    ___  _____  __  __  ____    ____  _____    __  __  _  _    _  _  ____  _  _  ____  ____  _  _  ___    __  __    __    ___  _   _  ____  _  _  ____ 
( \/\/ )( ___)(  )  / __)(  _  )(  \/  )( ___)  (_  _)(  _  )  (  \/  )( \/ )  ( \/ )( ___)( \( )(  _ \(_  _)( \( )/ __)  (  \/  )  /__\  / __)( )_( )(_  _)( \( )( ___)
 )    (  )__)  )(__( (__  )(_)(  )    (  )__)     )(   )(_)(    )    (  \  /    \  /  )__)  )  (  )(_) )_)(_  )  (( (_-.   )    (  /(__)\( (__  ) _ (  _)(_  )  (  )__) 
(__/\__)(____)(____)\___)(_____)(_/\/\_)(____)   (__) (_____)  (_/\/\_) (__)     \/  (____)(_)\_)(____/(____)(_)\_)\___/  (_/\/\_)(__)(__)\___)(_) (_)(____)(_)\_)(____)
""")

vending_machine = my_beautiful_and_hopefully_working_vendingmachine()
vending_machine.run()

print("""
  ___   __    __  ____    ____  _  _  ____         ____  __ _    __   __  _  _  _   
 / __) /  \  /  \(    \  (  _ \( \/ )(  __)   _   (  __)(  ( \ _(  ) /  \( \/ )/ \  
( (_ \(  O )(  O )) D (   ) _ ( )  /  ) _)   ( )   ) _) /    // \) \(  O ))  / \_/  
 \___/ \__/  \__/(____/  (____/(__/  (____)  (/   (____)\_)__)\____/ \__/(__/  (_)  

""")
