print("Welcome to my To-Do List!")
import json
todo=[]
y=json.dumps(todo)
   
def todo_():
   
   while True:
      task=input("What would you like to do? 1. View tasks 2. Add a task 3. Remove a task 4. Exit")
      
      
      if task=="1":
         for index, value in enumerate(todo):
            print(f"{index+1}.{value}")
      
      if task=="2":
         new=input("Enter the new task:")
         todo.append(new)
         print("Task added!")
      
      if task=="3":
         index=int(input("Enter the number of the task to remove:"))
            todo.pop(index+1)
   
      if task=="4":
         print("Goodbye!")
         break

todo_()
      
   
         
        
         
         
         
      
      
         
      
         
      
   
   







