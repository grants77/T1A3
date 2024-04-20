# System Packages
import os.path

# External Packages
## Add Colored ##

# Imported Packages
## From functions.py ##

print("Welcome to the FIFA Laws of the Game Exam\n\nPlease enter your email address below")

users_file = "exam_users.csv"
results_file = "exam_results.csv"
exam_file = "exam_questions.csv"

# Check if there is a user file - create a new one if it doesn't exist
if (not os.path.isfile(users_file)):
    print("\nCreating a new username file\n") 
    # create a file and open in write 'w' mode
    users_file = open(users_file, "w")
    # enter the headings into the file
    users_file.write("userid,email,name,accredited\n")
    # close the file
    users_file.close()

# Check if there is a results file - create a new one if it doesn't exist
if (not os.path.isfile(results_file)):
    print("\nCreating a results file\n")
    # create a file and open in write 'w' mode
    results_file = open(results_file, "w")
    # enter the headings into the file
    results_file.write("userid,date,score,result\n")
    # close the file
    results_file.close()

# Check if there is a questions file - return an error if there isn't
if (not os.path.isfile(exam_file)):
    print("\nError - There are no exam questions.\nPlease contact your facilitator to rectify.\n")



# def user_validate():



def user_menu():
    print("Main Menu: \n 1. Take New Exam \n 2. View Previous Scores \n 3. View Leaderboard")
    
    user_choice = input("Select Menu Number: ")
    return user_choice

print(user_menu())

print("This is the end of the exam script")