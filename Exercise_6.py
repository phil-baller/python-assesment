def convert_distance(miles):
    km = miles * 1.6
    return km

my_trip_miles = 55

my_trip_km = convert_distance(my_trip_miles)

print("The distance in kilometers is: " + str(my_trip_km))

print("The round-trip in kilometers is: " + str(my_trip_km * 2))