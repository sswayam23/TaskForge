import sqlite3
import pandas

def  get_user_choice():
    user_input=5
    while user_input>=5:
        user_input=int(input(
            'Please choose an option: \n 1. Add a task you\'d like to accomplish today \n ' \
        '2. View the tasks in your list for today. \n ' \
        '3. Update the completion status of a task on the list. \n ' \
        '4. Delete/Remove any tasks in the list. \n'))

        if user_input<5: #Conditional that will break the while loop. If the user wants to move ahead, they have to choose a valid input.
            print(f'You have chosen option {user_input}')
            return user_input
            # Value being returned here, if the option chosen is wrong/invalid the loop will continue executing until a valid input is received.
            print("Invalid Option, Please retry.")

def user_choice_action(user_input):
    if user_input==1:
        task_number= len(task_list) #No need to add any numbers to this because of Python indexing....
        task_name= input(' Enter a short description of the task you\'d like to accomplish \n')
        status=0 #More on this later.

        task_list.append([task_number, task_name, status])

        print(' After addition of task, the list looks like this ')
    
    for i in task_list:
        print(f'  {i[0]:<12}  |  {i[1]:^20}  | {i[2]:<10}  ')

    if user_input==2:
        for i in task_list:
            print(f'  {i[0]:<12}  |  {i[1]:^20}  | {i[2]:<10}  ')

    if user_input==3:
        print("The table currently looks like this")
        for i in task_list:
            print(f'  {i[0]:<12}  |  {i[1]:^20}  | {i[2]:<10}  ')
        
        updation=int(input("Which entry would you like to update?"))
        status_update=input("How would you like to update the status? [Completed/In Progess/Unfinished]")
        task_list[updation][2]= status_update

        print("Value Updated, the table now looks like")
        for i in task_list:
            print(f'  {i[0]:<12}  |  {i[1]:^20}  | {i[2]:<10}  ')

    if user_input==4:
        print("The table currently looks like this.")
        for i in task_list:
            print(f'  {i[0]:<12}  |  {i[1]:^20}  | {i[2]:<10}  ')
        deletion=int(input("Which entry would you like to delete?"))
        task_list.pop(deletion)


    # Room for improvement- Update the serial number after deletion. 

        print("Updated table looks like this: ")
        for i in task_list:
            print(f'  {i[0]:<12}  |  {i[1]:^20}  | {i[2]:<10}  ')

# This is a temporary line, we will fix this. I think this is not deserving of a line in the main window.
task_list=[['Task Number', 'Task Name','Status']]

task_list_touched=0

if task_list_touched==0:
    print("Let us add some tasks to track for today!")
    user_choice_action(1)
    task_list_touched=1

# Now that we have the first task added, let us display it and not just close the application. 
# This will help in at least maintaining the temporary memory. 

#Again, only using this to maintain memory and keep the app open, once we implement the database procedure, we do not need the user to
#keep the app open to retain memory.

#Another thing I'd like to change is that I feel like there's excessive text. Too much spoonfeeding going on, will fix it after POC is 
#deemed to be enough.
exit_app=1

while exit_app:
    # Did not use the function because I did not want the text to show up.
    for i in task_list:
            print(f'  {i[0]:<12}  |  {i[1]:^20}  | {i[2]:<10}  ')
    user_input=input("To see the menu or to make the changes please press Enter. \n" \
                 "To quit the app please enter q.")

    if user_input=="":
        user_choice=get_user_choice()
        user_choice_action(user_choice)
    
    if user_input=='q':
        exit_app=0

print(" Thank you for using the app.")

