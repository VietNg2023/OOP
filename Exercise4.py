# #Task 1:
# class ListHelper():
#     def __init__(self):
#         self.lists = []
#         self.dic_lists = {}
#         self.dic_lists_2 = {}
#         self.max_fre = 0
#         self.greatest =[]
    
#     def greatest_frequency(self, my_lists:list):
#         self.lists = my_lists
#         for item in self.lists:
#             if item in self.dic_lists:
#                 self.dic_lists[item] +=1
#             else:
#                 self.dic_lists[item] = 1
#         self.max_fre = max(self.dic_lists.values())
#         self.greatest = [key for key, value in self.dic_lists.items() if value == self.max_fre]
#         return self.greatest
    
#     def double(self,my_lists:list):
#         no_appear_2_times = 0
#         self.lists = my_lists
#         for item in self.lists:
#             if item in self.dic_lists_2:
#                 self.dic_lists_2[item] += 1
#             else:
#                 self.dic_lists_2[item] = 1
#         for keys in self.dic_lists_2:
#             if self.dic_lists_2[keys] >= 2:
#                 no_appear_2_times += 1
#         return no_appear_2_times
            
# numbers =[1,1,2,1,3,3,4,5,5,5,6,5,5,5]
# helper = ListHelper()
# print(helper.greatest_frequency(numbers))
# print(helper.double(numbers))

#Task 2:
#Part 1:
# class Item():
#     def __init__(self,names, weight):
#         self.__name = names
#         self.__weight = weight
    
#     def name(self):
#         return self.__name
    
#     def weight(self):
#         return self.__weight
    
#     def __str__(self):
#         return f"{self.__name} ({self.__weight}g)"
    
# # book = Item("ABC Book",200) 
# # phone = Item("Nokia 3210",100)

# # print("Name of the book:", book.name()) 
# # print("Weight of the book:", book.weight())
# # print("Book:", book) 
# # print("Phone:", phone)
# # book.weight = 100
# # print("Book:", book) 

# #Part 2:
# class Suitcase():
#     def __init__(self,maxi_weigh):
#         self.__maxi_weigh = maxi_weigh
#         self.__curr_weigh = 0
#         self.__next_weigh = 0
#         self.item_suit = []
    
#     def add_item(self,item: Item):
#         self.__next_weigh = self.__curr_weigh + item.weight()
#         if self.__next_weigh <= self.__maxi_weigh:
#             self.__curr_weigh += item.weight()
#             self.item_suit.append(item)
    
#     def __str__(self):
#         no_items = len(self.item_suit)
#         if no_items >= 2:
#             return f"{no_items} items ({self.__curr_weigh}g)"
#         else:
#             return f"{no_items} item ({self.__curr_weigh}g)"
# #Part 4:    
#     def print_items(self):
#         for item in self.item_suit:
#             print(item)

#     def weight(self):
#         return self.__curr_weigh
# #Part 5
#     def heaviest_item(self):
#         max_weight = 0
#         for item in self.item_suit:
#             if max_weight < item.weight():
#                 max_weight = item.weight()
#         for item in self.item_suit:
#             if item.weight() == max_weight:
#                 heaviest=item
#         return heaviest

# #Part 6:
# class CargoHold():
#     def __init__(self,maxi_weigh):
#         self.__cargo_maxi_weigh = maxi_weigh*1000
#         self.__cargo_curr_weigh = 0
#         self.__cargo_next_weigh = 0
#         self.__cargo_rem_weigh = 0
#         self.suitcase_cargo = []

#     def add_suitcase(self,suitcase: Suitcase):
#         self.__cargo_next_weigh = self.__cargo_curr_weigh + suitcase.weight()
#         if self.__cargo_next_weigh <= self.__cargo_maxi_weigh:
#             self.__cargo_curr_weigh += suitcase.weight()
#             self.suitcase_cargo.append(suitcase)
    
#     def __str__(self):
#         no_suitcases = len(self.suitcase_cargo)
#         self.__cargo_rem_weigh = (self.__cargo_maxi_weigh - self.__cargo_curr_weigh)/1000
#         return f"{no_suitcases} suitcases, space for {self.__cargo_rem_weigh}kg"
    
#     def print_items(self):
#         for suitcase in self.suitcase_cargo:
#             suitcase.print_items()

# book = Item("ABC Book", 200) 
# phone = Item("Nokia 3210", 100) 
# brick = Item("Brick", 400)
# suitcase = Suitcase(1000) 
# print(suitcase)
# suitcase.add_item(book)
# print(suitcase)
# suitcase.add_item(phone)
# print(suitcase)
# suitcase.add_item(brick)
# print(suitcase)
# #Part 4:
# suitcase.print_items()
# combined_weight = suitcase.weight()
# print(f"Combined weight: {combined_weight} g")
# #Part 5:
# heaviest = suitcase.heaviest_item() 
# print(f"The heaviest item: {heaviest}")
#Part 6:
# cargo_hold = CargoHold(100) 
# print(cargo_hold)
# book = Item("ABC Book", 200) 
# phone = Item("Nokia 3210", 100)
# brick = Item("Brick", 400)
# adas_suitcase = Suitcase(1000) 
# adas_suitcase.add_item(book) 
# adas_suitcase.add_item(phone)

# peters_suitcase = Suitcase(1000) 
# peters_suitcase.add_item(brick)

# cargo_hold.add_suitcase(adas_suitcase)
# print(cargo_hold)

# cargo_hold.add_suitcase(peters_suitcase) 
# print(cargo_hold)

# print("The suitcases in the cargo hold contain the following items:") 
# cargo_hold.print_items()

#Task 3:
# class Computer():
#     def __init__(self,model,speed):
#         self.model = model
#         self.speed = speed

# class LaptopComputer(Computer):
#     def __init__(self,model,speed,weight: int):
#         super().__init__(model,speed)
#         self.weight = weight

#     def __str__(self):
#         return f"{self.model}, {self.speed} MHz, {self.weight} kg"

# laptop = LaptopComputer("NoteBook Pro15", 1500, 2) 
# print(laptop)

#Task 4:
# class ComputerGame():
#     def __init__(self,name,producer,year):
#         self.name = name
#         self.producer = producer
#         self.year = year

# class GameWarehouse():
#     def __init__(self, game: ComputerGame):
#         self.game = game
    
# class GameMuseum(GameWarehouse):
#     def __init__(self):
#         game_dummy = ComputerGame("", "", 0)
#         super().__init__(game_dummy)
#         self.game_lists =[]
#         self.name_lists =[]
    
#     def add_game(self,game: ComputerGame):
#         self.game_lists.append(game)

#     def list_games(self):
#         for game in self.game_lists:
#             if game.year < 1990:
#                 self.name_lists.append(game)
#         return self.name_lists

# museum = GameMuseum()
# museum.add_game(ComputerGame("Pacman", "Namco", 1980)) 
# museum.add_game(ComputerGame("GTA 2", "Rockstar", 1999))
# museum.add_game(ComputerGame("Bubble Bobble", "Taito", 1986)) 
# for game in museum.list_games():
#     print(game.name)

#Task 5:
# SECRET MAGIC POTION:
# class MagicPotion:
#     def __init__(self, name: str):
#         self._name = name
#         self._ingredients = []

#     def add_ingredient(self, ingredient: str, amount: float):
#         self._ingredients.append((ingredient, amount))

#     def print_recipe(self):
#         print(self._name + ":")
#         for ingredient in self._ingredients:
#             print(f"{ingredient[0]} {ingredient[1]} grams")

# class SecretMagicPotion(MagicPotion):
#     def __init__(self, name:str, password:str):
#         super().__init__(name)
#         self.password = password
    
#     def add_ingredient(self,ingredient: str, amount: float, password: str):
#         if password == self.password:
#             super().add_ingredient(ingredient,amount)
#         else:
#             raise ValueError("Wrong password!")
        
#     def print_recipe(self,password: str):
#         if password == self.password:
#             super().print_recipe()
#         else:
#             raise ValueError("Wrong password!")
        
# diminuendo = SecretMagicPotion("Diminuendo maximus", "hocuspocus")
# diminuendo.add_ingredient("Toadstool", 1.5, "hocuspocus")
# diminuendo.add_ingredient("Magic sand", 3.0, "hocuspocus")
# diminuendo.add_ingredient("Frogspawn", 4.0, "hocuspocus")
# diminuendo.print_recipe("hocuspocus") 
# diminuendo.print_recipe("pocushocus") # WRONG password!

#Task 6:Part 1-2
# import random
# class Dice:
#     def __init__(self):
#         self.sides = 6
    
#     def roll(self):
#         return random.randint(1,self.sides)
    
# # class roll_n_times():
# #     def __init__(self,number):
# #         self.number = number
    
# #     def sum_n(self,dice:Dice):
# #         sum_n_time = 0
# #         for i in range(self.number):
# #             roll_result = dice.roll()
# #             print(f"{i+1} times: roll {roll_result}")
# #             sum_n_time += roll_result
# #         return sum_n_time
# Part 1,2
# class Game():
#     def __init__(self,number_player, rolls_per_player):
#         self.number_player = number_player
#         self.rolls_per_player = rolls_per_player
#         self.scores={}
    
#     def play_round(self):
#         dice = Dice()
#         for player in range(1,self.number_player +1):
#             player_score = sum(dice.roll()for _ in range(self.rolls_per_player))
#             print(f"Player {player} score: {player_score}")
#             self.scores[player] = player_score
    
#     def determine_winner(self):
#         max_score = max(self.scores.values())
#         winners = [player for player, score in self.scores.items() if score == max_score]

#         while len(winners) > 1:
#             print("Tie! Roll again")
#             self.play_round()
#             max_score = max(self.scores.values())
#             winners = [player for player, score in self.scores.items() if score == max_score]
        
#         return winners
# if __name__ == "__main__":
    # num_of_roll = int(input('How many rolls do you want to play:'))
    # num_of_players = int(input('How many players: '))
    # game = Game(num_of_players, num_of_roll)
    # game.play_round()
    # winners = game.determine_winner()
    # print(f"Player {winners[0]} wins with a score of {game.scores[winners[0]]}"
# Part 3
# class Player():
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id

#     def __str__(self):
#         return f"Player {self.name} has the id is {self.id}"
# class Game():
#     def __init__(self,players, rolls_per_player):
#         self.players = players
#         self.rolls_per_player = rolls_per_player
#         self.scores={}
    
#     def play_round(self):
#         for key in self.players:
#             print(key.name, key.id)
#             player_score = sum(self.players[key].roll() for _ in range (self.rolls_per_player))
#             print(f"Has score after {self.rolls_per_player} rolls: {player_score}")
#             self.scores[key.name] = player_score
#             # print(self.scores)
    
#     def determine_winner(self):
#         max_score = max(self.scores.values())
#         winners = [player for player, score in self.scores.items() if score == max_score]

#         while len(winners) > 1:
#             print("Tie! Roll again")
#             self.play_round()
#             max_score = max(self.scores.values())
#             winners = [player for player, score in self.scores.items() if score == max_score]
        
#         return winners
# # Part 3
# if __name__ == "__main__":
#     players_dict ={}
#     a = Player("EUR","012024")
#     b= Player("CAD","022024")
#     dice_a = Dice()
#     dice_b = Dice()
#     players_dict[a] = dice_a
#     players_dict[b] = dice_b
#     num_of_roll = 4
#     game = Game(players_dict, num_of_roll)
#     game.play_round()
#     winners = game.determine_winner()
#     print(f"Player {winners[0]} wins with a score of {game.scores[winners[0]]}")
# Part 4,5:
# class Player():
#     def __init__(self,name,id,mammal):
#         self.name = name
#         self.id = id
#         self.mammal = mammal

#     def __str__(self):
#         return f"Player {self.name} has the id is {self.id} and he has a"
# class Mammal():
#     def __init__ (self, ID, species, name, size, weight):
#         self.id = ID
#         self.species = species
#         self.name = name
#         self.size = size
#         self.weight = weight
    
#     def __str__(self):
#         return f"mammal: a {self.weight} kg {self.species}, its name {self.name}"
# # Part 5
# if __name__ == "__main__":
#     dog1 = Mammal("1","Husky","Bestie","Big","16")
#     cat1  = Mammal("1","Black","Miu","Normal","4")
#     a = Player("EUR","012024",dog1)
#     b= Player("CAD","022024",cat1)
#     print(a, a.mammal)
#     print(b, b.mammal)
# Part 6:
# class Player():
#     def __init__(self,name,id,mammal):
#         self.name = name
#         self.id = id
#         self.mammal = mammal

#     def __str__(self):
#         return f"Player {self.name} has the id is {self.id} and he has a"
    
# class Mammal():
#     def __init__ (self, ID, species, name, size, weight: int):
#         self.id = ID
#         self.species = species
#         self.name = name
#         self.size = size
#         self.weight = weight
    
#     def __str__(self):
#         return f"mammal: a {self.weight} kg {self.species}, its name {self.name}"
    
# class Score():
#     def __init__(self,players, rolls_per_player = 2):
#         self.players = players
#         self.rolls_per_player = rolls_per_player
#         self.scores={}
#         self.sorted_score= {}
    
#     def play_round(self):
#         for key in self.players:
#             #print(key.name, key.id)
#             player_score = sum(self.players[key].roll() for _ in range (self.rolls_per_player))
#             self.scores[key.name] = player_score
#             #print(self.scores)
#         self.sorted_score = dict(sorted(self.scores.items(), key=lambda item: item[1], reverse=True))
#         return(self.sorted_score)

# if __name__ == "__main__":
#     dog1 = Mammal("1","Husky","Bestie","Big",16)
#     cat1  = Mammal("2","Black","Miu","Normal",4)
#     duck1 = Mammal("3","Duck1","Quack1","Normal",8)
#     duck2 = Mammal("4","Duck2","Quack2","Normal",7)
#     duck3 = Mammal("5","Duck3","Quack3","Normal",6)
#     duck4 = Mammal("6","Duck4","Quack4","Normal",5)
#     duck5 = Mammal("7","Duck5","Quack5","Normal",9)
#     dummy = Mammal("NoId","NoSpecies","NoName","NoSize",0)
#     mammal_list = [dog1,cat1,duck1,duck2,duck3,duck4,duck5]
#     #sort weight of mammal
#     mammal_list.sort(key = lambda x: x.weight, reverse = True)
#     for mammal in mammal_list:
#         print(mammal)
#     print(mammal_list)
#     players_dict ={}
#     a = Player("EUR","012024",dummy)
#     b = Player("CAD","022024",dummy)
#     c = Player("USD","032024",dummy)
#     dice_a = Dice()
#     dice_b = Dice()
#     dice_c = Dice()
#     players_dict[a] = dice_a
#     players_dict[b] = dice_b
#     players_dict[c] = dice_c
#     score = Score(players_dict,2)
#     #Roll the dice
#     players_score = score.play_round()
#     print(players_score)
#     # Assign the mammal obj to the score
#     new_dict ={}
#     for mammal, score in zip(mammal_list, players_score.values()):
#         new_dict[mammal] = score
#     print(new_dict)
#     player_mammal={}
#     # Assign the player with the mammal obj
#     for key,value in new_dict.items():
#         for player,score in players_score.items():
#             if score == value:
#                 player_mammal[player] = key
#     print(player_mammal)
#     for key, value in player_mammal.items():
#         for player in players_dict.keys():
#             if player.name == key :
#                 player.mammal = value
# # In result
#     for player in players_dict.keys():
#         print(player.name)
#         print(player.id)
#         print(player.mammal)
# Task 7 Part 1
# class Person():
#     def __init__(self,name):
#         self.name_str = name
#         self.phone_number = []
#         self.addresses = None
    
#     def add_number(self,num:str):
#         self.phone_number.append(num)

#     def add_address(self,address:str):
#         self.addresses = address

#     def name(self):
#         return self.name_str
    
#     def address(self):
#         return self.addresses
    
#     def numbers(self):
#         return self.phone_number

# # person = Person("Eric")
# # print(person.name())
# # print(person.numbers())
# # print(person.address()) 
# # person.add_number("040-123456") 
# # person.add_address("Mannerheimintie 10 Helsinki") 
# # print(person.numbers())
# # print(person.address())
# # Part 2
# class PhoneBook:
#     def __init__(self):
#         self.__persons = {}

#     def add_number(self, name: str, number: str):
#         if not name in self.__persons:
#             self.__persons[name] = Person(name)
#         self.__persons[name].add_number(number)

#     def add_add(self, name: str, address: str):
#         if not name in self.__persons:
#             self.__persons[name] = Person(name)
#         self.__persons[name].add_address(address)

#     def get_numbers(self, name: str):
#         person = self.__persons.get(name)
#         if person:
#             return person.numbers()
#         else:
#             return None
#     def get_address(self, name: str):
#         person = self.__persons.get(name)
#         if person:
#             return person.address()
#         else:
#             return None
# # phonebook = PhoneBook()
# # phonebook.add_number("Eric", "02-123456")
# # print(phonebook.get_numbers("Eric"))
# # print(phonebook.get_numbers("Emily")) 
# # Part 3:
# class PhoneBookApplication:
#     def __init__(self):
#         self.__phonebook = PhoneBook()
#         self.__filehandler = FileHandler("phonebook.txt")

#         # add the names and numbers from the file to the phone book
#         for name, numbers in self.__filehandler.load_file().items():
#             for number in numbers:
#                 self.__phonebook.add_number(name, number)

#     def help(self):
#         print("commands: ")
#         print("0 exit")
#         print("1 add entry")
#         print("2 search")
#         print("3 add address")

#     def add_entry(self):
#         name = input("name: ")
#         number = input("number: ")
#         self.__phonebook.add_number(name, number)
    
#     def add_address_user(self):
#         name = input("name: ")
#         address = input("address: ")
#         self.__phonebook.add_add(name, address)

#     def search(self):
#         name = input("name: ")
#         numbers = self.__phonebook.get_numbers(name)
#         address = self.__phonebook.get_address(name)
#         if numbers == None:
#             print("number unknown")
#             return
#         for number in numbers:
#             print(number)
#         if address == None:
#             print("address unknown")
#             return
#         print(address)

#     def exit(self):
#         self.__filehandler.save_file(self.__phonebook.all_entries())

#     def execute(self):
#         self.help()
#         while True:
#             print("")
#             command = input("command: ")
#             if command == "0":
#                 self.exit()
#                 break
#             elif command == "1":
#                 self.add_entry()
#             elif command == "2":
#                 self.search()
#             elif command == "3":
#                 self.add_address_user()
#             else:
#                 self.help()

# class FileHandler():
#     def __init__(self, filename):
#         self.__filename = filename

#     def load_file(self):
#         names = {}
#         with open(self.__filename) as f:
#             for line in f:
#                 parts = line.strip().split(';')
#                 name, *numbers = parts
#                 names[name] = numbers

#         return names

#     def save_file(self, phonebook: dict):
#         with open(self.__filename, "w") as f:
#             for name, numbers in phonebook.items():
#                 line = [name] + numbers
#                 f.write(";".join(line) + "\n")

# application = PhoneBookApplication()
# application.execute()

#Task 8-Part 1
# class Task():
#     last_id = 0
#     def __init__(self,task_name,developer,workload):
#         Task.last_id += 1
#         self.description = task_name
#         self.programmer = developer
#         self.workload = workload
#         self.id = Task.last_id
#         self.status = "NOT FINISHED"

#     def __str__(self):
#         return f"{self.id}: {self.description} ({self.workload} hours),programmer {self.programmer} {self.status}"
    
#     def mark_finished(self):
#         self.status = "FINISHED"
    
#     def is_finished(self):
#         return True if self.status == "FINISHED" else False

# t1 = Task("program hello world", "Eric", 3)
# print(t1.id, t1.description, t1.programmer, t1.workload) 
# print(t1)
# print(t1.is_finished())
# t1.mark_finished()
# print(t1)
# print(t1.is_finished())
# t2 = Task("program webstore", "Adele", 10)
# t3 = Task("program mobile app for workload accounting", "Eric", 25) 
# print(t2)
# print(t3)
# Part 2:
# class OrderBook():
#     def __init__(self):
#         self.order_list = []
#         self.programmer_list_temp = []
#         self.programmer_list = []
#         self.finished_list = []
#         self.unfinished_list = []
        
#     def add_order(self, description, programmer, workload):
#         new_order = Task(description,programmer,workload)
#         self.order_list.append(new_order)
#         self.unfinished_list.append(new_order) 
#         name = new_order.programmer
#         self.programmer_list_temp.append(name)
#         self.programmer_list = list(set(self.programmer_list_temp))
    
#     def all_orders(self):
#         return self.order_list
    
#     def programmers(self):
#         return self.programmer_list
    
#     def mark_finished(self, id : int):
#         found = False
#         for order in self.order_list:
#             if order.id == id:
#                 order.status = "FINISHED"
#                 self.finished_list.append(order)
#                 found = True
#             # else:
#             #     self.unfinished_list.append(order)
#         if found:
#             self.unfinished_list = [order for order in self.order_list if order.status != "FINISHED"]
#         else:
#             raise ValueError("Wrong ID!")

#     def finished_orders(self):
#         return self.finished_list
    
#     def unfinished_orders(self):
#         return self.unfinished_list
    
#     def status_of_programmer(self, programmer: str):
#         no_finish_tasks = 0
#         no_unfinish_tasks = 0
#         no_finish_hours = 0
#         no_unfinish_hours = 0
#         found = False
#         for order in self.order_list:
#             if order.programmer == programmer:
#                 found = True
#                 if order.status =="FINISHED":
#                     no_finish_tasks += 1
#                     no_finish_hours += order.workload
#                 else:
#                     no_unfinish_tasks += 1
#                     no_unfinish_hours += order.workload
#         if found == False:
#             raise ValueError("Wrong Name!")
#         result = (no_finish_tasks,no_unfinish_tasks,no_finish_hours,no_unfinish_hours)
#         return result    
# # Part 4
# class OrderApplication():
#     def __init__(self):
#         self.__orderbook = OrderBook()

#     def help(self):
#         print("commands: ")
#         print("0 exit")
#         print("1 add orders")
#         print("2 list finished tasks")
#         print("3 list unfinished tasks")
#         print("4 mark tasks as finished")
#         print("5 programmers")
#         print("6 status of programmers")

#     def add_orders(self):
#         description = input("description: ")
#         programmer_workload = input("programmer and workload estimate: ")
#         parts = programmer_workload.split()
#         if len(parts) != 2:
#             print("erroneous input")
#             return
#         programmer, workload_str = parts

#         if not workload_str.isdigit():
#             print("erroneous input")
#             return

#         workload = int(workload_str)
#         self.__orderbook.add_order(description, programmer,workload)
#         print("added!")
        
    
#     def finish_order(self):
#         results = self.__orderbook.finished_orders()
#         if not results:
#             print("No finished tasks")
#         else:
#             print("Finished tasks:")
#             for result in results:
#                 print(result)
    
#     def unfinish_order(self):
#         results = self.__orderbook.unfinished_orders()
#         if not results:
#             print("No unfinished tasks")
#         else:
#             print("Unfinished tasks:")
#             for result in results:
#                 print(result)

#     def mark_as_finish(self):
#         id = input("id: ")
#         if not id.isdigit():
#             print("erroneous input")
#             return
#         else:
#             self.__orderbook.mark_finished(id)
#             print("marked as finished")
#             return

#     def programmer_list(self):
#         results = self.__orderbook.programmers()
#         for result in results: 
#             print(result)
    
#     def status_programmer(self):
#         name = input("programmer:")
#         results = self.__orderbook.status_of_programmer(name)
#         print(f"tasks: finished {results[0]} not finished {results[1]}, hours: finished {results[2]} not finished {results[3]}")

#     def execute(self):
#         self.help()
#         while True:
#             print("")
#             command = input("command: ")
#             if command == "0":
#                 self.exit()
#                 break
#             elif command == "1":
#                 self.add_orders()
#             elif command == "2":
#                  self.finish_order()
#             elif command == "3":
#                  self.unfinish_order()
#             elif command == "4":
#                  self.mark_as_finish()
#             elif command == "5":
#                  self.programmer_list()
#             elif command == "6":
#                  self.status_programmer()
#             else:
#                 self.help()
# application = OrderApplication()
# application.execute()
# Part 1
# orders = OrderBook()
# orders.add_order("program webstore", "Adele", 10) 
# orders.add_order("program mobile app for workload accounting", "Eric", 25)
# orders.add_order("program app for practising mathematics", "Adele", 100)
# for order in orders.all_orders(): 
#     print(order)
# print()
# for programmer in orders.programmers(): 
#     print(programmer)
    
# Part 2
# orders.mark_finished(1)
# orders.mark_finished(2)
# #orders.mark_finished(4)
# for order in orders.all_orders(): 
#     print(order)
# print("Order finish")  
# for order_finish in orders.finished_list: 
#      print(order_finish)
# print("Order Unfinish")    
# for order_unfinish in orders.unfinished_list: 
#      print(order_unfinish)

# Part 3
# orders = OrderBook()
# orders.add_order("program webstore", "Adele", 10)
# orders.add_order("program mobile app for workload accounting", "Adele", 25) 
# orders.add_order("program app for practising mathematics", "Adele", 100) 
# orders.add_order("program the next facebook", "Eric", 1000)
# orders.mark_finished(1) 
# orders.mark_finished(2)
# status = orders.status_of_programmer("Adele") 
# print(status)
# status2 = orders.status_of_programmer("Mama") 
# print(status)

# Task 9
# Part 1
import json

class StatisticsApplication():
    def __init__(self):
        with open("part.json") as my_file:
            self.data = my_file.read()
        self.datas = json.loads(self.data)

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from countru")
        print("6 most points")
        print("7 most goals")

    def search(self):
        name = input("name of player: ")
        found = False
        for data in self.datas:
            if data["name"] == name:
                print(f"{data['name']} {data['team']} {data['goals']} + {data['assists']} = {data['goals'] +data['assists']}")
                found = True
        if not found:
            print('Player not found')
    
    def team(self):
        team_temp=[]
        for data in self.datas:
            team_temp.append(data['team'])
        team = list(set(team_temp))
        team.sort()
        for i in team:
            print(i)
    
    def countries(self):
        countries_temp=[]
        for data in self.datas:
            countries_temp.append(data['nationality'])
        countries = list(set(countries_temp))
        countries.sort()
        for i in countries:
            print(i)
    
    def player_team(self):
        team = input("name of team: ")
        new_teams =[]
        found = False
        for data in self.datas:
            if data["team"] == team:
                new_teams.append(data)
                found = True
        if not found:
            print('Team not found')
        for team in new_teams:
            team['score'] = team['goals'] + team['assists']
        sorted_teams =  sorted(new_teams, key = lambda x: x['score'], reverse = True)
        for data in sorted_teams:
            print(f"{data['name']} \t {data['team']} \t {data['goals']} + {data['assists']} = {data['goals'] +data['assists']}")
    
    def player_country(self):
        country = input("name of country: ")
        new_countries =[]
        found = False
        for data in self.datas:
            if data["nationality"] == country:
                new_countries.append(data)
                found = True
        if not found:
            print('Team not found')
        for country in new_countries:
            country['score'] = country['goals'] + country['assists']
        sorted_country =  sorted(new_countries, key = lambda x: x['score'], reverse = True)
        for data in sorted_country:
            print(f"{data['name']} \t {data['team']} \t {data['goals']} + {data['assists']} = {data['goals'] +data['assists']}")
    
    def most_points(self):
        number = int(input('how many: '))
        new_list = self.datas
        for data in new_list:
            data['score'] = data['goals'] + data['assists']
        sorted_list =  sorted(new_list, key = lambda x: (x['score'],x['goals']), reverse = True)
       # for data in sorted_list:
        for i, data in enumerate(sorted_list[:number]):
            print(f"{data['name']} \t {data['team']} \t {data['goals']} + {data['assists']} = {data['goals'] +data['assists']}")

    
    def most_goals(self):
        how_many = int(input('how many: '))
        goals_list = []
        for data in self.datas:
            goals_list.append(data['goals'])
        goals_list.sort(reverse = True)
        print(goals_list)
        for i in range(how_many):
            for data in self.datas:
                if goals_list[i] == data['goals']:
                    print(f"{data['name']} \t {data['team']} \t {data['goals']} + {data['assists']} = {data['goals'] +data['assists']}")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                self.exit()
                break
            elif command == "1":
                self.search()
            elif command == "2":
                 self.team()
            elif command == "3":
                 self.countries()
            elif command == "4":
                 self.player_team()
            elif command == "5":
                 self.player_country()
            elif command == "6":
                 self.most_points()
            elif command == "7":
                 self.most_goals()
            else:
                self.help()
application = StatisticsApplication()
application.execute()