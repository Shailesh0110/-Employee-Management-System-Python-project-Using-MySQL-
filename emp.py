from tkinter import *


class Employee:
    def __init__(self,root) : 
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee Management Systeem")


root=Tk()
obj=Employee(root)
root.mainloop()
  
   
   
   
