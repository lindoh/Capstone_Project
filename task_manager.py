#=========================== Importing Libraries ==============================
import re

#=========================== Function Definitions =============================

def process_user_file():
    '''
    This function opens the user.txt file and seperate the username and password.
    Returns a dictionary with a key:value pair as username:password pair
    '''
     # Open a file for reading usernames and passwords
    with open('user.txt', 'r') as file:
        user_file = file.read()

    # Split the user_file information into seperate username and password
    user_file = re.split(',|\n', user_file)

    # Declare a dictionary to hold the username, password combination from
    # the user_file file
    login_details = {}

    # Iterate through user_file and to save the username and password
    for i in range(len(user_file)):
        if (i % 2 == 0):
            login_details[user_file[i]] = user_file[i + 1].strip()

    # Return the Username:Password pairs
    return login_details


def validate_logins(username, password):
    '''
    validate_logins takes username and password and checks if they are valid.
    The function returns a true for valid and false for invalid logins
    '''
    # Dictionary holds username, password combination from the user.txt file
    #login_details = {}
    login_details = process_user_file()

    # Iterate through login_details to find a match for username and password 
    username_found = False
    password_valid = False

    for user_name in login_details:
        # Check if given username is found in our database
        if (username == user_name):
            # If found, check if corresponding password is correct and update flag
            username_found = True

            # If Password match is found return true
            if login_details[user_name] == password:
                password_valid = True
                break    
            else:
                print("ERROR!! The supplied password is Invalid, please try again.\n")

    # If all usernames have been check and no match is found, alert the user
    if username_found == False:
        print("ERROR!! The username does not exist")

    # Return the result
    return password_valid

# =============================================================================
# ============================= Main Program ==================================
    
#====Login Section====

valid =  False

while valid == False:
    # Ask the user for username
    username = input("Please enter username: ")
    # Ask the user for password
    password = input("Please enter password: ")

    # If Login credentials are valid, display appropriate message and 
    # set valid to True
    if validate_logins(username, password) == True:
        print("Login Successful!!\n")
        valid = True

# If Login is successful, display the menu
while valid:
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.
    menu = input('''Select one of the following options:
                    r - register a user
                    a - add task
                    va - view all tasks
                    vm - view my tasks
                    e - exit
                    : ''').lower()

    if menu == 'r':
        # Request input of a new username
        username = input("Please enter username: ")
        # Request input of a new password
        password = input("Please enter password: ")
        # Request input of password confirmation.
        confirm_password = input("Please confirm password: ")

        # Check if the new password and confirmed password are the same
        if (password != confirm_password):
           print("ERROR!! Passwords do not match.. ") 
        # Else if they are the same, add them to the user.txt file,
        else:
            with open('user.txt', 'a') as file:
                file.write('\n' + username + ', ' + password)

    elif menu == 'a':
        # Ask the username of the person whom the task is assigned to,
        assigned_user = input("Enter username for the user assigned to task: ")
        # the title of the task,
        title = input("Enter task title: ")
        # the description of the task, and 
        description = input("Enter task description: ")
        # Then, get the current date.
        start_date = input("Enter current date: ")
        # the due date of the task.
        due_date = input("Enter task due date: ")
        
        # Add the data to the file task.txt
        with open('tasks.txt', 'a') as file:
            file.write('\n'+ assigned_user + ', ' + title + ', ' + description\
                       + ', ' + start_date + ', ' + due_date + ', ' + 'No')

    elif menu == 'va':
        pass
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in the PDF
            - It is much easier to read a file using a for loop.'''

    elif menu == 'vm':
        pass
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the 
              username you have read from the file.
            - If they are the same you print the task in the format of Output 2
              shown in the PDF '''

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")