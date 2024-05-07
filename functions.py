# System Packages
import os.path
import csv
import random
from datetime import datetime

# External Packages
from colored import Fore, Back, Style
import maskpass


file_questions = "exam_questions.csv"
file_results = "exam_results.csv"
file_users = "exam_users.csv"
referee_email = None
user_details = {}



########## LOGIN AND USER MENU ##########

# Login or Register Function
def user_check():
    global referee_email, user_details
    try:
        user_file = open (file_users, "r")
        print(f"\nWelcome to the FIFA Laws of the Game Exam") 
        referee_email = input(" \nEnter Email: ")
        
        user_found = False
        for line in user_file:
            item = line.strip().split(",")
            if referee_email == item[1]:
                user_found = True
                user_details = user_finder(referee_email)
                print("\nWelcome Back!\n")
                break
        
        if user_found:
            current_attempts = 0
            expire_attempts = 3
            while current_attempts < expire_attempts:
                password_entered = maskpass.askpass(mask="#")
                item = line.strip().split(",")
                if password_entered == item[4]:
                    print("Password Correct")
                    menu_selection()
                    return
                else:
                    current_attempts += 1
                    print(f"Password Incorrect - {expire_attempts - current_attempts} attempts remaining")
            print("Too many attempts - Try again later")
            user_exit()

        else:
            print("User Not Found?!? - Next Step, Create New")
            user_details = create_new_user(referee_email)
            menu_selection()

    except FileNotFoundError:
        print("File Not Found, Creating New File")
        create_users_file()
        user_check()
   
# Determines next step when menu item selected
def menu_selection():
    user_selection = ""
    while user_selection != "5":

        user_menu()
        user_selection = input("Select Menu Number: ")
        if user_selection == "1": # Take Exam
            user_exam()
            return

        elif user_selection == "2": # Previous Results
            user_results()
            return

        elif user_selection == "3": # Personal Profile
            user_profile(referee_email)
            return

        elif user_selection == "4": # Logout
            print("\nYou have been logged out of the FIFA LOTG Application")
            user_check()
            return
        
        elif user_selection == "5": # Exit
            user_exit()
            return

        else:
            print("\nYou have not made a valid selection. Please try again.")

# Menu Options
def user_menu():
    print("\nMain Menu: \n 1. Take New Exam \n 2. View Previous Scores \n 3. View Personal Profile \n 4. Logout \n 5. Exit")

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
    referee_password = maskpass.askpass(prompt="New Password: ", mask="#")
    referee_user_id = create_user_id()
    with open(file_users, "a") as f:
        writer = csv.writer(f)
        writer.writerow([referee_user_id,referee_email,referee_first_name, referee_last_name,referee_password,"False"])
    print(f"\nThanks for registering {referee_first_name}.\nYour new Referee ID is {referee_user_id}")
    return {
        "user_id": referee_user_id,
        "email": referee_email,
        "first_name": referee_first_name,
        "last_name": referee_last_name,
        "accredited": "False"
    }

# Generates random number for user_id
def create_user_id():
    return str(random.randint(10000,90000))

# Generates user file if none exists
def create_users_file():
    while (not os.path.isfile(file_users)):
        user_file = open(file_users, "w")
        user_file.write("user_id,email,first_name,last_name,password,accredited\n")
        user_file.close()



########## PERSONAL PROFILE ##########

# Menu Item 3 - Personal Profile
def user_profile(email):
    user_id = user_details.get("user_id")
    last_name = user_details.get("last_name")
    first_name = user_details.get("first_name")
    referee_email = user_details.get("email")
    accredited = user_details.get("accredited")
    print(f"\nRegistration Number: {user_id}\nName: {last_name}, {first_name}\nEmail: {referee_email}\nAccredited: {accredited}\n")
    return_or_exit()



########## PREVIOUS RESULTS ##########

# Menu Item 2 - Previous Results
def user_results():
    try:
        user_id = user_details.get("user_id")
        with open(file_results, 'r') as f:
            reader = csv.reader(f)
            found_results = False
            print("\n             Previous Results \n--------------------------------------------\n|        Date       |     Name    | Score ")
            for row in reader:
                if row[0] == user_id:
                    print(f"| {row[4]} | {row[1]} {row[2]} |   {row[5]}   ")
                    found_results = True
            if not found_results:
                print("\nNo results exist for this user")
            return_or_exit()
    except FileNotFoundError:
        print("\nNo results exist for this user")
        create_results_file()
        return_or_exit()

# Generates results file if none exists
def create_results_file():
    while (not os.path.isfile(file_results)):
        user_file = open(file_results, "w")
        user_file.write("user_id,first_name,last_name,email,date_time,score\n")



##########  REFEREE EXAM ##########

# Menu Item 1 - Runs the Exam
def user_exam():
    print("\nWelcome to the FIFA Laws of the Game Exam.\n\nThere are 10 questions in this exam, with a pass mark of 80%\n\nYou must answer TRUE or FALSE to each of the questions.\n\nIf you wish to exit the exam without saving your results, type EXIT as the answer to the question.\n\nGoodluck!\n\n")
    exam = {}
    user_tally = 0
    with open(file_questions, 'r') as f:
        reader = csv.reader(f)
        questions = list(reader)
        random.shuffle(questions)
        exam_questions = questions[:10]
        
        for row in exam_questions:
            question, answer = row[0], row[1]
            exam[question] = answer

        for question, correct_answer in exam.items():
            print(f"{Fore.black}{Back.white}{Style.bold}{question}{Style.reset}")
            while True:
                user_answer  = input(f"{Fore.white}{Back.black}{Style.bold}Enter 'True' or 'False': ").strip().lower()
                print(f"{Style.reset}")
                if user_answer == "exit":
                    user_exit()
                    return
                elif user_answer in ["true", "false"]:
                    break
                else:
                    print(f"{Back.red}{Fore.white}Invalid input. You must enter TRUE, FALSE or EXIT.{Style.reset}\n")
            if user_answer == correct_answer.lower():
                user_tally += 1
    record_result(user_tally)
    display_result(user_tally)

# Records the result of the user_exam
def record_result(user_tally):
    user_id = user_details.get("user_id")
    user_email = user_details.get("email")
    user_first_name = user_details.get("first_name")
    user_last_name = user_details.get("last_name")
    result_datetime = datetime.now().strftime('%y-%m-%d %H:%M:%S')
    
 #Adds the score for the exam into the results file
    if user_tally >= 0:
        with open(file_results, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([user_id,user_first_name,user_last_name,user_email,result_datetime,user_tally])

#Updates the users file to accredited (80% pass mark)    
    if user_tally >= 8:
        with open(file_users, 'r') as f:
            reader = csv.reader(f)
            rows = list(reader)

            found_user = False
            for i, row in enumerate(rows):
                if row[0] == user_id:
                    rows[i][5] = "True"
                    found_user = True
                    break
    
            if found_user:
                with open(file_users, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(rows)
            else:
                print("User not found")

def display_result(user_tally):
    first_name = user_details.get("first_name")
    score_percent = user_tally / 10 * 100
    if user_tally >= 8:
        print(f"{Back.green}{Fore.white}{Style.bold}Congratulations {first_name} - You passed with a score of {score_percent}%{Style.reset}")
        return_or_exit()
    elif user_tally <= 7:
        print(f"{Back.red}{Fore.white}{Style.bold}\nSorry {first_name} - You did not pass. You scored {score_percent}% with the pass mark being 80%.{Style.reset}\n\nDo you wish to try again?")
        while True:
            decision = input('\nEnter "Y" to retry, or "N" to return to main menu: ').lower()
            if decision =='y':
                user_exam()
                break
            elif decision =="n":
                menu_selection()
                break
            else:
                print("\nPlease enter a valid choice.")



########## EXITING THE APPLICATION ##########

# Back to Main Menu or Exit Application
def return_or_exit():
    print("\nDo you want to return to the main menu?")
    decision = input('Enter "Y" to return, or "exit" to leave the application: ').lower()
    if decision == 'y':
        menu_selection()
        return
    elif decision == "exit":
        user_exit()
        return
    else:
        print("Invalid entry, try again")
        return_or_exit()

# Exit Message
def user_exit():
    print("\nThank you for participating in the FIFA LOTG Application. Goodbye\n")