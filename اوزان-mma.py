print("|Welcome to MMA Classes App|")
print("1. KG (Kilograms)")
print("2. Lbs (Pounds)")
type1 = input("Choose (1 or 2): ")
weight = float(input("Enter your weight: "))

if type1 == "1":
    weight = weight * 2.20462    

print("1. Men")
print("2. Women")
gender = input("Choose (1 or 2): ")

if gender == "1":
    if weight <= 125:
        print("You are in Flyweight division (Demetrious Johnson style)")
    elif weight <= 135:
        print("You are in Bantamweight division (Merab Dvalishvili style)")
    elif weight <= 145:
        print("You are in Featherweight division (Alexander Volkanovski style)")
    elif weight <= 155:
        print("You are in Lightweight division (Khabib and Islam style)")
    elif weight <= 170:
        print("You are in Welterweight division (Georges St-Pierre style)")
    elif weight <= 185:
        print("You are in Middleweight division (Anderson Silva style)")
    elif weight <= 205:
        print("You are in Light Heavyweight division (Jon Jones style)")
    else:
        print("You are in Heavyweight division (Tom Aspinall style)")    

elif gender == "2":
    if weight <= 115:
        print("You are in Strawweight division (Zhang Weili style)")
    elif weight <= 125:
        print("You are in Flyweight division (Valentina Shevchenko style)")
    elif weight <= 135:
        print("You are in Bantamweight division (Amanda Nunes style)")
    else:
        print("You are above UFC women divisions")

else:
    print("Invalid choice! Please run the app again and choose 1 or 2.")

print("1. Wrestling, Pressure & Fence Control - Dagestani Style")
print("2. Striking & Boxing")
style = input("Choose your style (1 or 2): ")

if style == "1":
    print("You are a complete fighter! Smash them on the ground like Khabib!")
elif style == "2":
    print("Focus on your footwork and look for the knockout!")
input("\nPress Enter to exit...")
