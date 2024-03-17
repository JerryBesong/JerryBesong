# define the items for sale 
hammer_price = 5
wrench_price = 10
drill_price = 15

# create a shopping cart
shopping_cart = 0
hammer_quantity = 0
wrench_quantity = 0
drill_quantity = 0

# generate greeting
print("Hello and welcome to the Hardware engineering shop! \n")

# create a while loop to continously prompt the user for a choice
while True:
    main_menu_choice = input("---------\n"
                                     "Main Menu\n"
                                     "\n"
                         "Please Choose from the following options:\n"
                         "1. Browse Items\n"
                         "2. View Cart\n"
                         "3. Exit Store\n"
                         "Please Choose your option: "
                         "\n").strip(" .")
            
            # program option 1 
    if main_menu_choice == "1":      
        browsing_menu_choice = input("\nYou have chosen to browse items.\n"
                           "\n"
                          "Items for Sale:\n"
                          "Hammer (£5)\n"
                          "Wrench (£10)\n"
                          "Drill (£15)\n"
                          " \n"
                          "Please type the name of an item you would like to add to cart.\n"
                          "Or type MENU to return"
                          "\n").lower()
             # program the item choices, and add the users choice to the cart variables
        if browsing_menu_choice == "hammer":
            hammer_quantity += int(input("You have selected Hammer.\n"
                                           "Please enter the quantity you would like to add to your cart: "))
            print(f"You have added {hammer_quantity} hammer/s to your cart")
            
        elif browsing_menu_choice == "wrench":   
            wrench_quantity += int(input("You have selected Wrench.\n"
                                           "Please enter the quantity you would like to add to your cart: "))
            print(f"You have added {wrench_quantity} wrench/es to your cart")
            
        elif browsing_menu_choice == "drill":
            drill_quantity += int(input("You have selected Drill.\n"
                                           "Please enter the quantity you would like to add to your cart: "))
            print(f"You have added {drill_quantity} drill/s to your cart")
            
        elif browsing_menu_choice == "menu":
            continue
            
        else:
            print("\nInput Error!\n"
                "Please check your spelling, and try again")
                 
         # calculate the total shopping cart value after adding items
        shopping_cart = (hammer_price * hammer_quantity) + (wrench_price * wrench_quantity) + (drill_price * drill_quantity)
        

    # program the option to view the cart 
    elif main_menu_choice == '2':
            print("You have chosen to view your shopping cart:\n"
                "\n"
                f"Hammer: {hammer_quantity} pieces\n"
                f"Wrench: {wrench_quantity} pieces\n"
                f"Drill: {drill_quantity} pieces\n"
                "\n"
                "---------\n"
                "\n"
                f"Your total is £{shopping_cart}\n")
            
            # program an option to confirm the cart and checkout
            confirm_cart = input("Please type YES to checkout or EDIT to edit basket\n"
                                 "").upper()
            
            if confirm_cart == "YES":
                print("Thank You for Shopping at The Hardware Engineering Store. Goodbye!")
                break

            # program an option to edit the cart
            elif confirm_cart == "EDIT":
                item_alteration_choice = input("Please type which item you would like to alter the quantity of:\n").lower()
                
                if item_alteration_choice == "hammer":
                    hammer_quantity = int(input("You have selected Hammer.\n"
                                           "Please enter the quantity you would like in your cart: "))
                    print(f"You now have {hammer_quantity} hammer/s in your cart")
                
                elif item_alteration_choice == "wrench":   
                    wrench_quantity = int(input("You have selected Wrench.\n"
                                           "Please enter the quantity you would like in your cart: "))
                    print(f"You now have {wrench_quantity} wrench/es in your cart")
               
                elif item_alteration_choice == "drill":
                    drill_quantity = int(input("You have selected Drill.\n"
                                           "Please enter the quantity you would like in your cart: "))
                    print(f"You now have {drill_quantity} drill/s in your cart")
                else:
                    print("\nInput Error!\n"
                     "Please check your spelling, and try again")   
            else:
                print("\nInput Error!\n"
                    "Please check your spelling, and try again") 
               
                # calculate the total shopping cart value after adding items
            shopping_cart = (hammer_price * hammer_quantity) + (wrench_price * wrench_quantity) + (drill_price * drill_quantity)

    # program option 3 to exit the store
    elif main_menu_choice == "3":
        print("Thanks for visiting The Hardware Engineering Store!\n"
              "We hope to see you again soon!")
        break
    else: print("\nInput Error!\n"
          "Please check your spelling, and try again")
                


                    
                    

                    
