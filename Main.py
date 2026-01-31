def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsuies(f):
    return (f - 32) * 5/9

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.24062

while True:
    print("\n Unit Converter developed by Monty")
    print("1.Kilometers to Miles")
    print("2.Miles to Kilometers")
    print("3.Celsius to Fahrenheit")
    print("4.Fahrenheit to Celsius")
    print("5.Kilograms to Pounds")
    print("6.Pounds to Kilograms")
    print("7.Exit")

    choice = input("Enter your Choice(1 - 7): ")

    if choice == 7:
        print("Good Byee!")
        break

    try:
        value = float(input("Enter value to convert:"))

        if choice == "1":
            print(f"Result:{km_to_miles(value):.2f} Miles")
        elif choice == "2":
            print(f"Result:{miles_to_km(value):.2f} Km")
        elif choice == "3":
            print(f"Result:{celsius_to_fahrenheit(value):.2f} F")
        elif choice == "4":
            print(f"Result:{fahrenheit_to_celsuies(value):.2f} C")
        elif choice == "5":
            print(f"Result:{kg_to_pounds(value):.2f} Pounds")
        elif choice == "6":
            print(f"Result:{pounds_to_kg(value):.2f} Kg")   
        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter a valid number!")        
                  

