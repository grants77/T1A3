# System Packages
import os.path
import csv
import random

# External Packages
## Add Colored ##
## Add password masking ##
## Add Date Time ##

# Imported Packages

file_questions = "exam_questions.csv"
file_results = "exam_results.csv"
file_users = "exam_users.csv"
referee_email = None
user_details = {}

# Welcome Text
def welcome_screen():
    print("\nWelcome to the FIFA Laws of the Game Exam\n")

# Login Function
def user_check():
    global referee_email, user_details
    try:
        user_file = open (file_users, "r")
        referee_email = input("Enter Email: ")
        
        user_found = False
        for line in user_file:
            item = line.strip().split(",")
            if referee_email == item[1]:
                user_found = True
                print("User Found!!! - Next Step, Password")
                user_details = user_finder(referee_email)
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
                    menu_selection()
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
        print("File Not Found, Creating New File")
        create_users_file()

# Retains user details on login for future use
def user_finder(referee_email):
    with open(file_users, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['email'] == referee_email:
                user_details = row
                break
    return user_details

# Created a new user in csv file
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

# Generates random number for user_id
def create_user_id():
    return str(random.randint(10000,90000))

# Generates user file if none exists
def create_users_file():
    while (not os.path.isfile(file_users)):
        user_file = open(file_users, "w")
        user_file.write("user_id,email,first_name,last_name,password,accredited\n")
        user_file.close()

# Generates results file if none exists
def create_results_file():
    while (not os.path.isfile(file_results)):
        user_file = open(file_results, "w")
        user_file.write("userid,date,score,result\n")
        user_file.close()

# Menu Options
def user_menu():
    print("Main Menu: \n 1. Take New Exam \n 2. View Previous Scores \n 3. View Personal Profile \n 4. Exit")
    
# Determines next step when menu item selected
def menu_selection():
    user_selection = ""
    while user_selection != "4":
        user_menu()
        user_selection = input("Select Menu Number: ")
        print(f"You've chosen menu item {user_selection}")
        if user_selection == "1": # Take Exam
            print("You chose 1")
            #user_exam()

        elif user_selection == "2":
            print("You chose 2") # Previous Scores
            #user_scores

        elif user_selection == "3":
            print("You chose 3") # Personal Profile
            user_profile(referee_email)
            break

        elif user_selection == "4":
            print("You chose 4") #Logout
            user_exit()

        else:
            print("You have not made a valid selection")

# Menu Item 3 - Personal Profile
def user_profile(email):
    user_id = user_details.get("user_id")
    last_name = user_details.get("last_name")
    first_name = user_details.get("first_name")
    referee_email = user_details.get("email")
    accredited = user_details.get("accredited")
    print(f"\nRegistration Number: {user_id}\nName: {last_name}, {first_name}\nEmail: {referee_email}\nAccredited: {accredited}\n")
    return_or_exit()

# Exit Message
def user_exit():
    print("\nThank you for participating in the FIFA LOTG Application. Goodbye\n")

def return_or_exit():
    print("Do you want to return to the main menu?")
    decision = input('Enter "Y" to return, or "exit" to leave the application: ').lower()
    if decision == "Y":
        menu_selection()
    elif decision == "exit":
        user_exit()
    else:
        print("Invalid entry, try again")
        return_or_exit()