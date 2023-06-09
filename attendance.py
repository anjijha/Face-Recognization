from tkinter import*
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        self.root.state('zoomed')

        #==========================variable================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

#first image
        img = Image.open("college_images/classstudent.jpg ")
        img=img.resize((800, 210),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=210)
#second image
        img1 = Image.open("college_images/smart-attendance.jpg")
        img1=img1.resize((800, 210),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=210)

        #background image       
        img3 = Image.open("college_images/wp2551980.jpg ")
        img3=img3.resize((1540, 710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1540,height=710) 

        title_lb1=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new romain",35,"bold"),bg="dark violet",fg="white")
        title_lb1.place(x=0, y=0, width=1540,height=45)

        #Frame
        main_frame = Frame(bg_img, bd=2,bg="white")
        main_frame.place(x=0,y=45, width=1540,height=600)

        #left label Frame
             
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details")
        Left_frame.place(x=10,y=10,width=745, height=510)

        img_left = Image.open("college_images/face-recognition.png")
        img_left=img_left.resize((730, 130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=730,height=130)

        left_inside_frame = Frame(Left_frame, bd =2, relief=RIDGE,bg="white")
        left_inside_frame.place(x=5,y=135, width=730,height=350)

        #label and entry
        #attendance id
        attendance_label=Label(left_inside_frame,text="Attendance ID",font=("Helvetica",13 ,"bold"),bg="white")
        attendance_label.grid(row=0, column=0, padx=10,pady=5,sticky=W) 

        attendance_entry=ttk.Entry(left_inside_frame,width=24,textvariable=self.var_atten_id,font=("times new romain",10 ,"bold"))
        attendance_entry.grid(row=0,column=1,padx=10,sticky=W, pady=5)

        #Name
        nameLabel=Label(left_inside_frame,text="Name",bg="white",font="Helvetica 13 bold")
        nameLabel.grid(row=0, column=2, padx=10,pady=5, sticky=W) 

        atten_name=ttk.Entry(left_inside_frame,width=24,textvariable=self.var_atten_name,font=("times new romain",10 ,"bold"))
        atten_name.grid(row=0,column=3,pady=5, padx=10, sticky=W)

        #date
        dateLabel=Label(left_inside_frame,text="Date",bg="white",font=("Helvetica",13 ,"bold"))
        dateLabel.grid(row=1, column=0, padx=10, pady=5, sticky=W) 

        atten_date=ttk.Entry(left_inside_frame,width=24,textvariable=self.var_atten_date,font=("times new romain",10,"bold"))
        atten_date.grid(row=1,column=1,pady=5, padx=10, sticky=W)

        #department
        depLabel=Label(left_inside_frame,text="Department",bg="white",font=("Helvetica",13 ,"bold"))
        depLabel.grid(row=1, column=2, pady=5, padx=10, sticky=W) 

        atten_dep=ttk.Entry(left_inside_frame,width=24,textvariable=self.var_atten_dep,font=("times new romain",10 ,"bold"))
        atten_dep.grid(row=1,column=3, pady=5, padx=10, sticky=W)

        #time
        timeLabel=Label(left_inside_frame,text="Time",bg="white",font=("Helvetica",13 ,"bold"))
        timeLabel.grid(row=2, column=0, pady=5, padx=10, sticky=W) 

        atten_time=ttk.Entry(left_inside_frame,width=24,textvariable=self.var_atten_time,font=("times new romain",10,"bold"))
        atten_time.grid(row=2,column=1, pady=5, padx=10, sticky=W)

        #roll
        rollLabel=Label(left_inside_frame,text="Roll Number",bg="white",font=("Helvetica",13,"bold"))
        rollLabel.grid(row=2, column=2, pady=5, padx=10, sticky=W) 

        atten_roll=ttk.Entry(left_inside_frame,width=24,textvariable=self.var_atten_roll,font=("times new romain",10,"bold"))
        atten_roll.grid(row=2,column=3, pady=5, padx=10, sticky=W)

        #attendance
        attendanceLabel=Label(left_inside_frame,text="Attendance Status:",bg="white",font=("Helvetica",13,"bold"))
        attendanceLabel.grid(row=3, column=0, pady=5, padx=10, sticky=W) 

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,font=("times new romain",10,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1, pady=5, padx=10, sticky=W)
        self.atten_status.current(0)

        #buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)

        save_btn=Button(btn_frame,text = "Import csv",command=self.importCsv,width=17, font=("times new roman",13,"bold"),bg="dark violet",fg="white")
        save_btn.grid(row=0,column=0)

        Update_btn=Button(btn_frame,text = "Export csv",command=self.exportCsv,width=17, font=("times new roman",13,"bold"),bg="dark violet",fg="white")
        Update_btn.grid(row=0,column=1)

        Reset_btn=Button(btn_frame,text = "Reset",width=17,command=self.reset_data, font=("times new roman",13,"bold"),bg="dark violet",fg="white")
        Reset_btn.grid(row=0,column=2)

        Delete_btn=Button(btn_frame,text = "Delete",width=17, font=("times new roman",13,"bold"),bg="dark violet",fg="white")
        Delete_btn.grid(row=0,column=3)


        #Right label Frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details")
        Right_frame.place(x=770,y=10,width=750, height=510)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=0,y=0,width=750,height=490)

        #================Scrollbar table=============
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width="100",anchor=tk.CENTER)
        self.AttendanceReportTable.column("roll",width="100",anchor=tk.CENTER)
        self.AttendanceReportTable.column("name",width="100",anchor=tk.CENTER)
        self.AttendanceReportTable.column("department",width="100",anchor=tk.CENTER)
        self.AttendanceReportTable.column("time",width="100",anchor=tk.CENTER)
        self.AttendanceReportTable.column("date",width="100",anchor=tk.CENTER)
        self.AttendanceReportTable.column("attendance",width="100",anchor=tk.CENTER)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        #===========fetch data=============
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
              self.AttendanceReportTable.insert("",END,values=i)
      #import csv        
    def importCsv(self):
        global mydata 
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("AL1 File","*.*")),parent=self.root)       
        with open(fln) as myfile:
             csvread=csv.reader(myfile,delimiter=",") 
             for i in csvread:
                mydata.append(i)
             self.fetchData(mydata) 
     #export csv 
    def  exportCsv(self):
        try:
                if len(mydata)<1:
                   messagebox.showerror("No Data","No Data found to export",parent=self.root)
                   return False
                fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("AL1 File","*.*")),parent=self.root) 
                with open(fln,mode="w",newline="") as myfile:
                   exp_write=csv.writer(myfile,delimiter=",")
                   for i in mydata:
                        exp_write.writerow(i)
                   messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully", parent=self.root)
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']  
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
          
          

                                      





        
if __name__ == "__main__":
      root=Tk()
      obj=Attendance(root)
      root.mainloop()