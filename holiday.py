#This code is to calculate how much a user spends on holiday
#Request user to specify the city they would be travelling to;
#The number of nights they would be spending at a hotel;
#How long they would need to rent a car for
num_nights = int(input("Enter the number of nights to be spent at a hotel: "))
city_flights = input("Enter the city you are travelling to: ")
rental_days = int(input("Enter the number of days you will be hiring a car: "))

#Function to calculate total amount spent on hotel accomodation
#The hotel_cost functionn multiplies the prie per night by the number of nights to get the total hotel cost
def hotel_cost(night_hotel):
    price_night = 200
    total_hotel_cost = night_hotel * price_night 
    return total_hotel_cost

#Function to calculate total amount spent on flight tickets depending on the city being travelled to
#The plane_cost function uses an if-elif-esle statement to determine the amount spent on flight tickets depending on the city travelled to 
def plane_cost(city_travel):
    if city_travel == "Dubai":
        cost_flight = 300
    elif city_travel == "New York":
        cost_flight = 400
    elif city_travel == "Paris":
        cost_flight = 100
    else:
        cost_flight = 650 #The cost of flight ticket for every other city
    return cost_flight

#Function to calculate total amount spent on car rentals
#The car_rental function multiplies the cost of renting a car per day by the number of days it will be rented for 
def car_rental(num_days):
    cost_day = 50
    total_rental_cost = num_days * cost_day
    return total_rental_cost

#Function to calculate total holiday cost
#The holiday_cost function adds up the cost gotten from the other functions to make the total holiday cost 
def holiday_cost(night_hotel, city_travel, num_days):
    total_holiday_cost = hotel_cost(night_hotel) + plane_cost(city_travel) + car_rental(num_days)
    return total_holiday_cost

#Call the function holiday_cost and it is stored in a a variable called total_cost
total_cost = holiday_cost(num_nights, city_flights, rental_days)
#Print statements to print the cost breakdown 
print(city_flights.title(), "Holiday Cost Breakdown")
print("-" * 30)
print("Total cost of hotel: £", hotel_cost(num_nights))
print("Total cost of flight: £", plane_cost(city_flights))
print("Total cost of car rental: £", car_rental(rental_days))
print("-" * 30)
print("Total holiday cost: £", total_cost)

