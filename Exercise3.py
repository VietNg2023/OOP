# Task 2
# class NumberStats:
#     def __init__(self):
#         #no need to add any new varibales here, just change the
#         #initialization of the self.numbers variable.
#         self.numbers = []

#     def add_number(self, number:int):
#         self.numbers.append(number)

#     def count_numbers(self):
#         return len(self.numbers)
    
#     def get_sum(self):
#         return sum(self.numbers)
    
#     def average(self):
#         return sum(self.numbers)/len(self.numbers)  
    
#if __name__ == "__main__":
#         #Part 1 test prints:
#         stats = NumberStats()
#         stats.add_number(3)
#         stats.add_number(5)
#         stats.add_number(1)
#         stats.add_number(2)
#         print("Numbers added:", stats.count_numbers())
#         print("Sum of numbers:", stats.get_sum())
#         print("Mean of numbers:", stats.average())
# Part 3,4
# def main():
#     stats = NumberStats()
#     stats_odd = NumberStats()
#     stats_even = NumberStats()
#     user_input = int(input('Please type in integer numbers:\n'))
#     while user_input != -1:
#         stats.add_number(user_input)
#         if user_input % 2 != 0:
#             stats_odd.add_number(user_input)
#         else:
#             stats_even.add_number(user_input)
#         user_input = int(input())
#     print("Numbers added:", stats.numbers)
#     print("Sum of numbers:", stats.get_sum())
#     print('Mean of the numbers', stats.average())
#     print('Sum of even numbers', stats_even.get_sum())
#     print('Sum of odd numbers', stats_odd.get_sum())
# main()
#Task 3:
# class LunchCard:
#     def __init__(self, balance: float):
#         self.balance = balance

#     def __str__(self):
#         content = f"The balance is {self.balance:.2f} euros"
#         return content

#     def deposit_money(self, amount: float):
#         if amount < 0:
#             raise ValueError("You cannot deposit an amount of money less than zero")
#         else:
#             self.balance += amount

#     def eat_ordinary(self):
#         if self.balance <= 2.95:
#             return False
#         else:
#             self.balance -= 2.95
    
#     def eat_luxury(self):
#         if self.balance <= 5.9:
#             return False
#         else:
#             self.balance -= 5.9

# if __name__ == "__main__":
#     #Part1
#     card = LunchCard(10)
#     print(card)
#     # card.eat_ordinary()
#     # print(card)
#     # card.eat_ordinary()
#     # card.eat_luxury()
#     # print(card)
#     card.deposit_money(15)
#     print(card)
#     card.deposit_money(10)
#     print(card)
#     card.deposit_money(200)
#     print(card)
#     # card.deposit_money(-10)
#     # print(card)
# Task 4:
# Write your solution after the ExamSubmission class
# DO NOT CHANGE THE CLASS
# class ExamSubmission:
#     def __init__(self, examinee: str, points: int):
#         self.examinee = examinee
#         self.points = points

#     def __str__(self):
#         return f'Exam submission (examinee: {self.examinee}, points: {self.points})'

# # WRITE YOUR OWN SOLUTION HERE:
# def passed(submissions: list, lowest_passing: int):
#     pass_list = []
#     for submission in submissions:
#         if submission.points >= lowest_passing:
#             pass_list.append(submission)
#     return pass_list
        
# #You may use the following code to test your function:

# if __name__ == "__main__":
#     s1 = ExamSubmission("Peter", 12)
#     s2 = ExamSubmission("Pippa", 19)
#     s3 = ExamSubmission("Paul", 15)
#     s4 = ExamSubmission("Phoebe", 9)
#     s5 = ExamSubmission("Persephone", 17)

#     passes = passed([s1, s2, s3, s4, s5], 15)
#     for passing in passes:
#         print(passing)
# Task 5:
# class LunchCard:
#     def __init__(self, balance: float):
#         self.balance = balance

#     def deposit_money(self, amount: float):
#         self.balance += amount

#     def subtract_from_balance(self, amount: float):
#         if self.balance < amount:
#             return False
#         else:
#             self.balance -= amount
#             return True
    
# class PaymentTerminal:
#     def __init__(self):
#         # Initially there is 1000 euros in cash available at the terminal
#         self.funds = 1000
#         self.ordinaries = 0
#         self.luxuries = 0

#     def eat_ordinary(self, payment: float):
#         if payment >= 2.95:
#             self.funds += 2.95
#             self.ordinaries += 1
#             change = payment - 2.95
#             return change

#     def eat_luxury(self, payment: float):
#         if payment >= 5.90:
#             self.funds += 5.90
#             self.luxuries += 1
#             change = payment - 5.90
#             return change
       
#     def eat_ordinary_lunchcard(self, card: LunchCard):
#         if card.balance >= 2.95:
#             self.funds += 2.95
#             self.luxuries += 1
#             card.balance -= 2.95
#             return True
#         else:
#             return False
        
#     def eat_luxury_lunchcard(self, card: LunchCard):
#         if card.balance >= 5.90:
#             self.funds += 5.90
#             self.luxuries += 1
#             card.balance -=5.90
#             return True
#         else:
#             return False
       
#     def deposit_money_on_card(self, card: LunchCard, amount: float):
#         card.balance += amount

# #You may use the following code to test your function:

# if __name__ == "__main__":
#     #Part1
#     # card = LunchCard(10)
#     # print("Balance", card.balance)
#     # result = card.subtract_from_balance(8)
#     # print("Payment successful:", result)
#     # print("Balance", card.balance)
#     # result = card.subtract_from_balance(4)
#     # print("Payment successful:", result)
#     # print("Balance", card.balance) 

#     #Part2
#     # exactum = PaymentTerminal()
#     # change = exactum.eat_ordinary(10)
#     # print("The change returned was", change)
#     # change = exactum.eat_ordinary(5.9)
#     # print("The change returned was", change)
#     # change = exactum.eat_luxury(5.9)
#     # print("The change returned was", change)
#     # print(f"Funds available at the terminal: {exactum.funds:.2f}")
#     # print("Ordinary lunches sold:", exactum.ordinaries)
#     # print("Luxury lunches sold:", exactum.luxuries)

#     #Part 3
#     # exactum = PaymentTerminal()

#     # change = exactum.eat_ordinary(10)
#     # print("The change returned was", change)

#     # card = LunchCard(8)

#     # result = exactum.eat_luxury_lunchcard(card)
#     # print("Payment successful:", result)
#     # result = exactum.eat_luxury_lunchcard(card)
#     # print("Payment successful:", result)
#     # result = exactum.eat_ordinary_lunchcard(card)
#     # print("Payment successful:", result)

#     # print("Funds available at the terminal:", exactum.funds)
#     # print("Regular lunches sold:", exactum.ordinaries)
#     # print("Special lunches sold:", exactum.luxuries)

#     #Part4
#     exactum = PaymentTerminal()

#     card = LunchCard(2)
#     print(f"Card balance is {card.balance} euros")

#     result = exactum.eat_luxury_lunchcard(card)
#     print("Payment successful:", result)

#     exactum.deposit_money_on_card(card, 100)
#     print(f"Card balance is {card.balance} euros")

#     result = exactum.eat_luxury_lunchcard(card)
#     print("Payment successful:", result)
#     print(f"Card balance is {card.balance} euros")

#     print("Funds available at the terminal:", exactum.funds)
#     print("Regular lunches sold:", exactum.ordinaries)
#     print("Special lunches sold:", exactum.luxuries)
#Task 6:
#Part 1:
# class Present():
#     def __init__(self,name,weight):
#         self.name = name
#         self.weight = weight
    
#     def __str__(self):
#         return f"{self.name.split(':')[-1].strip()} ({self.weight} g)"

# #Part 2:
# class Box():
#     def __init__(self):
#         self.total_weight_value = 0

#     def add_present(self,present: Present):
#         self.present = present
#         self.total_weight_value += int(present.weight)
    
#     def total_weight(self):
#         return self.total_weight_value

# book = Present("Ta-Nehisi Coates: The Water Dancer", 200)
# box = Box() 
# box.add_present(book) 
# print(box.total_weight())
# cd = Present("Pink Floyd: Dark Side of the Moon", 50) 
# box.add_present(cd)
# print(box.total_weight())

#Task 7:
# class Person():
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height

# class Room():
#     def __init__(self):
#         self.lists =[]
#         self.sum_height = 0
#         self.list_height=[]
#         self.min_height=0
#         self.removed = Person("None",0)
    
#     def add(self,person: Person):
#         self.lists.append(person)
    
#     def is_empty(self):
#         if len(self.lists) == 0:
#             return True
#         else: return False

#     def print_contents(self):
#         self.sum_height = 0
#         for person in self.lists:
#             self.sum_height += int(person.height)
#         print(f'There are {len(self.lists)} persons in the room, and their combined height is {self.sum_height} cm')
#         for person in self.lists:
#             print(f'{person.name} ({person.height} cm)')

#     def shortest(self):
#         if len(self.lists) != 0:
#             for person in self.lists:
#                 self.list_height.append(int(person.height))
#                 self.min_height = min(self.list_height)
#             for person in self.lists:
#                 if int(person.height)== self.min_height:
#                     return person.name
                
#     def remove_shortest(self):
#         if self.shortest():
#             self.removed.name = self.shortest()
#             for person in self.lists:
#                 if person.name == self.removed.name:
#                     self.lists.remove(person)
#         return self.removed
    

# room = Room()
# room.add(Person("Lea", 183)) 
# room.add(Person("Kenya", 172)) 
# room.add(Person("Ally", 166))
# room.add(Person("Nina", 162)) 
# room.add(Person("Dorothy", 175))
# print("Is the room empty?", room.is_empty()) 
# print("Shortest:", room.shortest())
# print()
# room.print_contents()
# removed = room.remove_shortest() 
# print(f"Removed from room: {removed.name}")
# print()
# room.print_contents()

# Task 8:
class Recording():
    def __init__(self, length_no: int):
        self.__length_no = length_no
    
    @property
    def length(self):
        return int(self.__length_no)
    
    @length.setter
    def length(self, new_length):
        self.__length_no = new_length
    
the_wall = Recording(43) 
print(the_wall.length) 
the_wall.length = 44 
print(the_wall.length)

# Task 9:
# class WeatherStation():
#     def __init__(self,name):
#         self.name = name
#         self.lists=[]

#     def __str__(self):
#         return f"{self.name},{len(self.lists)} observations"

#     def add_observation(self,observation: str):
#         self.lists.append(observation)
    
#     def latest_observation(self):
#         if len(self.lists) == 0:
#             return ""
#         else:
#             return self.lists[-1]
    
#     def number_of_observations(self):
#         return len(self.lists)
    
# station = WeatherStation("Houston") 
# station.add_observation("Rain 10mm") 
# station.add_observation("Sunny") 
# print(station.latest_observation())
# station.add_observation("Thunderstorm") 
# print(station.latest_observation())
# print(station.number_of_observations()) 
# print(station)

#Task 10:
# class BankAccount():
#     def __init__(self,name, acc_no: str, balance_no: float):
#         self.name = name
#         self.acc_no = acc_no
#         self.balance_no = balance_no

#     def deposit(self,amount: float):
#         self.balance_no += amount
#         self.__service_charge()


#     def withdraw(self,amount: float):
#         self.balance_no -= amount
#         self.__service_charge()

#     @property
#     def balance(self):
#         return self.balance_no
    
#     def __service_charge(self):
#         self.balance_no *= 0.99
    
# account = BankAccount("Randy Riches", "12345-6789", 1000)
# account.withdraw(100)
# print(account.balance)
# account.deposit(100)
# print(account.balance)