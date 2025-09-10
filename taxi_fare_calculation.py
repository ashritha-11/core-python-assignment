BASE_FARE = 50
DISTANCE_FARE = 10  
def calculate_fare(distance):
    return BASE_FARE + (DISTANCE_FARE * distance)
trips = [5, 10, 3]

total_fare = 0

for i, distance in enumerate(trips, start=1):
    fare = calculate_fare(distance)
    total_fare += fare
    print(f"Trip {i}: ${fare}")

print("Total Fare: $", total_fare)
