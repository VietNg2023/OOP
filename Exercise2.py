#Name: Exercise 2
#Author: Viet Nguyen
#Date: 16 Jan 2024
#Description: Coin object and tossing
#Task 2
# import random
# #Class definition
# class Coin:
#     def __init__(self):
#         self.sideup = "Heads"

#     def toss_the_coin(self):
#         if random.randint(0,4) == 0:
#             self.sideup = "Heads"
#         elif random.randint(0,4) == 1:
#             self.sideup = "Tails"
#         #Task 2
#         elif random.randint(0,4) == 2:
#             self.sideup = "OMG!Coin lands on the table upright"
#         elif random.randint(0,4) == 3:
#             self.sideup = "Unlucky! Coin drops on the ground and disappears in a rabbit hole"
#         else:
#             self.sideup = "Unfortunely! Coin defies gravity and gets lost on a wormhole in space"
    
#     def get_sideup(self):
#         return self.sideup
    
# #Main function definition
# def main():
#     my_coin = Coin()
#     print("This side is up:", my_coin.get_sideup())
#     print("Tossing the coin...")
#     my_coin.toss_the_coin()
#     print("Now this side is up:",my_coin.get_sideup())

# #Calling the main function
# main()

#Task3: alarm clock
# import time

# def time_running(hours,minutes,seconds):
#     while True:
#         time.sleep(1)
#         seconds += 1
#         if seconds == 60:
#             seconds = 0
#             minutes += 1

#             # Check for overflow in minutes
#             if minutes == 60:
#                 minutes = 0
#                 hours += 1

#                 # Check for overflow in hours
#                 if hours == 24:
#                     hours = 0

#         # Returning the current time
#         return hours, minutes, seconds
                
# def main():
#     current_hour = int(input('Please input current hours-24h format:'))
#     current_minute = int(input('Please input current minute-24h format:'))
#     current_second = int(input('Please input current hours-24h format:'))
#     alarm_hour = int(input('Please input alarm hours-24h format:'))
#     alarm_minute = int(input('Please input alarm minutes-24h format:'))
#     while True:
#         current_hour, current_minute, current_second = time_running(current_hour,current_minute,current_second)
#         print('Current time:',current_hour,':',current_minute,':',current_second)
#         if current_hour == alarm_hour and current_minute == alarm_minute:
#             print('Alarm!!! Buzz')

# main()

#Task 4:
# def factorials(n):
#     dict_fac = {}
#     fac = 1
#     for i in range(1,n+1):
#         fac = fac*i
#         dict_fac[i]=fac
#     return dict_fac
# k = factorials(5)
# print(k[1])
# print(k[3])
# print(k[5])

#Task 5:
# def smallest_average(person1,person2,person3):
#     person1_average = person1["result1"] +person1["result2"] + person1["result3"]
#     person2_average = person2["result1"] +person2["result2"] + person2["result3"]
#     person3_average = person3["result1"] +person3["result2"] + person3["result3"]
#     if person1_average < person2_average: 
#         if person1_average < person3_average:
#             person1["smallest"] = 1
#         elif person1_average > person3_average:
#             person3["smallest"] = 1
#         else:
#             person1["smallest"] = 1
#             person3["smallest"] = 1
#     elif person1_average > person2_average: 
#         if person2_average < person3_average:
#             person2["smallest"] = 1
#         elif person2_average > person3_average:
#             person3["smallest"] = 1
#         else:
#             person2["smallest"] = 1
#             person3["smallest"] = 1
#     else:
#         if person1_average < person3_average:
#             person1["smallest"] = 1
#             person2["smallest"] = 1
#         elif person1_average > person3_average:
#             person3["smallest"] = 1
#         else:
#             person1["smallest"] = 1
#             person2["smallest"] = 1
#             person3["smallest"] = 1
#     return person1,person2,person3
# person1 = {"name": "Mary","result1":2,"result2":3,"result3":1}
# person2 = {"name": "Gary","result1":2,"result2":3,"result3":1}
# person3 = {"name": "Larry","result1":2,"result2":3,"result3":3}
# person1,person2,person3 =smallest_average(person1,person2,person3)
# if person1.get("smallest")==1:
#     print('The smallest average is: ',person1)
# if person2.get("smallest")==1:
#     print('The smallest average is: ',person2)
# if person3.get("smallest")==1:
#     print('The smallest average is: ',person3)

#Task6:
# from datetime import date

# def list_year(all):
#     date1 = all[0]
#     date2 = all[1]
#     date3 = all[2]
#     list_year = [date1.year,date2.year,date3.year]
#     list_year.sort()
#     return list_year

# date1 = date(2009,2,3)
# date2 = date(2010,10,10)
# date3 = date(1993,5,9)

# years = list_year([date1,date2,date3])
# print(years)

#Task 7:
# class Book:
#     def __init__(self,name,author,genre,year):
#         self.name = name
#         self.author = author
#         self.genre = genre
#         self.year = year

# python = Book("Fluent Python","Luciano Ramalho","programming",2015)
# everest = Book("High Adventure","Edmud Hillary","autobiography",1956)
# print(f"{python.author}: {python.name} ({python.year})")
# print(f"The genre of the book {everest.name}: {everest.genre}")

#Task 8:
# class Checklist:
#     def __init__(self, header="", entries=[]):
#         self.header = header
#         self.entries = entries

# class Customer:
#     def __init__(self, id="", balance=0.0, discount=5):
#         self.id = id
#         self.balance = balance
#         self.discount = discount

# class Cable:
#     def __init__(self, model="", length=0.0, max_speed=100, bidirectional=True):
#         self.model = model
#         self.length = length
#         self.max_speed = max_speed
#         self.bidirectional = bidirectional

#Task 9:
# class Pet():
#     def __init__(self,name,species,year_of_birth):
#         self.name = name
#         self.species = species
#         self.year_of_birth = year_of_birth

# def new_pet(name, species, year_of_birth):
#     return Pet(name,species,year_of_birth)

# fluffy = new_pet("Fluffy","dog","2017")
# print(fluffy.name)
# print(fluffy.species)
# print(fluffy.year_of_birth)

#Task 10:
class Movie():
    def __init__(self,name,director,genre,year):
        self.name = name
        self.director = director
        self.genre = genre
        self.year = year

def movies_of_genre(movies,genre):
    new_list=[]
    for movie in movies:
        if movie.genre == genre:
            new_list.append(movie)
    return new_list

john_woo = Movie("A Better Tomorrow", "John Woo", "action", 1986)
kungfu = Movie("Chinese Odyssey", "Stephen Chow", "comedy", 1993)
jet_li = Movie("The Legend", "Corey Yuen", "comedy", 1993)
movies = [john_woo, kungfu, jet_li, Movie("Hero", "Yimou Zhang","action", 2002)]
print("Movies in the action genre:")
for movie in movies_of_genre(movies,"action"):
    print(f"{movie.director}: {movie.name}")

# for movie in movies_of_genre(books, "action"):
#     print(f"{movie.director}: {movie.name}")