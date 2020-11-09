#!/usr/bin/env python
# coding: utf-8

# In[14]:


from tkinter import*
import json
import tkinter.messagebox as tmsg
from PIL import ImageTk
from tkinter import ttk
root=Tk()
text_file=Label(root,text="Data Manager",font="comicsansms 30 bold",fg="blue",bg="yellow")
image_me=ImageTk.PhotoImage(file="Main.jpg")
label_me=Label(image=image_me)
text_file.grid(row=0,column=2,padx=58,pady=15)
label_me.grid(row=1,column=2,padx=120)

root.configure(background='cornflowerblue')
root.iconbitmap(r'Icon.ico')

root.maxsize(850,580)
root.minsize(850,580)
root.title("Data Manager")
roll_no={}

def store():
    personal={}
    personal['Name']=name_value.get()
    personal['Roll No.']=roll_value.get()
    personal["Father's Name"]=F_name_value.get()
    personal["Mother's Name"]=M_name_value.get()
    personal['Mobile No.']=mob_value.get()
    personal['Address']=address_value.get()
    
    roll_no[roll_value.get()]=personal
    with open("Personal.json",'w') as json_file:
        json.dump(roll_no,json_file)
def store2():
    course={}
    course['Roll No.']=roll_value.get()
    course['Subject ID']=Sub_ID_value.get()
    course['Subject Name']=Sub_name_value.get()
    course['Credits']=credits_value.get()
    roll_no[roll_value.get()]=course
    with open("Subject.json",'w') as json_file:
        json.dump(roll_no,json_file)

def store3():
    marks={}
    marks['Roll No.']=roll_value.get()
    marks['Subject ID']=Sub_ID_value.get()
    marks['Subject Name']=Sub_name_value.get()
    marks['Maximum Marks']=max_marks_value.get()
    marks['Obtained Marks']=obt_marks_value.get()
    roll_no[roll_value.get()]=marks
    with open("Marks.json",'w') as json_file:
        json.dump(roll_no,json_file)
        
def Output(): 
        if var.get()=="1":
            with open("Personal.json") as f:
                data=f.read()
                temp=json.loads(data)
                if roll_main_value.get() in temp:
                        l1=temp[roll_main_value.get()]
                        l1.pop("Roll No.")
                        tmsg.showinfo("Desired Info",f"{l1}")
                else:
                    tmsg.showinfo("Error",f"There is no information stored for roll number {roll_main_value.get()}")
        if var.get()=="2":
            with open("Subject.json") as f:
                data=f.read()
                temp=json.loads(data)
                if roll_main_value.get() in temp:
                    l1=temp[roll_main_value.get()]
                    l1.pop("Roll No.")
                    tmsg.showinfo("Desired Info",f"{l1}")
                else:
                    tmsg.showinfo("Error",f"There is no information stored for roll number {roll_main_value.get()}")
        if var.get()=="3":
            with open("Marks.json") as f:
                data=f.read()
                temp=json.loads(data)
                if roll_main_value.get() in temp:
                    l1=temp[roll_main_value.get()]
                    l1.pop("Roll No.")
                    tmsg.showinfo("Desired Info",f"{l1}")
                else:
                    tmsg.showinfo("Error",f"There is no information stored for roll number {roll_main_value.get()}")
            
            
            
def packing():
    Start_2.grid_forget()
    roll.grid_forget()
    roll_entry.grid_forget()
    Sub_ID.grid_forget()
    Sub_ID_entry.grid_forget()
    
    Sub_name.grid_forget()
    Sub_name_entry.grid_forget()
    
    credits.grid_forget()
    credits_entry.grid_forget()
    Button_2.grid_forget()
    
    
    Start_3.grid_forget()
    
    roll.grid_forget()
    roll_entry.grid_forget()
    Sub_ID.grid_forget()
    Sub_ID_entry.grid_forget()
    
    Sub_name.grid_forget()
    Sub_name_entry.grid_forget()
    
    max_marks.grid_forget()
    max_marks_entry.grid_forget()
    
    obt_marks.grid_forget()
    obt_marks_entry.grid_forget()
    
    Button_3.grid_forget()
    
    Start_4.grid_forget()
    roll_main.grid_forget()
    roll_main_entry.grid_forget()
    
    radio_1.grid_forget()
    radio_2.grid_forget()
    radio_3.grid_forget()
    Button_4.grid_forget()
    
    text_file.grid_forget()
    label_me.grid_forget()
        
    
    
    Start.grid(row=0,column=1,padx=6,pady=15)
    name.grid(row=1,column=0,pady=6)
    name_entry.grid(row=1,column=1)
    roll.grid(row=2,column=0,pady=6)
    roll_entry.grid(row=2,column=1)
    F_name.grid(row=3,column=0,pady=6,padx=15)
    F_name_entry.grid(row=3,column=1)
    M_name.grid(row=4,column=0,pady=6,padx=15)
    M_name_entry.grid(row=4,column=1)
    mob.grid(row=5,column=0,pady=6)
    mob_entry.grid(row=5,column=1)
    address.grid(row=7,column=0,pady=6)
    address_entry.grid(row=7,column=1)
    Button_1.grid(row=8,column=1)
def packing_2():
    Start.grid_forget()
    
    name.grid_forget()
    name_entry.grid_forget()
    roll.grid_forget()
    roll_entry.grid_forget()
    F_name.grid_forget()
    F_name_entry.grid_forget()
    M_name.grid_forget()
    M_name_entry.grid_forget()
    mob.grid_forget()
    mob_entry.grid_forget()
    address.grid_forget()
    address_entry.grid_forget()
    Button_1.grid_forget()
    
    
    Start_3.grid_forget()
    
    roll.grid_forget()
    roll_entry.grid_forget()
    Sub_ID.grid_forget()
    Sub_ID_entry.grid_forget()
    
    Sub_name.grid_forget()
    Sub_name_entry.grid_forget()
    
    max_marks.grid_forget()
    max_marks_entry.grid_forget()
    
    obt_marks.grid_forget()
    obt_marks_entry.grid_forget()
    
    Button_3.grid_forget()
    
    Start_4.grid_forget()
    roll_main.grid_forget()
    roll_main_entry.grid_forget()
    
    radio_1.grid_forget()
    radio_2.grid_forget()
    radio_3.grid_forget()
    Button_4.grid_forget()
    
    text_file.grid_forget()
    label_me.grid_forget()
        
    
    
    Start_2.grid(row=0,column=1,pady=15)
    
    roll.grid(row=1,column=0,pady=7)
    roll_entry.grid(row=1,column=1)
    
    Sub_ID.grid(row=2,column=0,pady=7)
    Sub_ID_entry.grid(row=2,column=1)
    
    Sub_name.grid(row=3,column=0,pady=7,padx=20)
    Sub_name_entry.grid(row=3,column=1)
    
    credits.grid(row=4,column=0,pady=7)
    credits_entry.grid(row=4,column=1)
    
    
    Button_2.grid(row=5,column=1,pady=8)

def packing_3():
    Start.grid_forget()
    
    name.grid_forget()
    name_entry.grid_forget()
    roll.grid_forget()
    roll_entry.grid_forget()
    F_name.grid_forget()
    F_name_entry.grid_forget()
    M_name.grid_forget()
    M_name_entry.grid_forget()
    mob.grid_forget()
    mob_entry.grid_forget()
    address.grid_forget()
    address_entry.grid_forget()
    Button_1.grid_forget()
    
    Start_2.grid_forget()
    
    roll.grid_forget()
    roll_entry.grid_forget()
    Sub_ID.grid_forget()
    Sub_ID_entry.grid_forget()
    
    Sub_name.grid_forget()
    Sub_name_entry.grid_forget()
    
    credits.grid_forget()
    credits_entry.grid_forget()
    Button_2.grid_forget()   
    
    Start_4.grid_forget()
    roll_main.grid_forget()
    roll_main_entry.grid_forget()
    
    radio_1.grid_forget()
    radio_2.grid_forget()
    radio_3.grid_forget()
    Button_4.grid_forget()
    
    text_file.grid_forget()
    label_me.grid_forget()
    
    
    
    
    
    Start_3.grid(row=0,column=1,pady=15)
    
    roll.grid(row=1,column=0,pady=8)
    roll_entry.grid(row=1,column=1)
    
    Sub_ID.grid(row=2,column=0,pady=8)
    Sub_ID_entry.grid(row=2,column=1)
    
    Sub_name.grid(row=3,column=0,pady=8)
    Sub_name_entry.grid(row=3,column=1)
    
    max_marks.grid(row=4,column=0,pady=8,padx=20)
    max_marks_entry.grid(row=4,column=1)
    
    obt_marks.grid(row=5,column=0,pady=8,padx=15)
    obt_marks_entry.grid(row=5,column=1)
    
    Button_3.grid(row=6,column=1,pady=8)
    
def packing_4():
    
    Start_2.grid_forget()
    roll.grid_forget()
    roll_entry.grid_forget()
    Sub_ID.grid_forget()
    Sub_ID_entry.grid_forget()
    
    Sub_name.grid_forget()
    Sub_name_entry.grid_forget()
    
    credits.grid_forget()
    credits_entry.grid_forget()
    Button_2.grid_forget()
    
    
    Start.grid_forget()
    
    name.grid_forget()
    name_entry.grid_forget()
    roll.grid_forget()
    roll_entry.grid_forget()
    F_name.grid_forget()
    F_name_entry.grid_forget()
    M_name.grid_forget()
    M_name_entry.grid_forget()
    mob.grid_forget()
    mob_entry.grid_forget()
    address.grid_forget()
    address_entry.grid_forget()
    Button_1.grid_forget()
    
     
    Start_3.grid_forget()
    
    roll.grid_forget()
    roll_entry.grid_forget()
    Sub_ID.grid_forget()
    Sub_ID_entry.grid_forget()
    
    Sub_name.grid_forget()
    Sub_name_entry.grid_forget()
    
    max_marks.grid_forget()
    max_marks_entry.grid_forget()
    
    
    obt_marks.grid_forget()
    obt_marks_entry.grid_forget()
    
    Button_3.grid_forget()
    
    text_file.grid_forget()
    label_me.grid_forget()
    
    

    
    
    

    
    Start_4.grid(row=0,column=1,pady=15)
    roll_main.grid(row=2,column=0,pady=9)
    roll_main_entry.grid(row=2,column=1)
    
    radio_1.grid(row=3,column=0,pady=9,padx=10)
    radio_2.grid(row=3,column=1,pady=9)
    radio_3.grid(row=3,column=2,pady=9,padx=10)


    Button_4.grid(row=4,column=1,pady=10)

    
    
    

        


    
    

#First Menu
Start=Label(root,text="Registration",font="comicsansms 30 bold",fg="blue",bg="yellow")

    
name=Label(text="Name",fg="blue",font="comicsansms 30 bold")

name_value=StringVar()
name_entry=Entry(root,textvariable=name_value,font="comicsansms 30")

    
roll=Label(text="Roll No.",fg="blue",font="comicsansms 30 bold")

roll_value=StringVar()
roll_entry=Entry(root,textvariable=roll_value,font="comicsansms 30")

    
F_name=Label(text="Father's Name",fg="blue",font="comicsansms 30 bold")

F_name_value=StringVar()
F_name_entry=Entry(root,textvariable=F_name_value,font="comicsansms 30")

    
M_name=Label(text="Mother's Name",fg="blue",font="comicsansms 30 bold")

M_name_value=StringVar()
M_name_entry=Entry(root,textvariable=M_name_value,font="comicsansms 30")


mob=Label(text="Mobile No.",fg="blue",font="comicsansms 30 bold")

mob_value=StringVar()
mob_entry=Entry(root,textvariable=mob_value,font="comicsansms 30")

    
click=Label(text="Courses",fg="blue",font="comicsansms 30 bold")

clicked=StringVar()
clicked.set("Select Course")
course=OptionMenu(root,clicked,"Computer Science Engineering","Mechanical Engineering","Electronics and Communication Engineering","Electrical Engineering","Civil Engineering","Chemical Engineering")

    
address=Label(text="Address",fg="blue",font="comicsansms 30 bold")

address_value=StringVar()
address_entry=Entry(root,textvariable=address_value,font="comicsansms 30")

Button_1=Button(text="Register",bg="blue",fg="white",font="comicsansms 30 bold",command=store)

#Second Menu
Start_2=Label(root,text="Subject Allocation",font="comicsansms 30 bold",fg="blue",bg="yellow")
   
roll=Label(text="Roll No.",fg="blue")

roll_value=StringVar()
roll_entry=Entry(root,textvariable=roll_value,font="comicsansms 30")

    
Sub_ID=Label(text="Subject ID",fg="blue",font="comicsansms 30 bold")

Sub_ID_value=StringVar()
Sub_ID_entry=Entry(root,textvariable=Sub_ID_value,font="comicsansms 30")

    
Sub_name=Label(text="Subject Name",fg="blue",font="comicsansms 30 bold")

Sub_name_value=StringVar()
Sub_name_entry=Entry(root,textvariable=Sub_name_value,font="comicsansms 30")


credits=Label(text="Credits",fg="blue",font="comicsansms 30 bold")

credits_value=StringVar()
credits_entry=Entry(root,textvariable=credits_value,font="comicsansms 30")

Button_2=Button(text="Submit",bg="blue",fg="white",font="comicsansms 30 bold",pady=0,command=store2)

#Third Menu
Start_3=Label(root,text="Marks Allocation",font="comicsansms 30 bold",fg="blue",bg="yellow")
   
roll=Label(text="Roll No.",fg="blue",font="comicsansms 30 bold")

roll_value=StringVar()
roll_entry=Entry(root,textvariable=roll_value,font="comicsansms 30")

    
Sub_ID=Label(text="Subject ID",fg="blue",font="comicsansms 30 bold")

Sub_ID_value=StringVar()
Sub_ID_entry=Entry(root,textvariable=Sub_ID_value,font="comicsansms 30")

    
Sub_name=Label(text="Subject Name",fg="blue",font="comicsansms 30 bold")

Sub_name_value=StringVar()
Sub_name_entry=Entry(root,textvariable=Sub_name_value,font="comicsansms 30")

max_marks=Label(text="Maximum Marks",fg="blue",font="comicsansms 30 bold")

max_marks_value=StringVar()
max_marks_entry=Entry(root,textvariable=max_marks_value,font="comicsansms 30")

obt_marks=Label(text="Obtained Marks",fg="blue",font="comicsansms 30 bold")

obt_marks_value=StringVar()
obt_marks_entry=Entry(root,textvariable=obt_marks_value,font="comicsansms 30")

Button_3=Button(text="Allot",bg="blue",fg="white",font="comicsansms 30 bold",command=store3)

#Final Menu
Start_4=Label(root,text="View Data",font="comicsansms 30 bold",fg="blue",bg="yellow")

    
roll_main=Label(text="Roll No.",fg="blue",font="comicsansms 30 bold")

roll_main_value=StringVar()
roll_main_entry=Entry(root,textvariable=roll_main_value,font="comicsansms 30")

var=StringVar()
var.set("Radio")


radio_1=Radiobutton(text="Personal Details",padx=14,variable=var,value="1",font="comicsansms 15 bold")
radio_2=Radiobutton(text="Subject Details",padx=14,variable=var,value="2",font="comicsansms 15 bold")
radio_3=Radiobutton(text="Marks Info",padx=14,variable=var,value="3",font="comicsansms 15 bold")

Button_4=Button(text="View",bg="blue",fg="white",font="comicsansms 30 bold",command=Output)






    

main_menu=Menu(root)
root.config(menu=main_menu)
main_menu.add_command(label="Student Registration",command=packing)
main_menu.add_command(label="Subject Allocation",command=packing_2)
main_menu.add_command(label="Marks Allocation",command=packing_3)
main_menu.add_command(label="View Data",command=packing_4)

 

root.mainloop()





# In[ ]:




