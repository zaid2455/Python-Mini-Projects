class Task:

    def __init__(self, name, duedate, description):
        self.name = name
        self.due = duedate
        self.desc = description
    
    def __str__(self):
        return f'{self.name} due {self.due}'
    

class Manager():

    def __init__(self):
        self.tasks = []
        self.completed = []

    def view_tasks(self):
        if self.tasks:                                          
            for num, task in enumerate(self.tasks, start=1):                                                                        
                print(f'{num}: {task}')                                                                     
            print('\n')                                                                     
        else:                                                                       
            print('No tasks available!\n')                                                                      

    def view_completed(self):                                                                       
        print('-------COMPLETED-------')                                                                        
        if self.completed:                                                                      
            for num, task in enumerate(self.completed, start=1):                                                                        
                print(f'{num}: {task}')                                                                     
            print('\n')                                                                     
        else:                                                                       
            print('No tasks completed!\n')                                                                      

    def add_task(self, name, duedate, description):
        created_task = Task(name, duedate, description)
        self.tasks.append(created_task)
        print(f'Task {name} succesfully added!\n')

    def remove_task(self, taskindex):
        removed = self.tasks.pop(taskindex-1)
        print(f'{removed} has been removed!\n')

    def view_task_desc(self, taskindex):
        task = self.tasks[taskindex-1]
        print(f'Description for {task.name}: {task.desc}\n')

    def complete(self, taskindex):
        completed = self.tasks.pop(taskindex - 1)
        self.completed.append(completed)
        print(f'Task {completed} marked as complete!')


manager = Manager()


def managerhandle(prompt, task_action):
        if manager.tasks:
            manager.view_tasks()

            while True:
                    try:
                        taskindex = input(f'{prompt}? ("e" to exit) ')
                        if taskindex == 'e':
                            print('EXITING...\n')
                            break
                        
                        elif int(taskindex) > 0:                                              
                           task_action(int(taskindex))
                           break
                        
                        else:
                            print('Must be on list!')

                    except:
                        print('Must be on list!')
        else:
            print('No Tasks Available!\n')


def main(): 
    print('1. Create a Task\n2. Remove a Task\n3. View Description\n4. View Tasks\n5. Mark as Complete\n6. View Completed Tasks')
    
    while True:

        option = input('Select an option (Enter "0" to view options): ')

        if option == '1':

            print('\n-----CREATE A TASK-----')
            name = input('Name of task: ')
            due = input(f'When is {name} due: ')
            desc = input(f'Description of {name}: ')
            manager.add_task(name, due, desc)

        elif option == '2':

            print('-----REMOVE TASK-----')
            managerhandle('Which task do you want to remove?', manager.remove_task)

        elif option == '3':

            print('\n------SELECT TASK FOR DESCRIPTION------')            
            managerhandle('Select task for description', manager.view_task_desc)

        elif option == '4':
            print('-------TASKS-------')
            manager.view_tasks()

        elif option == '5':
             managerhandle('Which task do you want to mark as complete', manager.complete)

        elif option == '6':
            manager.view_completed()

        elif option == '0':
            print('1. Create a Task\n2. Remove a Task\n3. View Description\n4. View Tasks\n5. Mark as Complete\n6. View Completed Tasks')

        elif option.upper() == 'CLEAR':
            print('\n' * 100)

        else:
            print('NOT AN OPTION\n')


if __name__ == '__main__':
    main()
