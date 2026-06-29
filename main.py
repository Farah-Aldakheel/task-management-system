tasks = []

while True:
    print ("\n==== tasks management system ====")
    print ("1. Add task")
    print ("2. View tasks")
    print ("3. exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("enter your task: ")
        tasks.append(task)

    elif choice == "2":
        if len(tasks) == 0:
            print("no tasks available ")
        else:
            print ("your tasks are: ")
            for i, task in enumerate(tasks,start=0):
                print (f"{i+1}. {task}")

    elif choice == "3":
        print ("exiting the program")
        break

    else:
        print("invalid choice,please try againg")
1