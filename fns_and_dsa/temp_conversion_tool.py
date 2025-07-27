FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 /5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

temp = input("Enter the temperature to convert: ")
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if temp.replace('.', '', 1).isdigit():
    temperature = float(temp)
    
    if unit.upper() == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {round(converted_temp, 2)}°C")
    elif unit.upper() == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {round(converted_temp, 2)}°F")
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")
else:
    print("Invalid temperature. Please enter a numeric value.")