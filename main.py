import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

win=tk.Tk()
win.geometry("1250x600+0+0")
win.title("Student Managment System")
title_label=tk.Label(win,text="Student Management System",font=("Arial",30,"bold"),border=12,relief=tk.GROOVE,bg="orange",foreground="black")
title_label.pack(side=tk.TOP,fill=tk.X)

detail_frame=tk.LabelFrame(win,text="Enter Details",font=("Arial",20),bd=12,relief=tk.GROOVE,bg="lightgrey")
detail_frame.place(x=30,y=90,width=420,height=500)

data_frame=tk.Frame(win,bd=12,bg="lightgrey",relief=tk.GROOVE)
data_frame.place(x=475,y=90,width=770,height=500)

rollno=tk.StringVar()
name_var=tk.StringVar()
dept_var=tk.StringVar()
email_var=tk.StringVar()
contact_var=tk.StringVar()
gender=tk.StringVar()
dob=tk.StringVar()
father_name=tk.StringVar()
add_var=tk.StringVar()

search_by=tk.StringVar()
search_entry=tk.StringVar()


rollno_lbl=tk.Label(detail_frame,text="Rollno:",font=('Arial',14),bg="yellow")
rollno_lbl.grid(row=0,column=0,padx=2,pady=2)

rollno_ent=tk.Entry(detail_frame,bd=7,font=("Arial",14),bg="white",textvariable=rollno)
rollno_ent.grid(row=0,column=1,padx=2,pady=2)

name_lbl=tk.Label(detail_frame,text="Name:",font=('Arial',14),bg="yellow")
name_lbl.grid(row=1,column=0,padx=2,pady=2)

name_ent=tk.Entry(detail_frame,bd=7,font=("Arial",14),bg="white",textvariable=name_var)
name_ent.grid(row=1,column=1,padx=2,pady=2)

dept_lbl=tk.Label(detail_frame,text="Dept:",font=('Arial',14),bg="yellow")
dept_lbl.grid(row=2,column=0,padx=2,pady=2)

dept_ent=tk.Entry(detail_frame,bd=7,font=("Arial",14),bg="white",textvariable=dept_var)
dept_ent.grid(row=2,column=1,padx=2,pady=2)

email_lbl=tk.Label(detail_frame,text="Email:",font=('Arial',14),bg="yellow")
email_lbl.grid(row=3,column=0,padx=2,pady=2)

email_ent=tk.Entry(detail_frame,bd=7,font=("Arial",14),bg="white",textvariable=email_var)
email_ent.grid(row=3,column=1,padx=2,pady=2)

contact_lbl=tk.Label(detail_frame,text="Contact:",font=('Arial',14),bg="yellow")
contact_lbl.grid(row=4,column=0,padx=2,pady=2)

contact_ent=tk.Entry(detail_frame,bd=7,font=("Arial",14),bg="white",textvariable=contact_var)
contact_ent.grid(row=4,column=1,padx=2,pady=2)

gender_lbl=tk.Label(detail_frame,text="Gender:",font=('Arial',14),bg="yellow")
gender_lbl.grid(row=5,column=0,padx=2,pady=2)

gender_ent=ttk.Combobox(detail_frame,font=("Arial",14),textvariable=gender)
gender_ent['values']=("Male","Female","Others")
gender_ent.grid(row=5,column=1,padx=2,pady=2)

dob_lbl=tk.Label(detail_frame,text="DOB:",font=('Arial',14),bg="yellow")
dob_lbl.grid(row=6,column=0,padx=2,pady=2)

dob_ent=tk.Entry(detail_frame,bd=7,font=("Arial",14),bg="white",textvariable=dob)
dob_ent.grid(row=6,column=1,padx=2,pady=2)



fathername_lbl=tk.Label(detail_frame,text="Father'sname:",font=('Arial',14),bg="yellow")
fathername_lbl.grid(row=7,column=0,padx=2,pady=2)

fathername_ent=tk.Entry(detail_frame,bd=7,font=("Arial",14),bg="white",textvariable=father_name)
fathername_ent.grid(row=7,column=1,padx=2,pady=2)

address_lbl=tk.Label(detail_frame,text="Address:",font=('Arial',14),bg="yellow")
address_lbl.grid(row=8,column=0,padx=2,pady=2)

address_ent=tk.Entry(detail_frame,bd=7,font=("Arial",14),bg="white",textvariable=add_var)
address_ent.grid(row=8,column=1,padx=2,pady=2)

def fetch_data():
       conn=pymysql.connect(host="localhost",user="root",password="",database="sms1")
       curr=conn.cursor()
       curr.execute("Select*from student")
       rows=curr.fetchall()
       if len(rows)!=0:
              student_table.delete(*student_table.get_children())
              for row in rows:
                     student_table.insert('',tk.END,values=row)
              conn.commit()
       conn.close()


def add_func():
       if rollno.get()=="" or name_var.get()=="" or dept_var.get()=="" or email_var.get()=="" or contact_var.get()=="" or gender.get()=="" or dob.get()=="" or father_name.get()=="" or add_var=="":
              messagebox.showerror("Oops!!,you did not fill the fields please fill it. ")
       else:
              conn=pymysql.connect(host="localhost",user="root",password="",database="sms1")
              curr=conn.cursor()
              curr.execute("INSERT INTO student VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(rollno.get(),name_var.get(),dept_var.get(),email_var.get(),contact_var.get(),gender.get(),dob.get(),father_name.get(),add_var.get()))
              conn.commit()
              conn.close()

              fetch_data()
def get_cursor(event):
       cursor_row=student_table.focus()
       content=student_table.item(cursor_row)
       row=content['values']
       rollno.set(row[0])
       name_var.set(row[1])
       dept_var.set(row[2])
       email_var.set(row[3])
       contact_var.set(row[4])
       gender.set(row[5])
       dob.set(row[6])
       father_name.set(row[7])
       add_var.set(row[8])
def clear_func():
       rollno.set("")
       name_var.set("")
       dept_var.set("")
       email_var.set("")
       contact_var.set("")
       gender.set("")
       dob.set("")
       father_name.set("")
       add_var.set("")
def update_func():

        conn=pymysql.connect(host="localhost",user="root",password="",database="sms1")
        curr=conn.cursor()
        curr.execute("update student  set Name=%s, Dept=%s, Email=%s, Contact=%s, Gender=%s, DOB=%s, Fathername=%s, Address=%s where Rollno=%s" ,(name_var.get(),dept_var.get(),email_var.get(),contact_var.get(),gender.get(),dob.get(),father_name.get(),add_var.get(),rollno.get()))
        conn.commit()
        fetch_data()
        conn.close()
        clear_func() 
     
def delete_func():       
        conn=pymysql.connect(host='localhost',user="root",password="",database='sms1')
        cursor=conn.cursor()
        if rollno.get()=="" or name_var.get()=="" or dept_var.get()=="" or email_var.get()=="" or contact_var.get()=="" or gender.get()=="" or dob.get()=="" or father_name.get()=="" or add_var.get()=="":
              messagebox.showerror("Oops!!,you did not select the data from table . ")
        else:      
          cursor.execute("delete from student where Rollno=%s",(rollno.get(),))
          conn.commit()
          fetch_data()
          conn.close()
          messagebox.showinfo("Success","Data has been Deleted ")        

def search():
     search_criteria = search_by.get()
     search_value = search_entry.get()  # Assuming search_entry is defined somewhere
    
     if search_value == "":  # No search criteria selected
        messagebox.showerror("Error", "Please select a search value.")
        return
    
     try:
        conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
        curr = conn.cursor()

        # Constructing the SQL query based on selected criteria

        if search_criteria == "Name":
            query = "SELECT * FROM student WHERE Name =%s"
        elif search_criteria == "Rollno":
            query = "SELECT * FROM student WHERE Rollno =%s"
        elif search_criteria == "Contact":
            query = "SELECT * FROM student WHERE Contact =%s"
        elif search_criteria == "Email":
            query = "SELECT * FROM student WHERE Email = %s"
        elif search_criteria == "Dept":
            query = "SELECT * FROM student WHERE Dept =%s"
        elif search_criteria == "DOB":
            query = "SELECT * FROM student WHERE DOB =%s"
        else:
            messagebox.showerror("Error", "Invalid search criteria selected.")
            return

        # Executing the query
        curr.execute(query,(search_value))  # Using wildcard search for 'LIKE' queries
        rows = curr.fetchall()
        print(rows)
        # Clear existing rows in student_table
        for row in student_table.get_children():
            student_table.delete(row)

        # Inserting fetched data into student_table
        if(len(rows)==0):
            messagebox.showerror("Error", "No result found")
        else:    
           for row in rows:
            student_table.insert('', 'end', values=row)

        conn.close()

     except pymysql.Error as e:
        messagebox.showerror("Error", f"Error searching data: {str(e)}")



btn_frame=tk.Frame(detail_frame,bg="lightgrey",bd=10,relief=tk.GROOVE)
btn_frame.place(x=20,y=375,width=350,height=72)

add_btn=tk.Button(btn_frame,bg="lightgreen",text="Add",bd=7,font=("Arial",11),width=6,command=add_func)
add_btn.grid(row=0,column=0,padx=2,pady=2)

update_btn=tk.Button(btn_frame,bg="orange",text="Update",bd=7,font=("Arial",11),width=6,command=update_func)
update_btn.grid(row=0,column=1,padx=2,pady=2)

delete_btn=tk.Button(btn_frame,bg="red",text="Delete",bd=7,font=("Arial",11),width=6,command=delete_func)
delete_btn.grid(row=0,column=2,padx=2,pady=2)

clear_btn=tk.Button(btn_frame,bg="blue",text="Clear",bd=7,font=("Arial",11),width=6,command=clear_func)
clear_btn.grid(row=0,column=3,padx=2,pady=2)

search_frame=tk.Frame(data_frame,bg="lightgrey",bd=10,relief =tk.GROOVE)
search_frame.pack(side=tk.TOP,fill=tk.X)

search_lbl=tk.Label(search_frame,text="Search",bg="lightgrey",font=("Arial",14))
search_lbl.grid(row=0,column=0,padx=12,pady=2)

search_in=ttk.Combobox(search_frame,font=("Arial",14),state="readonly",textvariable=search_by)
search_in['values']=("Name","Rollno","Contact","Email","Dept","DOB")
search_in.grid(row=0,column=1,padx=12,pady=2)
search_in.current(0)
txtsearch=tk.Entry(search_frame,font=('arial',17,'bold'),relief='ridge',width=8,bd=3,textvariable=search_entry)
txtsearch.grid(row=0,column=2)

search_btn=tk.Button(search_frame,text="Search",font=("Arial",13),bd=9,width=14,bg="lightblue",command=search)
search_btn.grid(row=0,column=0,padx=12,pady=2)

showall_btn=tk.Button(search_frame,text="Show all",font=("Arial,13"),bd=9,width=10,bg="lightgreen",command=fetch_data)
showall_btn.grid(row=0,column=4,padx=12,pady=2)

main_frame=tk.Frame(data_frame,bg="lightgrey",bd=11,relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)

y_scroll=tk.Scrollbar(main_frame,orient=tk.VERTICAL)
x_scroll=tk.Scrollbar(main_frame,orient=tk.HORIZONTAL)

student_table=ttk.Treeview(main_frame,columns=("Rollno","Name","Dept","Email","Contact","Gender","DOB","Father'sname","Address"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

student_table.heading("Rollno",text="Rollno")
student_table.heading("Name",text="Name")
student_table.heading("Dept",text="Dept")
student_table.heading("Email",text="Email")
student_table.heading("Contact",text="Contact")
student_table.heading("Gender",text="Gender")
student_table.heading("DOB",text="DOB")
student_table.heading("Father'sname",text="Father'sname")
student_table.heading("Address",text="Address")

student_table['show']='headings'

student_table.column("Rollno",width=100)
student_table.column("Name",width=100)
student_table.column("Dept",width=100)
student_table.column("Email",width=100)
student_table.column("Contact",width=100)
student_table.column("Gender",width=100)
student_table.column("DOB",width=100)
student_table.column("Father'sname",width=100)
student_table.column("Address",width=100)

fetch_data()

student_table.bind("<ButtonRelease-1>",get_cursor)

student_table.pack(fill=tk.BOTH,expand=True)
win.mainloop()