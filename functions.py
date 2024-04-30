# System Packages
import os.path
import csv
import random
from datetime import datetime

# External Packages
## Add Colored ##
## Add password masking ##

# Imported Packages

file_questions = "exam_questions.csv"
file_results = "exam_results.csv"
file_users = "exam_users.csv"
referee_email = None
user_details = {}

########## LOGIN AND USER MENU ##########

# Login Function
def user_check():
    global referee_email, user_details
    try:
        user_file = open (file_users, "r")
        print("\nWelcome to the FIFA Laws of the Game Exam\n") 
        referee_email = input("Enter Email: ")
        
        user_found = False
        for line in user_file:
            item = line.strip().split(",")
            if referee_email == item[1]:
                user_found = True
                user_details = user_finder(referee_email)
                print("\nWelcome Back!")
                break
        
        if user_found:
            current_attempts = 0
            expire_attempts = 3
            while current_attempts < expire_attempts:
                password_entered = input("\nEnter Password: ")
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
            create_new_user(referee_email)
            menu_selection()

    except FileNotFoundError:
        print("File Not Found, Creating New File")
        create_users_file()
        user_check()


    
# Determines next step when menu item selected
def menu_selection():
    print("DEBUGGING - MENU_SELECTION")
    user_selection = ""
    user_menu()
    user_selection = input("Select Menu Number: ")
    print(f"You've chosen menu item {user_selection}")
    if user_selection == "1": # Take Exam
        print("You chose 1")
        user_exam()

    elif user_selection == "2":
        print("You chose 2") # Previous Results
        user_results()

    elif user_selection == "3":
        print("You chose 3") # Personal Profile
        user_profile(referee_email)

    elif user_selection == "4":
        print("You chose 4") #Logout
        print("You have been logged out of the FIFA LOTG Application")
        user_check()
    
    elif user_selection == "5":
        print("You chose 5") #Exit
        print("DEBUGGING - IN SELECTION 5")
        user_exit()

    else:
        print("You have not made a valid selection")


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
            print("\n             Previous Results \n--------------------------------------------\n|        Date       |     Name    | Score |")
            for row in reader:
                if row[0] == user_id:
                    print(f"| {row[4]} | {row[1]} {row[2]} |   {row[5]}   |")
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
            print(question)
            user_answer = input("Enter 'True' or 'False': ").strip().lower()
            if user_answer == correct_answer.lower():
                user_tally += 1
    record_result(user_tally)

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


########## EXITING THE APPLICATION ##########

# Back to Main Menu or Exit Application
def return_or_exit():
    print("DEBUGGING - RETURN_OR_EXIT")
    print("\nDo you want to return to the main menu?")
    decision = input('Enter "Y" to return, or "exit" to leave the application: ').lower()
    if decision == 'y':
        menu_selection()
    elif decision == "exit":
        user_exit()
    else:
        print("Invalid entry, try again")

# Exit Message
def user_exit():
    print("\nThank you for participating in the FIFA LOTG Application. Goodbye\n")
    return