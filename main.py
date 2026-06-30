tasks = []

def add_task():
    task = input("enter your task: ")
    tasks.append(task)

def view_task():
    if len(tasks) == 0:
        print("no tasks available ")
    else:
        print ("your tasks are: ")
        for i, task in enumerate(tasks,start=0):
            print (f"{i+1}. {task}")

def delete_task():
    if len(tasks) == 0:
            print ("the task list is empty there is no thunfg to delete")
    else:
            print ("your tasks are:")
            for i,task in enumerate(tasks,start=0):
                print (f"{i+1}. {task}")
                task_num = int(input("enter the task number you want to delete :"))
                if 1 <= task_num <= len(tasks):
                    deleted_task = tasks.pop(task_num - 1)
                    print (f"task '{deleted_task}' has been deleted")
                else:
                    print ("invalid task number, please try again")

def exit_program():
    print ("exiting the program")

    
while True:
    print ("\n==== tasks management system ====")
    print ("1. Add task")
    print ("2. View tasks")
    print ("3. delete task")
    print ("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_task()

    elif choice == "3":
      delete_task()

    elif choice == "4":
        exit_program()
        break

    else:
        print("invalid choice,please try againg")
