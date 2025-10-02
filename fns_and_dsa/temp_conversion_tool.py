# Temperature Conversion Tool
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    print("Temperature Conversion Tool")
    
    temperature = float(input("Enter the temperature to convert: "))
    choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    if choice == 'C':
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {fahrenheit:.2f}°F")
    elif choice == 'F':
        celsius = convert_to_celsius(temperature)
        print(f"{temperature}°F is {celsius:.2f}°C")
    else:
        print("Invalid choice. Please select C or F.")

if __name__ == "__main__":
    main()