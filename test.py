import sqlite3
import pandas 
print('Imported SQLite!')


# Moving onto the actual shape/structure of the to do list

#  task_list will be a nested list that will contain lists in the format [task_no, rask_name, completed]
task_list=[['Task Number', 'Task Name','Status']]

#setting the default value as 5 for now. 
user_input=5

while user_input>=5:
    user_input=int(input(
        'Please choose an option: \n 1. Add a task you\'d like to accomplish today \n ' \
    '2. View the tasks in your list for today. \n ' \
    '3. Update the completion status of a task on the list. \n ' \
    '4. Delete/Remove any tasks in the list. \n'))

    if user_input<5: #Conditional that will break the while loop. If the user wants to move ahead, they have to choose a valid input.
        print(f'You have chosen option {user_input}')
        break 
    else:
        print("Invalid Option, Please retry.")

# NOTE FOR IMPROVEMENT- PLEASE IMPLEMENT OOPS.

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

    