# A game, mad library
# inspiration from kylie ying
# june 2021
import random

sport = input("A sport: ")
country = input("A country: ")
movie = input("A Movie: ")
phone = input("A phone model: ")
month = input("A month: ")

madness = f"\nThis is a tragic yet funny story, a little old village called {country}. \
In every month of {month}, a ritual was held. Scary and brutal, very few every took part in it. \
The ritual was known as....{sport}.This is nothing like \"{movie}\".\
For more info, call us today and you could stand to win a/an {phone}...JOKING"

life = f"\nIf you were born in {country}. It mus be sad. having to tackle life on your own.\
All who are born in {month},oh so sorry. {sport}.This is nothing like \"{movie}\".\
For more info, call us today and you could stand to win a/an {phone}...JOKING"

funny = f"\nThis is the funny bit, time isnt really on my side {month}, a ritual was held. Scary and brutal, very few every took part in it. \
The ritual was known as....{sport}.This is nothing like \"{movie}\".\
For more info, call us today and you could stand to win a/an {phone}...JOKING"

love = f"\nEh mungu nguvu yetu, ilete baraka kwetu {country}. \
In every month of {month}, a ritual was held. Scary and brutal, very few every took part in it. \
The ritual was known as....{sport}.This is nothing like \"{movie}\".\
For more info, call us today and you could stand to win a/an {phone}...JOKING"

pick = random.choice([madness,life,funny, love])
print(pick)



# print ("hello")

# # print ("we are okay")
# x = int(input("enter a value:\n"))
# print(f"input is {x}")
# amt = 1
# while x < 20:

#     print("*" * amt)
#     amt += 1
#     # print(f"{d * 2}")
#     x += 1
# else:
#     print("try again, a bit lower :)")