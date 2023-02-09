from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 

class Employee:
    def __init__(self,root) : 
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee Management Systeem")


        #variables
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_id=StringVar()
        self.var_address=StringVar()
        self.var_salary=StringVar()
        self.var_phone=StringVar()

        lbl_title=Label(self.root,text="EMPLOYEE MANAGEMENT SYSTEEM",font=("tiles new roman",37,'bold'),fg='darkblue',bg='red')
        lbl_title.place(x=0,y=0,width=1400,height=50)

        #logo
        img_logo=Image.open('college_images/emplogo.png')
        img_logo=img_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_logo= ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=200,y=0,width=50,height=50)



        # image fram
        img_fram=Frame(self.root,bd=5,relief=RIDGE,bg='pink')
        img_fram.place(x=0,y=50,width=1350,height=160)

        # img1
        img1=Image.open('college_images/post-1.png')
        img1=img1.resize((400,140),Image.ANTIALIAS)
        self.photo_img1= ImageTk.PhotoImage(img1)

        self.img1=Label(img_fram,image=self.photo_img1)
        self.img1.place(x=10,y=10,width=400,heigh=140)

        # img2
        img2=Image.open('college_images/post-2.png')
        img2=img2.resize((400,140),Image.ANTIALIAS)
        self.photo_img2= ImageTk.PhotoImage(img2)

        self.img2=Label(img_fram,image=self.photo_img2)
        self.img2.place(x=460,y=10,width=400,heigh=140)

        # img3
        img3=Image.open('college_images/post-3.png')
        img3=img3.resize((400,140),Image.ANTIALIAS)
        self.photo_img3= ImageTk.PhotoImage(img3)

        self.img3=Label(img_fram,image=self.photo_img3)
        self.img3.place(x=910,y=10,width=400,heigh=140)

        #main fram
        main_fram=Frame(self.root,bd=5,relief=RIDGE,bg='green')
        main_fram.place(x=0,y=210,width=1350,height=483)

        #upper fram
        upper_fram=LabelFrame(main_fram,bd=0,relief=RIDGE,bg='black',text='Employee Informarion',fg='white')
        upper_fram.place(x=10,y=10,width=1320,height=240)

        #lables & entry 
        lbl_dep=Label(upper_fram,text='Department:',font=('arial',11,'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,padx=10,)

        combo_dep=ttk.Combobox(upper_fram,textvariable=self.var_dep,font=('arial',11,'bold'),width=20,state='readonly')
        combo_dep['value']=('select Department','HR','Manager','Engineer')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=10,pady=10,)

        #name 
        lbl_name=Label(upper_fram,text='Name:',font=('arial',11,'bold'),bg='white')
        lbl_name.grid(row=0,column=2,padx=10,pady=7,)

        combo_name=ttk.Entry(upper_fram,textvariable=self.var_name,font=('arial',11,'bold'),width=20)
        combo_name.grid(row=0,column=3,padx=10,pady=7,)

        #ID 
        lbl_ID=Label(upper_fram,text='ID:',font=('arial',11,'bold'),bg='white')
        lbl_ID.grid(row=1,column=0,padx=10,pady=2,)

        combo_ID=ttk.Entry(upper_fram,textvariable=self.var_id,font=('arial',11,'bold'),width=20)
        combo_ID.grid(row=1,column=1,padx=0,pady=10,)

         #Address
        lbl_Address=Label(upper_fram,text='Address:',font=('arial',11,'bold'),bg='white')
        lbl_Address.grid(row=1,column=2,padx=2,pady=2,)

        combo_Address=ttk.Entry(upper_fram,textvariable=self.var_address,font=('arial',11,'bold'),width=20)
        combo_Address.grid(row=1,column=3,padx=0,pady=10,)

         #Salary
        lbl_Salary=Label(upper_fram,text='Salary:',font=('arial',11,'bold'),bg='white')
        lbl_Salary.grid(row=2,column=0,padx=2,pady=2,)

        combo_Salary=ttk.Entry(upper_fram,textvariable=self.var_salary,font=('arial',11,'bold'),width=20)
        combo_Salary.grid(row=2,column=1,padx=0,pady=10,)


         #Phone no:
        lbl_Phone=Label(upper_fram,text='Phone no:',font=('arial',11,'bold'),bg='white')
        lbl_Phone.grid(row=2,column=2,padx=2,pady=2,)

        combo_Phone=ttk.Entry(upper_fram,textvariable=self.var_phone,font=('arial',11,'bold'),width=20)
        combo_Phone.grid(row=2,column=3,padx=0,pady=50,)

        #button fram
        button_fram=Frame(upper_fram,bd=0,relief=RIDGE,bg='black')
        button_fram.place(x=1000,y=10,width=170,height=190)

        btn_add=Button(button_fram,text='Save',command=self.add_data, font=('arial',10,'bold'),width=20,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=1,pady=5)

        btn_add=Button(button_fram,text='Update',command=self.update_data, font=('arial',10,'bold'),width=20,bg='blue',fg='white')
        btn_add.grid(row=1,column=0,padx=1,pady=10)

        btn_add=Button(button_fram,text='Delete',command=self.delete_data,font=('arial',10,'bold'),width=20,bg='blue',fg='white')
        btn_add.grid(row=2,column=0,padx=1,pady=10)

        btn_add=Button(button_fram,text='Reset',command=self.reset_data,font=('arial',10,'bold'),width=20,bg='blue',fg='white')
        btn_add.grid(row=3,column=0,padx=1,pady=10)

        #lower fram
        lower_fram=LabelFrame(main_fram,bd=0,relief=RIDGE,bg='blue',text='Employee Informarion Table',fg='white')
        lower_fram.place(x=10,y=260,width=1320,height=200)


         #search fram
        search_fram=LabelFrame(lower_fram,bd=0,relief=RIDGE,bg='brown',text='Search Employee information',fg='white')
        search_fram.place(x=10,y=10,width=1270,height=60)


         #search
        
        search=Label(search_fram,text='Search',font=('arial',11,'bold'),bg='white',fg='black')
        search.grid(row=0,column=0,padx=2,pady=2,)

 
        self.var_com_search=StringVar()
        combo_search=ttk.Combobox(search_fram,textvariable=self.var_com_search ,font=('arial',11,'bold'),width=25,state='readonly')
        combo_search['value']=('select Option','phone','ID')
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=10,pady=10,)

        self.var_search=StringVar()
        text_search=ttk.Entry(search_fram,textvariable=self.var_search,font=('arial',11,'bold'),width=25)
        text_search.grid(row=0,column=2,padx=0,pady=5,)

        btn_search=Button(search_fram,text='Search',command=self.search_data,font=('arial',10,'bold'),width=20,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=5,pady=5)

        btn_showall=Button(search_fram,text='Show all',command=self.fetch_data,font=('arial',10,'bold'),width=20,bg='blue',fg='white')
        btn_showall.grid(row=0,column=4,padx=5,pady=5)


        #============Employee Table=============

         #table fram
        table_fram=LabelFrame(lower_fram,bd=0,relief=RIDGE,bg='white',text='Database information',fg='black')
        table_fram.place(x=10,y=75,width=1270,height=100)
        
        # scroll_x
        scroll_x=ttk.Scrollbar(table_fram,orient=HORIZONTAL)
        #scroll_y
        scroll_y=ttk.Scrollbar(table_fram,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_fram,columns=('dep','name','id','adress','salary','phone',),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('id',text='ID')
        self.employee_table.heading('adress',text='Adress')
        self.employee_table.heading('salary',text='Salary')
        self.employee_table.heading('phone',text='Phone')

        self.employee_table['show']='headings'
 
        self.employee_table.column('dep',width=20)
        self.employee_table.column('name',width=20)
        self.employee_table.column('id',width=20)
        self.employee_table.column('adress',width=20)
        self.employee_table.column('salary',width=20)
        self.employee_table.column('phone',width=20)

        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind('<ButtonRelease>',self.get_cursor)
        

        self.fetch_data()
    
    #=========fuction Declaration==============

        #variables
        '''self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_id=StringVar()
        self.var_address=StringVar()
        self.var_salary=StringVar()
        self.var_phone=StringVar()'''

    def add_data(self):
        if self.var_dep.get()==" ":
            messagebox.showerror('Error',"All filed are required")     
        else:
            try:

                conn=mysql.connector.connect(host='localhost',user='root',passwd='123456',database='mydata')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into employee1 values(%s,%s,%s,%s,%s,%s)',(
                                        self.var_dep.get(),
                                        self.var_name.get(),
                                        self.var_id.get(),
                                        self.var_address.get(),
                                        self.var_salary.get(),
                                        self.var_phone.get(),                            
                                          
                ))  
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success','employee has been added',parent=self.root)
            except Exception as es:
                messagebox.showerror('error',f'due to :{str(es)}',parent= self.root)
    

    # fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',user='root',passwd='123456',database='mydata')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from employee1')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
                conn.commit()
            conn.close()

    #get cursor
    def get_cursor(self,event=""):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values']
        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_id.set(data[2])
        self.var_address.set(data[3])
        self.var_salary.set(data[4])
        self.var_phone.set(data[5])

    #update data
    def update_data(self):
        if self.var_dep.get()==" ":
            messagebox.showerror('Error',"All filed are required")     
        else:
            try:
                update=messagebox.askyesno('update','Are you sure update')
                if update>0:
                    conn=mysql.connector.connect(host='localhost',user='root',passwd='123456',database='mydata')
                    my_cursor=conn.cursor()
                    my_cursor.execute("update employee1 set Department=%s,Name=%s,Adress=%s,Salary=%s,Phone=%s where ID=%s ",(
                                    self.var_dep.get(),
                                    self.var_name.get(),
                                    
                                    self.var_address.get(),
                                    self.var_salary.get(),
                                    self.var_phone.get(),
                                    self.var_id.get(),
                                    ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success','employee succefully updated',parent=self.root)
            except Exception as es:
                messagebox.showerror('error',f'due to :{str(es)}',parent= self.root)


    #Delete
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror('error','all field are required')
        else:
            try:
                Delete=messagebox.askyesno('Delete','are you sure',parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',user='root',passwd='123456',database='mydata')
                    my_cursor=conn.cursor()
                    sql='delete from employee1 where id=%s'
                    value=(self.var_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete','employee succefully delete',parent=self.root)
            except Exception as es:
                messagebox.showerror('error',f'due to :{str(es)}',parent= self.root)

    #reset
    def reset_data(self):
        self.var_dep.set("select Department")
        self.var_name.set("")
        self.var_id.set("")
        self.var_address.set("") 
        self.var_salary.set("")
        self.var_phone.set("")

    #search data
    def search_data(self):
        if self.var_com_search.get()=='' or self.var_search.get()=='':
            messagebox.showerror('error','please select option')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',passwd='123456',database='mydata')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from employee1 where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("",END,values=i)
                conn.commit()
                
                conn.close()
            except Exception as es:
                messagebox.showerror('error',f'due to :{str(es)}',parent= self.root)   

if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()