# This is program that calculates the total holiday cost of a customer.
# These total cost includes PLANE COST, HOTEL COST and CAR-RENTAL COST.
def option():
    print("c = continue")
    print("q = quit")

# created a function that calculates hotel cost
def hotel_cost(num_nights):
    return (num_nights * 300)

# created a function that calculates plane cost           
def plane_cost(city_flight):
    return country_dic[city_flight]

# created a function that calculates car rental
def car_rental(rental_days):
    return rental_days * Taxis[city_flight]

# created a function that calculates total holiday cost
def holiday_cost(hotel_cost, plane_cost, car_rental):
    return (hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days))
    
print("____________Hello There._____________ ") 
print("Welcome To Prudence Travel Agency Ltd,")
print("--------------------------------------")

while True:
    option()
    user_input = input("Please Enter an option from the above.: ").lower().strip()
    if user_input != "q":
        
        # created a list of avaliable country destination
        valid_country = ["italy", "nigeria", "south africa", "united Kingdom", "canada"]
        
        # created a dictionary of avaliable country destination and price value.
        country_dic = {"italy" : 750,
                    "nigeria" : 1000,
                    "south africa" : 970,
                    "united kingdom" : 1390,                       
                    "canada" : 1500,}
        
        # created a dictionary of avaliable country destination and taxis price.
        Taxis = {"italy" : 50,
                    "nigeria" : 10,
                    "south africa" : 97,
                    "united kingdom" : 90,                       
                    "canada" : 150,}
        
        # using a while loop to iterate city flight and valid country
        while True:
            city_flight = input('''\nPlease enter your desired destination.\nHere are options of our travel destinations
Italy, Nigeria, South Africa, United Kingdom, Canada': ''').lower().rstrip().strip()
            if city_flight in valid_country:
                break
            else:
                print("We are Sorry, Destination not found")
            
        # using a while loop to handle value error from users input
        while True:
            try:
                num_nights = int(input("Please enter the number of nights you will be staying in the hotel: "))
                break
            
            except ValueError:
                print("Invalid input. Please enter a valid number for numbers of night.")
                
        # using a while loop to handle value error from users input
        while True:
            try:
                rental_days = int(input("Please enter the numbers of days you will be renting a car : "))
                break
            
            except ValueError:
                print("Invalid input. Please enter a valid number for rental days.")
               
        # print all calculated steps with the help of my function
        
        print(f"\nThe plane cost to {city_flight} is = {plane_cost(city_flight)}pp (per person)")
        print(f"The hotel cost is = {hotel_cost(num_nights)}")
        print(f"Car rentals for {rental_days}days is = {car_rental(rental_days)}")
        print(f'''\nTotal Holiday for {city_flight} is = {holiday_cost(hotel_cost, plane_cost,car_rental)}pp (per person)\n''')
        
        print("Do you wish to try another desired destination?\n")
        
    else:
        break
print("\nThanks for your enquiry")           
print("See you again soon.")