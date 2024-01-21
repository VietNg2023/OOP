#Name: Exercise 1
#Author: Viet Nguyen
#Date: 12 Jan 2024
import random
#Task 2:
# my_numeric_list = []
# my_string_list = []
# my_random_list = []
# i=1
# while i < 11:
#     numeric_cont = int(input('Enter the number:'))
#     string_cont   = input('Enter the string:')
#     random_cont = random.randint(0,99)
#     my_numeric_list.append(numeric_cont)
#     my_string_list.append(string_cont)
#     my_random_list.append(random_cont)
#     i= i+1
# print(my_numeric_list)
# print(my_string_list)
# print(my_random_list)

# #Task 3:
# my_numeric_list.sort()
# my_string_list.sort()
# my_random_list.sort()
# print("After sorting")
# print(my_numeric_list)
# print(my_string_list)
# print(my_random_list)

#Task 4:
#Write a program which repeatedly reads integers until the user enters 0.
#Print out the number of negative integers. Use functions in your solution.    
# def task4(list_no,count_neg):
#     for i in list_no:
#         if i < 0:
#             count_neg += 1
#     return count_neg
    
# def task5(list_no,count_even):
#     for i in list_no:
#         if (i >= 0) and (i%2 == 0):
#             count_even += 1
#     return count_even

# def task6(list_no,total_sum_3):
#     for i in list_no:
#         if (i >= 0) and (i%3 == 0):
#             total_sum_3 += i
#     return total_sum_3
# if __name__ == "__main__":
#     int_no = 1
#     count_neg = 0
#     count_even = 0
#     total_sum_3 = 0
#     list_no = []
#     while int_no != 0:
#         int_no = int(input('Key in the number: '))
#         list_no.append(int_no)
#     count_neg = task4(list_no,count_neg)
#     print(f'No of negative number: {count_neg}' )
#     count_even = task5(list_no,count_even)
#     print(f'No of even number: {count_even}' )
#     total_sum_3 = task6(list_no,total_sum_3)
#     print(f'Total of number divisible by 3: {total_sum_3}' )

#Task 7:
# sum_i = 0
# sum_sq_i = 0
# i = 3
# no_i = 0
# list_i =[]
# maxi_no = int(input('Give the maximum number:'))
# while i <= maxi_no:
#     no_i = no_i + 1
#     sum_i = sum_i + i
#     sum_sq_i = sum_sq_i + i*i
#     list_i.append(i)
#     i = i + 3
# print(f'Procession is {list_i}')
# print(f'The number of terms: {no_i}')
# print(f'Total sum of the term: {sum_i}')
# print(f'Total sum of the square term: {sum_sq_i}')

#Task 8:
# user_win = 0
# computer_win = 0
# while user_win < 3 or computer_win < 3: 
#     words = ['rock', 'paper', 'scissors']

#     while True:
#         user_choice_temp = input('Give your choice(Rock,Paper,Scissors): ').strip()
#         user_choice = user_choice_temp.lower()
#         if user_choice in words:
#             print(f'You choose: {user_choice}')
#             break
#         else:
#             print('Wrong choice, try again')

#     computer_choice = random.choice(words)

#     match user_choice:
#         case "rock":
#             if computer_choice == 'rock':
#                 print('It is a tie!')
#             elif computer_choice == 'paper':
#                 print(f'Computer choice is {computer_choice}')
#                 print('Paper covers Rock')
#                 computer_win = computer_win + 1
#                 print(f'Computer {computer_win} You {user_win}')
#             else:
#                 print(f'Computer choice is {computer_choice}')
#                 print('Rock crushes Scissors')
#                 user_win = user_win + 1
#                 print(f'Computer {computer_win} You {user_win}')
#         case "paper":
#             if computer_choice == 'paper':
#                 print('It is a tie!')
#             elif computer_choice == 'scissors':
#                 print(f'Computer choice is {computer_choice}')
#                 print('Scissors cut Paper')
#                 computer_win = computer_win + 1
#                 print(f'Computer {computer_win} You {user_win}')
#             else:
#                 print(f'Computer choice is {computer_choice}')
#                 print('Rock crushes Scissors')
#                 user_win = user_win + 1
#                 print(f'Computer {computer_win} You {user_win}')
#         case "scissors":
#             if computer_choice == 'scissors':
#                 print('It is a tie!')
#             elif computer_choice == 'rock':
#                 print(f'Computer choice is {computer_choice}')
#                 print('Rock crushes Scissors')
#                 computer_win = computer_win + 1
#                 print(f'Computer {computer_win} You {user_win}')
#             else:
#                 print(f'Computer choice is {computer_choice}')
#                 print('Scissors cut Paper')
#                 user_win = user_win + 1
#                 print(f'Computer {computer_win} You {user_win}')
#     if user_win == 3:
#         print('Congrat! You won')
#         break
#     if computer_win == 3:
#         print('So sad! You lost')
#         break

# Task9:
# def ran_no():
#     random_number = random.randint(1,6)
#     return random_number

# random_number = ran_no()
# print(f'Random Number is {random_number}')

#Task 10:
phone_dict = {}
user_command = 0
while user_command != 3:
    user_command = input("command(1 search, 2 add, 3 quit): ")
    if int(user_command) == 2:
        name_add = input('name: ')
        number_add = input('number: ')
        phone_dict[name_add] = number_add
        print(phone_dict)
    elif int(user_command) == 1:
        name_search = input('name: ')
        if name_search in phone_dict:
            print(phone_dict[name_search])
        else:
            print('no number')
    elif int(user_command) == 3:
        break
    else:
        print('Wrong function chosen. Please do it again')