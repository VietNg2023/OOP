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
import random
class Dice:
    def __init__(self):
        self.sides = 6
    
    def roll(self):
        return random.randint(1,self.sides)
    
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
# Task 7

            


    