print("""Here is console Based Task List where you can view add delete the tasks
1) View All Tasks
2) Add New Task
3) Delete the Task
""")
taskList = ["Fix the Vercel Issues"]

def task_operations(select_operation):
    if select_operation == 1:
        for idx,showList in enumerate(taskList,start=1):
            print("\n",idx,")",showList)
    if select_operation == 2:
        task_addition = input("\n Enter the task Item ")
        taskList.append(task_addition)
        print("Task Added In TaskList")
    if select_operation == 3:
        if not taskList:
            print("TaskList Empty could not delete the tasks")
        for idx, showList in enumerate(taskList, start=1):
            print(f"{idx}) {showList}")
        try:
            select_task_item = int(input("\nSelect the item number you want to delete: "))
            if 1 <= select_task_item <= len(taskList):
                deleted_task = taskList.pop(select_task_item - 1)
                print(f" Task '{deleted_task}' deleted successfully!")
            else:
                print("Please select a valid task number.")
        except ValueError:
            print("Invalid input! Please enter a number.")

while True:
    try:
        select_operation = int(input("\n Please Select Operation Number "))
        task_operations(select_operation)
        choice = input("\nDo you want to exit? (Y/N): ").strip().lower()
        if choice == "y":
            print("\nExiting Task Manager. Goodbye!")
            break
    except ValueError:
        print("Invalid input! Please enter string with y or n operations values only.")


