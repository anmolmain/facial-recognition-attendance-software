from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from PIL import Image
import os
from tkinter import filedialog
from import_image import StudentImage
from attendanceMarker import AttMark
from Add_remove_students_to_db import Student
import pandas as pd
class Attendance_Management_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("425x700+200+0")
        root.resizable(False,False)
        self.root.title("Attendance Management System")
        headingTop=Label(self.root,text=" Facial Recognition \n Attendance System ",font=("times new roman",25,'bold'),bg='red',fg='white').grid(padx=15,pady=25,column=0,row=0,columnspan=3)
        a=Button(self.root,text="Add/Remove\nStudent",command=self.AddRemoveStudent,width=10,height=2,font=("times new roman",13,'bold'),bg='wheat',border=11).grid(column=0,row=1)
        b=Button(self.root,text="Mark\nAttendance",command=self.markingAttendance,width=10,height=2,font=("times new roman",13,'bold'),bg='wheat',border=11).grid(column=1,row=1)
        c=Button(self.root,text="Import Image",command=self.imageImporting,width=10,height=2,font=("times new roman",13,'bold'),bg='wheat',border=11).grid(column=2,row=1)
        headingTop=Label(self.root,text="\n   Punjabi   \nUniversity \n",font=("times new roman",60,'bold'),bg='red',fg='white').grid(padx=15,pady=25,column=0,row=2,rowspan=6,columnspan=3)
        d=Button(self.root,text="Exel sheet",command=self.exelDownload,width=10,height=2,font=("times new roman",13,'bold'),bg='wheat',border=11).grid(column=0,row=9)
        e=Button(self.root,text="exit",command=self.exit,width=10,height=2,font=("times new roman",13,'bold'),bg='wheat',border=11).grid(column=2,row=9)
    def exelDownload(self):
        df_new = pd.read_csv('attendance.csv')
        GFG = pd.ExcelWriter('attendance.xlsx')
        df_new.to_excel(GFG, index=False)
        GFG.save()
    def imageImporting(self):
        self.new_window=Toplevel(self.root)
        self.app=StudentImage(self.new_window)
    def markingAttendance(self):
        self.new_window=Toplevel(self.root)
        self.app=AttMark()
    def AddRemoveStudent(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    def exit():
        root. destroy()

if(__name__)=="__main__":
    root= Tk()
    obj=Attendance_Management_system(root)    
    root.mainloop()





    