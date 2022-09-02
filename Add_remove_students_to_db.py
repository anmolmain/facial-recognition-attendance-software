from doctest import script_from_examples
from tkinter import *
from tkinter import ttk
import tkinter
from tkinter.font import Font
from turtle import width
from PIL import Image
from tkinter import messagebox
import mysql.connector 
# import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x720+0+0")
        self.root.title("Student details")
        self.root.configure(bg='white')
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_radioButton1=StringVar()
        self.var_radioButton2=StringVar()
        headingTop=Label(self.root,text=" Add / Remove ",font=("times new roman",25,'bold'),bg='wheat').place(x=0,y=0)
        main_frame=Frame(root,bd=2)
        main_frame.place(x=5,y=50,width=1270,height=660)
        left_frame=LabelFrame(main_frame,bd=2,bg="white",text="Student details",font=("times new roman",18,"bold"))
        left_frame.place(x=10,y=20,width=600,height=630)
        course_frame=LabelFrame(left_frame,bd=2,bg="white",text="Course details",font=("times new roman",15,"bold"))
        course_frame.place(x=5,y=10,width=580,height=140)
        dep_label=Label(course_frame,text="Department : ",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=2,pady=10)
        dep_combo=ttk.Combobox(course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=17)
        dep_combo['values']=("Select department","CSE","ECE","ECM","CIVIL","MEC")
        dep_combo.current(0) 
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        course_label=Label(course_frame,text="Course : ",font=("times new roman",12,"bold"))
        course_label.grid(row=0,column=3,padx=5,pady=10,sticky=W)
        course_combo=ttk.Combobox(course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=17)
        course_combo['values']=("Select Course","B.tech","M.tech","Phd")
        course_combo.current(0) 
        course_combo.grid(row=0,column=4,padx=1,pady=10,sticky=W)
        year_label=Label(course_frame,text="Year : ",font=("times new roman",12,"bold"))
        year_label.grid(row=1,column=0,padx=2,pady=10)
        year_combo=ttk.Combobox(course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=17)
        year_combo['values']=("Select year","1","2","3","4")
        year_combo.current(0) 
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        semester_label=Label(course_frame,text="Semester : ",font=("times new roman",12,"bold"))
        semester_label.grid(row=1,column=3,padx=5,pady=10,sticky=W)
        semester_combo=ttk.Combobox(course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=17)
        semester_combo['values']=("Select Sem","1","2","3","4","5","6","7","8")
        semester_combo.current(0) 
        semester_combo.grid(row=1,column=4,padx=1,pady=10,sticky=W)
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",text="Student Information",font=("times new roman",15,"bold"))
        class_student_frame.place(x=5,y=155,width=580,height=400)
        studentId_label=Label(class_student_frame,text="Student ID : ",font=("times new roman",10,"bold"))
        studentId_label.grid(row=0,column=0,padx=5,pady=10,sticky=W)
        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=18,font=("times new roman",10,"bold")).grid(row=0,column=1,padx=5,pady=10,sticky=W)
        student_Name_Label=Label(class_student_frame,text="Student Name : ",width=20,font=("times new roman",10,"bold"))
        student_Name_Label.grid(row=0,column=2,padx=5,pady=10,sticky=W)
        student_Name_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=18,font=("times new roman",10,"bold")).grid(row=0,column=3,padx=5,pady=10,sticky=W)
        studentDivision_Label=Label(class_student_frame,text="Student Div : ",font=("times new roman",10,"bold"))
        studentDivision_Label.grid(row=1,column=0,padx=5,pady=10,sticky=W)
        studentDivision_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=18,font=("times new roman",10,"bold")).grid(row=1,column=1,padx=5,pady=10,sticky=W)
        student_Roll_Label=Label(class_student_frame,text="Roll No : ",width=20,font=("times new roman",10,"bold"))
        student_Roll_Label.grid(row=1,column=2,padx=5,pady=10,sticky=W)
        student_Roll_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=18,font=("times new roman",10,"bold")).grid(row=1,column=3,sticky=W)
        student_gender_label=Label(class_student_frame,text="Student gender : ",font=("times new roman",10,"bold"))
        student_gender_label.grid(row=2,column=0,padx=5,pady=10,sticky=W)
        student_gender=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",10,"bold"),state="readonly",width=17)
        student_gender['values']=("Select","Male","Female","other")
        student_gender.current(0) 
        student_gender.grid(row=2,column=1,padx=5,pady=10,sticky=W)
        student_dob_Label=Label(class_student_frame,text="Student dob : ",width=20,font=("times new roman",10,"bold"))
        student_dob_Label.grid(row=2,column=2,padx=5,pady=10,sticky=W)
        student_dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=18,font=("times new roman",10,"bold")).grid(row=2,column=3,padx=5,pady=10,sticky=W)
        studentd_email_Label=Label(class_student_frame,text="Student email : ",font=("times new roman",10,"bold"))
        studentd_email_Label.grid(row=3,column=0,padx=5,pady=10,sticky=W)
        studentd_email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=18,font=("times new roman",10,"bold")).grid(row=3,column=1,padx=5,pady=10,sticky=W)
        student_phone_Label=Label(class_student_frame,text="Phone : ",width=20,font=("times new roman",10,"bold"))
        student_phone_Label.grid(row=3,column=2,padx=5,pady=10,sticky=W)
        student_phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=18,font=("times new roman",10,"bold")).grid(row=3,column=3,sticky=W)
        studentd_address_Label=Label(class_student_frame,text="address : ",font=("times new roman",10,"bold"))
        studentd_address_Label.grid(row=4,column=0,padx=5,pady=10,sticky=W)
        studentd_address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=18,font=("times new roman",10,"bold")).grid(row=4,column=1,padx=5,pady=10,sticky=W)
        student_teacherName_Label=Label(class_student_frame,text="Teacher Name : ",width=20,font=("times new roman",10,"bold"))
        student_teacherName_Label.grid(row=4,column=2,padx=5,pady=10,sticky=W)
        student_teacherName_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=18,font=("times new roman",10,"bold")).grid(row=4,column=3,sticky=W)
        # buttonFrame
        btn_frame=Frame(class_student_frame,bd=2,bg='white')
        btn_frame.place(x=3,y=240,width=570,height=65)
        save_btn=Button(btn_frame,text="save",command=self.AddData,width=13,height=2,font=("times new roman",13,"bold"),bg="indianred",fg="white")
        save_btn.grid(row=0,column=0)
        Update_btn=Button(btn_frame,text="update",command=self.updateData,width=13,height=2,font=("times new roman",13,"bold"),bg="indianred",fg="white")
        Update_btn.grid(row=0,column=1)
        Delete_btn=Button(btn_frame,text="Delete",command=self.deleteData,width=13,height=2,font=("times new roman",13,"bold"),bg="indianred",fg="white")
        Delete_btn.grid(row=0,column=2)
        Reset_btn=Button(btn_frame,text="Reset",command =self.resetData,width=13,height=2,font=("times new roman",13,"bold"),bg="indianred",fg="white")
        Reset_btn.grid(row=0,column=3)
        right_frame=LabelFrame(main_frame,bd=2,bg="white",text="",font=("times new roman",18,"bold"))
        right_frame.place(x=650,y=20,width=600,height=630)
        table_frame=LabelFrame(right_frame,bd=2,bg="white",text="",font=("times new roman",18,"bold"))
        table_frame.place(x=3,y=5,width=590,height=620)
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        # self.student_table.heading("dep",text="Department")
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="year")
        self.student_table.heading("sem",text="sem")
        self.student_table.heading("id",text="id")
        self.student_table.heading("name",text="name")
        self.student_table.heading("div",text="div")
        self.student_table.heading("roll",text="roll")
        self.student_table.heading("gender",text="gender")
        self.student_table.heading("dob",text="dob")
        self.student_table.heading("email",text="email")
        self.student_table.heading("phone",text="phone")
        self.student_table.heading("address",text="address")
        self.student_table.heading("teacher",text="teacher")
        self.student_table.heading("photo",text="photo")
        self.student_table["show"]="headings"
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)   
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.getCursor)
        self.fetching()
    def AddData(self):
        if (self.var_dep.get()=="Select department" or self.var_std_id.get()=="" or self.var_std_name.get()==""):
            messagebox.showerror("Error","Please fill all fields",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="mini_projects")
                my_cursor=conn.cursor()
                x=f"insert into StudentDatabase values ('{self.var_dep.get()}','{self.var_course.get()}','{self.var_year.get()}','{self.var_semester.get()}','{self.var_std_id.get()}','{self.var_std_name.get()}','{self.var_div.get()}','{self.var_roll.get()}','{self.var_gender.get()}','{self.var_dob.get()}','{self.var_email.get()}','{self.var_phone.get()}','{self.var_address.get()}','{self.var_teacher.get()}','{self.var_radioButton1.get()}');"
                my_cursor.execute(x)
                conn.commit()
                self.fetching()
                conn.close()
                messagebox.showinfo("Success","Details Added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Error is due to {str(es)}",parent=self.root)
    def fetching(self):
            conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="mini_projects")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from StudentDatabase")
            data=my_cursor.fetchall()
            if(len(data)!=0):
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
    def getCursor(self,event=""):
        cursorFocus=self.student_table.focus()
        content=self.student_table.item(cursorFocus)
        data=content["values"]
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        #self.var_radioButton1.set(data[14])
    def  updateData(self):
        if (self.var_dep.get()=="Select department" or self.var_std_id.get()=="" or self.var_std_name.get()==""):
                messagebox.showerror("Error","Please fill all fields",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this data?",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="mini_projects")
                    my_cursor=conn.cursor()
                    x=f"update StudentDatabase set studepartment='{self.var_dep.get()}',stucourse='{self.var_course.get()}',stuyear='{self.var_year.get()}',stusemester='{self.var_semester.get()}',stuname='{self.var_std_name.get()}',studiv='{self.var_div.get()}',sturoll='{self.var_roll.get()}',stugender='{self.var_gender.get()}',studob='{self.var_dob.get()}',stuemail='{self.var_email.get()}',stuphone='{self.var_phone.get()}',stuaddress='{self.var_address.get()}',stuteacher='{self.var_teacher.get()}',stuphoto='{self.var_radioButton1.get()}' where stuId='{self.var_std_id.get()}';"
                    print(x)
                    my_cursor.execute (x)
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","dATA uPDATED",parent=self.root)
                conn.commit()
                self.fetching()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error is due to {str(es)}",parent=self.root)
    def  deleteData(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Id required",parent=self.root)
        else:
            try:
                delete= messagebox.askyesno("Update","Do you want to Delete this data?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="mini_projects")
                    my_cursor=conn.cursor()
                    my_cursor.execute(f"delete from StudentDatabase where stuId = '{self.var_std_id.get()}'")
                    
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetching()
                conn.close()
                messagebox.showinfo("Success","dATA Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Error is due to {str(es)}",parent=self.root)
    def resetData(self):
        self.var_dep.set("Select department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select year"),
        self.var_semester.set("Select Sem"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set(""),
        self.var_roll.set(""),
        self.var_gender.set("Select"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        #self.var_radioButton1.set(""),
if(__name__)=="__main__":
    root= Tk()
    obj=Student(root)
    root.mainloop()