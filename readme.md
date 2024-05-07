# Grant South - Terminal Application

## Introduction 

Welcome to the FIFA Laws of the Game Exam Application. This application is designed to generate an exam for users, with randomly selected questions. The application is built with the Python programming language.

The Application will allow you to:

- **Login:** The user can login to the application and store their name, email address and accreditation status. 

- **View Previous Results:** Allows the user to see the results from all of their previous exams, including the time they undertook the exam and the result they recived.

- **View User Profile:** Allows the user to see their user profile including their personal details, Unique User ID which was randomly generated when registering for the first time, and their accreditation status, which becomes TRUE when passing an exam for the first time.

- **Logout:** Allows the user to easily logout of the application and quickly log back in with another user account.

## Links

- [Github Repository (Public)](https://github.com/grants77/T1A3)

- [Trello KanBan (Public)](https://trello.com/b/UhQ6BV0P/t1a3-fifa-lotg-exam)

- [FIFA Laws of the Game (2023-24)](https://www.theifab.com/laws-of-the-game-documents/?language=all&year=2023%2F24)

## User Instructions

This application was designed and tested using Windows Subsystem for Linux (WSL). It is recommended that the application be run on a standalone termianl and not within VSCode or similar.

**1. Open a terminal**
**2. Close the GitHub Repository via SSH:**
> git@github.com:grants77/T1A3.git

**OR via HTTPS:**

> https://github.com/grants77/T1A3.git

**3. Navigate into the directory of the Cloned Repository:**

> cd T1A3

**4. Add execute permissions to the run.sh script:**

> chmod +x run.sh

**5. Run the run.sh script to begin the application:**

> ./run.sh

## Requirements

Below are the dependencies and system/hardware requirements for the use of this application.

### Dependencies

The following Python libraries are used in this application. You are not required to install them yourself as they will do so when you run the scripts from the above user instructions.

- **colored:** A simple library for the colouring and formatting in the terminal application.

- **maskpass:** A library which in this instance is used to mask the password of the user when they are either logging into the application or creating an account.

- **random:** This is used for two purposes in the application - For the generation of a random UserID when the user registers for the first time, and to randomly sort the examination questions to present to the user.

- **datetime:** This is used to record the date and time of the user at the time they completed their examination. It is retained and displayed when viewing the users previous results.

### System/Hardware

This application is not resource intensive and will run with minimal hardware specs. There are some software requirements as per below.

- Python3
- Bash
- Git

## Features

The following features are displayed within the application for the user to navigate to and interact with:

- **Login:** The user is able to login to the application with a username and password which is stored in a **exam_users.csv** file. This allows the user to have a personalised experience when they are in the application and allow for potentially sensitive information to be stored and not displayed by the application to other users.

- **Registration:** The application checks the users email address in the **exam_users.csv** file and if the user is not registered it prompts for their personal details and stores them in the file, allowing that user to login with those details if they return to the system.

- **Examination:** The user is able to select the 'Take New Exam' option from the provided menu. This takes the user to the examination screen which will prompt the user to answer 'TRUE' or 'FALSE' to ten randomly selected questions from the **exam_questions.csv** file. The user can gracefully exit from the exam by entering 'EXIT'. For testing/marking purposes, if the question ends with an 'F' it is false, otherwise it is true.

- **Previous Results:** The application allows the user to view all of their previous exam attempts by accessing the **exam_results.csv** file and only returning the results for the user that is logged into the application. The results on this file are recorded at the end of the exam whether the user passes or fails.

- **Personal Profile:** The user can select the personal profile option from the menu which will present a screen with the information they provided on registration. This screen will also display if the user is accredited by displaying 'TRUE'. This accreditation is updated by the application if the user achieves a score of 80% or more in an exam. The information on this screen is derived from the **exam_users.csv** file.

- **Logout:** This allows the user to log out of the application without terminating the script, so they can log into another account.

## Code Styling Guide / Styling Conventions (R5)



## Implementaton Plan (R7)

## Help Documentation (R8)
