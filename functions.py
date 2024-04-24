# System Packages
import os.path
import csv
import random

# External Packages
## Add Colored ##

# Imported Packages

file_questions = "exam_questions.csv"
file_results = "exam_results.csv"
file_users = "exam_users.csv"

def welcome_screen():
    print("\nWelcome to the FIFA Laws of the Game Exam\n")

def user_check():
    try:
        user_file = open (file_users, "r")
        referee_email = input("Enter Email: ")
        
        user_found = False
        for line in user_file:
            item = line.strip().split(",")
            if referee_email == item[1]:
                user_found = True
                print("User Found!!! - Next Step, Password")
                break
        
        if user_found:
            current_attempts = 0
            expire_attempts = 3
            while current_attempts < expire_attempts:
                password_entered = input("Enter Password: ")
                item = line.strip().split(",")
                if password_entered == item[4]:
                    print("Password Correct")
                    user_file.close()
                    return
                else:
                    current_attempts += 1
                    print(f"Password Incorrect - {expire_attempts - current_attempts} attempts remaining")
            print("Too many attempts - Try again later")
            user_exit()
        else:
            print("User Not Found?!? - Next Step, Create New")
            create_new_user(referee_email)

    except FileNotFoundError:
        print('File Not Found, Creating New File')
        create_users_file()

def create_new_user(referee_email):
    referee_first_name = input("Enter First Name: ")
    referee_last_name = input("Enter Last Name: ")
    referee_password = input("Create New Password : ")
    referee_user_id = create_user_id()
    with open(file_users, "a") as f:
        writer = csv.writer(f)
        writer.writerow([referee_user_id,referee_email,referee_first_name, referee_last_name,referee_password,"False"])
    print(f"Thanks for registering {referee_first_name}.\nYour new Referee ID is {referee_user_id}")
    return

def create_user_id():
    return str(random.randint(10000,90000))

def create_users_file():
    while (not os.path.isfile(file_users)):
        user_file = open(file_users, "w")
        user_file.write("user_id,email,first_name,last_name,password,accredited\n")
        user_file.close()

def create_results_file():
    while (not os.path.isfile(file_results)):
        user_file = open(file_results, "w")
        user_file.write("userid,date,score,result\n")
        user_file.close()

def user_menu():
    print("Main Menu: \n 1. Take New Exam \n 2. View Previous Scores \n 3. View Personal Profile \n 4. Exit")
    
def menu_selection():
    user_selection = ""
    while user_selection != "4":
        user_menu()
        user_selection = input("Select Menu Number: ")
        print(f"You've chosen menu item {user_selection}")
        if user_selection == 1: # Take Exam
            print("You chose 1")
            #user_exam()

        elif user_selection == 2:
            print("You chose 2") # Previous Scores
            #user_scores

        elif user_selection == 3:
            print("You chose 3") # Personal Profile
            #user_profile

        elif user_selection == 4:
            print("You chose 4") #Logout
            user_exit()

        else:
            print("You have not made a valid selection")

# def user_scores():

# def user_profile():

# def user_exam():

def user_exit():
    print("\nThank you for participating in the FIFA LOTG Application. Goodbye\n")

    