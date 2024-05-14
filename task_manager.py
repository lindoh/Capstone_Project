#=========================== Importing Libraries ==============================
# Regex split module
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


def print_task(assigned_user, title, description, start_date, \
                           due_date, task_complete):
    '''
    Display information in a clear and easy to read manner
    '''
     # Print the results
    print('Task:\t\t\t ' + title + '\n'+ 'Assigned to:\t\t ' + assigned_user+\
          '\n'+ 'Date assigned:\t\t ' + start_date + '\n' + 'Due date:\t\t '+\
          due_date + '\n' + 'Task complete:\t\t ' + task_complete + '\n' +\
          'Task description:\t ' + description + '\n')


def process_task_file(menu_option):
    '''
    This function reads a file, split and strip into seperate information
    And print the resulting information based on the menu option chosen
    '''
    # Read a line from the file
    with open('tasks.txt', 'r') as file:
        for line in file:
            # Convert the string line into a list for ease of manipulation
            task = line.split(',')

            # Assigned each text to the correct component
            assigned_user = task[0].strip()
            title = task[1].strip()
            description = task[2].strip()
            start_date = task[3].strip()
            due_date = task[4].strip()
            task_complete = task[5].strip()

            # Print all tasks if menu option is 'va' else print the tasks for 
            # logged in user
            if (menu_option == 'va' or 
               (menu_option == 'vm' and assigned_user == logged_in_user)):
                print_task(assigned_user, title, description, start_date, \
                           due_date, task_complete)
                
# =============================================================================
# ============================= Main Program ==================================
    
# ============================= Login Section =================================

# Flag to be used for accessing the menu after logging in successfuly
valid =  False
# To hold the username of the logged in user
logged_in_user = ''

# Initially assume the user credentials are invalid 
while valid == False:
    # Ask the user for username
    username = input("Please enter username: ")
    # Ask the user for password
    password = input("Please enter password: ")

    # If Login credentials are valid, display appropriate message and 
    # set valid to True
    if validate_logins(username, password) == True:
        print("Login Successful!!\n")
        logged_in_user = username
        valid = True

# ========================== Main Program Section =============================

# Menu options for all users
menu_items = '''Select one of the following options:
                    r - register a user
                    a - add task
                    va - view all tasks
                    vm - view my tasks
                    e - exit
                    : '''

# Menu options only for admin users
extra_menu_items = '''Select one of the following options:
                    r - register a user
                    a - add task
                    va - view all tasks
                    vm - view my tasks
                    d - display statistics
                    e - exit
                    : '''

# If Login is successful, display the menu
while valid:
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.
    if (logged_in_user == 'admin'):
        menu = input(extra_menu_items).lower()
    else:
        menu = input(menu_items).lower()

    # Register User
    if menu == 'r':

        # Check if the user is an admin
        if (logged_in_user == 'admin'):
            
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

        else:
            print("Only admin can register other users!!\n")

    # Add Task
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

    # View All Tasks
    elif menu == 'va':
        # Process the task file and print the task details
        process_task_file(menu)
       
    # View My Tasks
    elif menu == 'vm':
        # Process the task file and print the task details for the
        # logged in user
        process_task_file(menu)

    # Display Statistics
    elif menu == 'd' and logged_in_user == 'admin':
        # tasks counter
        task_counter = 0
        # users counter
        user_counter = 0

        # Read a line from the tasks.txt file and count number of lines
        with open('tasks.txt', 'r') as file:
            for line in file:
                task_counter += 1 

        # Read a line from the user.txt file and count number of lines
        with open('user.txt', 'r') as file:
            for line in file:
                user_counter += 1 

        # Display the results
        print("\nCurrent Statistics: ")
        print(f"The number of Tasks is {task_counter}")
        print(f"The number of Users is {user_counter}\n")

    # Exit
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    # Provide appropriate error message if an invalid selection is made
    else:
        print("You have entered an invalid input. Please try again")