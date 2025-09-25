# Weather Advice Program
# This program provides clothing advice based on the temperature input by the user.
weather_condition = input("What's the weather like today? (sunny, rainy, cold): ").strip().lower()

if weather_condition == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather_condition == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather_condition == "cold":
    print("Make sure to wear a warm jacket and a scarf.")
else:
    print("Sorry, I don't have recommendation for this weather.")