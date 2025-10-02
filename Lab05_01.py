price = 12000

age = int(input("Enter your age: "))
week = input("Enter the day of the week: ")
movie = input("Enter movie type (Normal/3D/IMAX): ")

if age < 13:
    price *= 0.5
elif age>=13 and age<=18:
    price *= 0.7
elif age >= 65:
    price *= 0.6

if week.strip().lower() == "wednesday":
    price *= 0.8

if movie.strip().lower() == "normal":
    pass
elif movie.strip().lower() == "3d":
    price += 3000
elif movie.strip().lower() == "imax":
    price += 5000

if price == 0:
    print("Free Ticket!")
else:
    print(f"Final ticket price: {price}KRW")
