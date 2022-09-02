from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
from PIL import Image  
import PIL  
import os
from tkinter import messagebox

class StudentImage:
    def __init__(self,root):
        self.var_SidImg=StringVar()
        self.var_SNameImg=StringVar()
        self.imgpath=StringVar()

        Top_Label=Label(root,text="Import Student Image ",bg='white',width=20,font=("times new roman",15,"bold")).grid(row=0,column=0,columnspan=2,pady=15)
        
        SidImg_Label=Label(root,text="Student ID : ",width=20,font=("times new roman",13,"bold"))
        SidImg_Label.grid(row=1,column=0)
        SidImg_entry=ttk.Entry(root,textvariable=self.var_SidImg,width=23,font=("times new roman",13,"bold")).grid(row=1,column=1)
        
        empty_Label=Label(root,text="\n",width=20,font=("times new roman",6,"bold")).grid(row=2,column=1)

        SidImg_Label=Label(root,text="Student Name : ",width=20,font=("times new roman",13,"bold"))
        SidImg_Label.grid(row=3,column=0)
        SidImg_entry=ttk.Entry(root,textvariable=self.var_SNameImg,width=23,font=("times new roman",13,"bold")).grid(row=3,column=1)
       
        empty_Label=Label(root,text="\n",width=20,font=("times new roman",6,"bold")).grid(row=4,column=2)

        def open_file():
            file = filedialog.askopenfile(mode='r', filetypes=[('Image Files', '*jpg')])
            if file:
                filepath = os.path.abspath(file.name)
                self.imgpath = str(filepath)
                Label(root, text="File selected : " + self.imgpath, font=('Aerial 11')).grid(row=6,column=0,columnspan=2)
        label = Label(root, text="", font=('Georgia 13'))
        label.grid(row=4,column=1)
        ttk.Button(root, text="Browse", command=open_file).grid(row=5,column=0,columnspan=2)

        
        save_btn=Button(root,text="save",command=self.AddImage,width=13,height=1,font=("times new roman",13,"bold"),bg="indianred",fg="white")
        save_btn.grid(row=7,column=0,columnspan=2,pady=15)

    def reset(self):
        self.var_SidImg.set("")
        self.var_SNameImg.set("")


    def AddImage(self):
        try:
            print(self.var_SidImg.get())
            print(self.var_SNameImg.get())
            print(self.imgpath)
            picture = Image.open(self.imgpath)  
            picture = picture.save(f"images\\{self.var_SidImg.get()}.jpg")
            self.reset()             
        except Exception as es:
            messagebox.showerror("Error",f"Please check ID , Name and make sure file is selected properly",parent=root)

if(__name__)=="__main__":
    root= Tk()
    root.geometry("450x550")
    obj=StudentImage(root)
    
    root.mainloop()