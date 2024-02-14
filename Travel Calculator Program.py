# This is program that calculates the total holiday cost of a customer.
# These total cost includes PLANE COST, HOTEL COST and CAR-RENTAL COST.
def option():
    print("c = continue")
    print("q = quit")
print("Hello There. \n") 
print("Welcome To Prudence Travel Agency Ltd,") 

while True:
    option()
    user_input = input("Please Enter Your Choice from the above: ").lower().strip()
    if user_input != "q":
        
        # collected data from the user using input
        valid_city = ["italy", "nigeria", "south africa", "united Kingdom", "canada"]
        city_dic = {"italy" : 750,
                    "nigeria" : 1000,
                    "south africa" : 970,
                    "united kingdom" : 1390,                       
                    "canada" : 1500,}

        Taxis = {"italy" : 50,
                    "nigeria" : 10,
                    "south africa" : 97,
                    "united kingdom" : 90,                       
                    "canada" : 150,}

        #city_flight = input("Please enter your desired destination.\nHere are options of our travel destinations (Italy, Nigeria, South Africa, United Kingdom, Canada': ").lower().rstrip().strip()
        while True:
            city_flight = input("\nPlease enter your desired destination.\nHere are options of our travel destinations Italy, Nigeria, South Africa, United Kingdom, Canada': ").lower().rstrip().strip()
            if city_flight in valid_city:
                break
            else:
                print("We are Sorry, Destination not found")
            
        num_nights = int(input("Please enter the numbers of night you will be staying in the hotel : "))

        while True:
            rental_days = int(input("Please enter the numbers of days you will be renting a car : "))
            if rental_days >= 0:  # Add appropriate validation for rental days
                break
            else:
                print("Invalid input. Please enter a non-negative number for rental days.")
            #if city_flight in Taxis:
                break
            #else:
                #print("We are Sorry, Destination not found")

        # created three functions to make the program calculation easy when ever we will be needing to calculate.

        def hotel_cost(num_nights):
            return (num_nights * 300)
            
        def plane_cost(city_flight):
            return city_dic[city_flight]

        def car_rental(rental_days):
            return rental_days * Taxis[city_flight]

        def holiday_cost(hotel_cost, plane_cost, car_rental):
            return (hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days))

        # using a loop statement to give verity of flight destination and cost to our user
    
        # print all calculated steps with the help of my function
        
        print(f"\nThe plane cost to {city_flight} is = {plane_cost(city_flight)}pp (per person)")
        print(f"The hotel cost is = {hotel_cost(num_nights)}")
        print(f"Car rentals for {rental_days}days is = {car_rental(rental_days)}")
        print(f"\nTotal Holiday for {city_flight} is = {holiday_cost(hotel_cost, plane_cost,car_rental)}pp (per person)\n")
        
        print("Do you wish to try another desired destination?\n")
        

    else:
        break
print("\nThanks for your enquiry")           
print("see you again soon")