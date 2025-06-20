# Natalie Banks
# P2LAB2
# 6/20/2025
# writing dictionary in python


vehicles_mpg = {
    "camaro": 18.21,
    "prius" : 52.36,
    "model S": 110,
    "silverado": 26
}


print("Available vehicles:")
for vehicle in vehicles_mpg.keys():
    print (f" -{vehicle.title()}")



vehicle_choice = input("\nEnter a vehicle to its MPG: ") .lower().strip()
miles_driven = float(input("Enter the number of miles you will drive: "))


if vehicle_choice in vehicles_mpg:
    mpg = vehicles_mpg [vehicle_choice]
    gallons_needed = miles_driven / mpg
    print(f"\n{vehicle_choice.title()} gets {mpg} MPG")
    print(f"Gallons of gas needed: {gallons_needed:.2f}")
else:
    print("Vehicle not found in dictionary.")
    print("Please choose from the available vehicles listed above.")

