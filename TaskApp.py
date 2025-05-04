# alpha male coding sesh

import datetime
import json

#initializes some variables for the program to run
close_prog = False
taskID = 1
utime = ""
status = ""

#prepares a unique "task" to write to the json file for first time loads
#this helps with users understanding the stored task format, and does initial setup to make writing future tasks easier
first_writer = [0, "task", "desc", "status", "time of creation", "time of update"]

#including taskID (maybe remove later if it cucks the function to list and locate tasks)
task_items = len(first_writer)

with open("taskapp_storage.json",) as startcheck:
    startcheck = startcheck.read()

#this checks if its a first time loading, or if its a user returning, or if potentially the initialized data is tampered by a user in some way.
try:
    startcheck = list(json.loads(startcheck))
except:
    try:
        if startcheck[0] == 0:
            print("Welcome back!")
        else:
            with open("taskapp_storage.json", "w") as firstwrite:
                first_writer = json.dumps(first_writer)
                firstwrite.write(first_writer)
                print("Data was potentially corrupted! Storage reset...")
    except:
        with open("taskapp_storage.json", "w") as firstwrite:
                first_writer = json.dumps(first_writer)
                firstwrite.write(first_writer)
                print("First time data write finished successfully!")
else:
    print("Welcome Back!")


#this function adds tasks
def add_task():
    global task, desc, ctime
    task = str(input("Input task: "))
    desc = str(input("Description: "))
    usr_status = int(input("(1) for To do, (2) for In Progress, (3) for Done: "))
    match usr_status:
        case 1:
            status = "To Do"
        case 2:
            status = "In Progress"
        case 3:
            status = "Done"
        case _:
            print("Pick from the options given.")
    ctime = str(datetime.datetime.now())
    with open("taskapp_storage.json") as tidcheck:
        temp_tid = list(json.loads(tidcheck.read()))
    tempid = 1
    for x in range(len(temp_tid)):
        try:
            if int(temp_tid[x]):
                tempid = temp_tid[x]
                tempid += 1
        except:
            pass
    taskID = tempid
    writer = [taskID, task, desc, status, ctime, utime]
    with open("taskapp_storage.json") as file_dcheck:
        global fdc
        fdc = file_dcheck.read()
        try:
            with open("taskapp_storage.json", "w") as file_w:
                fdc = list(json.loads(fdc))
                file_w.write(json.dumps(fdc + writer))
                print("Saved new task successfully!")
        except:
            print("Couldn't write task to file.")

#this function lists all tasks or all status per status: To Do, In Progress, Done
def list_tasks():
    usr_list_choice = int(input("(1) for list all tasks, (2) for listing all Done tasks, (3) for listing all In Progress tasks, (4) for listing all To Do tasks: "))
    with open("taskapp_storage.json") as ltasks:
                tasks = list(json.loads(ltasks.read()))
    option2 = "Done"
    option3 = "In Progress"
    option4 = "To Do"
    match usr_list_choice:
        case 1:
            i = len(tasks)
            trange = range(1, i, task_items)
            taskid = 0
            for x in trange:
                if x == 1:
                    continue
                taskid += 1
                print("taskID:", taskid, "|", "Task:", tasks[x])
        case 2:
            with open("taskapp_storage.json") as ltasks:
                tasks = list(json.loads(ltasks.read()))
            tasks_l = len(tasks)                
            for x in range(9, tasks_l, 6):
                x_chk = tasks[x]
                if x_chk == option2:
                    x -= 2
                    print(tasks[x], " | ", "Status: Done")
                else:
                    continue
            pass
        case 3:
            with open("taskapp_storage.json") as ltasks:
                tasks = list(json.loads(ltasks.read()))
            tasks_l = len(tasks)                
            for x in range(9, tasks_l, 6):
                x_chk = tasks[x]
                if x_chk == option3:
                    x -= 2
                    print(tasks[x], " | ", "Status: In Progress")
        case 4:
            with open("taskapp_storage.json") as ltasks:
                tasks = list(json.loads(ltasks.read()))
            tasks_l = len(tasks)                
            for x in range(9, tasks_l, 6):
                x_chk = tasks[x]
                if x_chk == option4:
                    x -= 2
                    print(tasks[x], " | ", "Status: To Do")
        case _:
            print("Pick an option listed.")
            

def update_task():
    task_updt_time = str(datetime.datetime.now())
    try:
        usr_task_updt = int(input("Which task to update? (Please use taskID only): "))
    except ValueError:
        print("use a TaskID only.")
    if usr_task_updt == 0:
        print("You can't update task 0")
        quit()
    with open("taskapp_storage.json") as updt:
        task_updt = list(json.loads(updt.read()))
        for x in task_updt:
            if x is usr_task_updt:
                z = task_updt.index(x)
                z += 5
                task_updt[z] = task_updt_time
                z -= 2
                usr_status_updt = int(input("Update task status | (1) for To do, (2) for In Progress, (3) for Done: "))
                match usr_status_updt:
                    case 1:
                        task_updt[z] = "To Do"
                    case 2:
                        task_updt[z] = "In Progress"
                    case 3:
                        task_updt[z] = "Done"
                    case _:
                        print("Pick an option listed.")
                z -= 1
                usr_taskd_updt = input("Update task description: ")
                task_updt[z] = usr_taskd_updt
                z -= 1
                usr_taskt_updt = input("Update task title: ")
                task_updt[z] = usr_taskt_updt
                print("Updating task: ", task_updt[z])
    with open("taskapp_storage.json", "w") as updtwrite:
        updtwrite.write(json.dumps(task_updt))


def del_task():
    try:
        usr_task_del = int(input("Which task to delete? (Please use TaskID only): "))
    except ValueError:
        print("Use a TaskID only.")
    if usr_task_del == 0:
        print("You can't delete task 0")
        quit()
    with open("taskapp_storage.json") as find:
        taskr = list(json.loads(find.read()))
        taskrl = len(taskr)    
        for x in taskr:
            if x is usr_task_del:
                z = taskr.index(x)
                z += 5
                del taskr[z]
                z -= 1
                del taskr[z]
                z -= 1
                del taskr[z]
                z -= 1
                del taskr[z]
                z -= 1
                print("Deleting task: ", taskr[z])
                del taskr[z]
                z -= 1
                del taskr[z]
        for x in range(taskrl):
            try:
                if int(taskr[x]):
                    if taskr[x] > usr_task_del:
                        temp_taskr = taskr[x]
                        temp_calc_taskr = taskr[x]
                        temp_taskr = taskr.index(temp_taskr)
                        temp_calc_taskr -= 1
                        taskr[temp_taskr] = temp_calc_taskr

            except:
                pass
    with open("taskapp_storage.json", "w") as delwrite:
        delwrite.write(json.dumps(taskr))
        print("Successfully deleted task.")
                


#this gives the user options they can call and a way to exit the program safely from the CLI
while close_prog == False:
    print("(1) for add a task (2) listing all tasks (3) for updating a task (4) for deleting a task (5) to exit")
    usr_input = input("What would you like to do?: ")
    match usr_input:
        case "1":
            add_task()
        case "2":
            list_tasks()
        case "3":
            update_task()
        case "4":
            del_task()
        case "5":
            close_prog = True
        case _:
            print("Please pick an option listed.")

#program closer
if close_prog == True:
    print("Closing...")
    exit()