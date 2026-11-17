# Weather Advice Agent
weather = input("Enter weather (Sunny, Rainy or Cold): ")
if weather == "Sunny" or weather == "sunny":
    print("Wear sunglasses and stay hydrated.")

elif weather == "Rainy" or weather == "rainy ":
    print("Take an umbrella.")

elif weather == "Cold" or weather == "cold":
    print("Wear warm clothes.")

else:
    print("Invalid weather input. Please enter Sunny, Rainy or Cold.")