# first introduced the Finance calculator to the user
print()
print('''\t----------HELLO THERE----------
      \n----------WELCOME TO J2 FINANCE CALCULATOR----------''')

print()

import math

# giving the conditions needed for this to be well accurate, i gave the users options needed for the program to work fine
def option():
    print("CALCULATOR MENU")
    print("Investment - to calculate the ammount of interest you'll earn on your investment.")
    print("Bond       - to calculate the amount you'll have to pay on a home loan.")
    print("'q'        - to quit\n")
    
def option2():
    print()
       
# requested the input of the users and den saved it as a varaiable.
option()
User_info = input("Please enter 'investment' or 'bond' from the menu above to proceed or 'q' to quit:\n").lower().strip()

# Welcomed the user to the investment section of the finance calculator if investment was typed.
# asked the user to give more informations to enable the program be more accurate.
# where p = amount to be deposited, r = interest rate. t = number of years. 
# def investment(ammount_deposited, interest__rate, numbers_of_years):b
    #return ammount_deposited * (1 + interest__rate) * numbers_of_years
def simple_cal(amount, rate, years):
    # Your investment logic here
    return amount * (1 + rate)**years

def compound_cal(ammount, rate, years):
    return ammount * math.pow((1 + rate), years) - ammount

def bond(value, months, rate,):
    return (rate * value)/(1-(1 + rate)**(-months))
while True:
    if User_info != "q":
        if User_info == "investment":
            print("\nWelcome to the investment section of FINANCE CALCULATOR. \n")
            ammount_deposited = int (input("Please enter amount to deposit: "))
            interest__rate = int (input("Please enter the interest rate in whole number only (eg. 8): "))/100
            numbers_of_years = int (input("Enter the numbers of year's you plan to invest: "))

        # Gave the user an option of either simple interest or a compound interest calculation
        # Calculated the interest and printed the result.
            
            interest = input("\nPlease enter if you want a simple or compound interest calculation: ").lower().strip()
            while True:
                if interest == "simple":
                    simple_interest = simple_cal(ammount_deposited, interest__rate, numbers_of_years)
                    print(f"\nYour Total investment on a simple interest after {interest__rate} year(s) is = {simple_interest}")
                    break

                elif interest == "compound":
                    compound_interest = compound_cal(ammount_deposited, interest__rate, numbers_of_years)
                    print(f"\nYour Total investment on a compund interest after {interest__rate} year(s) is = {compound_interest}")
                    break

                else:
                    print("You entered the type of interest wronglly")
                    interest = (input("\nPlease enter if you want a simple or compound interest calculation: ")).lower().strip()
                option()
                User_info = input("Please enter 'investment' or 'bond' from the menu above to proceed or 'q' to quit:\n").lower().strip()
        # User_info = input("Please enter 'investment' or 'bond' from the menu above to proceed or 'q' to quit:\n").lower().strip()
        # if bond was typed, asked the user to input datas needed to calculate for the bond result
        # Calculated and printed the result
        # rounded my result up
            
        elif User_info == "bond":
            print("\nWelcome to the bond section of FINANCE CALCULATOR. \n")
            house_value = int(input("Please enter the value of the house: "))
            months = int(input("Please enter the numbers of month(s) bond will be repaid: "))
            interest_rate = int(input("Please input the monthly interest: "))/100/12
            monthly_amount = bond(house_value, months, interest_rate,)
            print(f"\nTotal repayment {months} month(s) is {monthly_amount} ")
            print(f"which gives us {round(monthly_amount)} when rounded up\n")
            

        # just in case the user gives a wrong input
        # i notify the user and also ask the user to follow the instruction on the screen
        
        else:
            print("You have entered an incorrect option")
            
        option()
        User_info = input("Please enter 'investment' or 'bond' from the menu above to proceed or 'q' to quit:\n").lower().strip()

    else:
        print("Thank you for banking with us")  
        break      

    
    
