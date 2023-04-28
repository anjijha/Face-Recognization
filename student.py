from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        root.state('zoomed')
    # Course dictionary

        self.dictDepartmentCourse = {
        "B.Tech": ["Computer Science", "IT", "Civil", "Mechanical", "Elecrical", "Electronics"],
        "B.Sc": ["Bsc Geology", "Bio Medical"],
        "BCA": ["Computer Science"]
        }

        #=============variables=============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        #first image
        img = Image.open("college_images/face-recognition.png ")
        img=img.resize((500, 130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
#second image
        img1 = Image.open("college_images/smart-attendance.jpg")
        img1=img1.resize((500, 130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130) 
#Third image
        img2 = Image.open("college_images/classstudent.jpg ")
        img2=img2.resize((500, 130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130) 

        #background image       
        img3 = Image.open("college_images/wp2551980.jpg ")
        img3=img3.resize((1530, 710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710) 

        title_lb1=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new romain",35,"bold"),bg="dark violet",fg="white")
        title_lb1.place(x=0, y=0, width=1530,height=45)
#Fram8
        main_frame = Frame(bg_img, bd =2,bg="white")
        main_frame.place(x=0,y=45, width=1530,height=617)

#left label Frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details")
        Left_frame.place(x=0,y=10,width=700, height=590)

        img_left = Image.open("college_images/AdobeStock_303989091.jpeg ")
        img_left=img_left.resize((700, 130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=745,height=130)

#current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course details")
        current_course_frame.place(x=5,y=135,width=690, height=110)

#Department
        dep_label=Label(current_course_frame,text="Department",font=("Helvetica", 13 ,"bold"),bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W, pady=5)
        self.dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new romain", 10 ,"bold"),state="readonly",width=20)
        self.dep_combo["values"]= list(self.dictDepartmentCourse.keys())
        self.dep_combo.current(0)
        self.dep_combo.grid(row=0,column=1,padx=10,sticky=W, pady=5)
        self.dep_combo.bind("<<ComboboxSelected>>", self.functionCourse)
#Course
        course_label=Label(current_course_frame,text="Course",font=("Helvetica", 13 ,"bold"),bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)
        self.course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new romain",10 ,"bold"),state="readonly",width=20)
        self.course_combo.grid(row=0,column=3,padx=10,sticky=W, pady=5)

#Year
        year_label=Label(current_course_frame,text="Admission Year",font=("Helvetica", 13 ,"bold"),bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W, pady=5)
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new romain", 10, "bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2019-20","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=10,sticky=W, pady=5)

#Semester 
        semester_label=Label(current_course_frame,text="Semester",font=("Helvetica", 13 ,"bold"),bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W, pady=5)
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new romain", 10, "bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester", "Sem 1", "Sem 2", "Sem 3", "Sem 4", "Sem 5", "Sem 6", "Sem 7", "Sem 8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=10,sticky=W, pady=5)  

#class student information 
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class student information")
        class_student_frame.place(x=5,y=250,width=690, height=320)       
#StudentID

        studentId_label=Label(class_student_frame,text="Student ID",font=("Helvetica",13 ,"bold"),bg="white")
        studentId_label.grid(row=0, column=0, padx=10,pady=5, sticky=W) 

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_id, width=24, font=("times new romain",10 ,"bold"))
        studentID_entry.grid(row=0,column=1, padx=10, sticky=W, pady=5)
#student name        

        studentName_label=Label(class_student_frame,text="Student Name",font=("Helvetica",13 ,"bold"),bg="white")
        studentName_label.grid(row=0, column=2, padx=10,pady=5, sticky=W) 

        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=24,font=("times new romain",10 ,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10, pady=5,sticky=W)

#class division
        class_div_label=Label(class_student_frame,text="Class Division",font=("Helvetica",13 ,"bold"),bg="white")
        class_div_label.grid(row=1, column=0, padx=10,pady=5, sticky=W) 


        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new romain",10 ,"bold"),state="readonly",width=21)
        div_combo["values"]=("Select", "A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10, pady=5, sticky=W)
#Roll no
        roll_no_label=Label(class_student_frame,text="Roll Number",font=("Helvetica",13 ,"bold"),bg="white")
        roll_no_label.grid(row=1, column=2, padx=10,pady=5, sticky=W) 

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=24,font=("times new romain",10 ,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10, pady=5,sticky=W)
#Gender        

        gender_label=Label(class_student_frame,text="Gender",font=("Helvetica",13 ,"bold"),bg="white")
        gender_label.grid(row=2, column=0, padx=10,pady=5, sticky=W) 


        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new romain",10 ,"bold"),state="readonly",width=21)
        gender_combo["values"]=("Select","Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10, pady=5, sticky=W)


#dob
        dob_label=Label(class_student_frame,text="Date of Birth",font=("Helvetica",13 ,"bold"),bg="white")
        dob_label.grid(row=2, column=2, padx=10,pady=5, sticky=W) 

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=24,font=("times new romain",10 ,"bold"))
        dob_entry.grid(row=2,column=3,padx=10, pady=5,sticky=W)

#Email
        email_label=Label(class_student_frame,text="E-mail",font=("Helvetica",13 ,"bold"),bg="white")
        email_label.grid(row=3, column=0, padx=10,pady=5, sticky=W) 

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=24,font=("times new romain",10 ,"bold"))
        email_entry.grid(row=3,column=1,padx=10, pady=5,sticky=W)

#phone no
        phone_label=Label(class_student_frame,text="Phone Number",font=("Helvetica",13 ,"bold"),bg="white")
        phone_label.grid(row=3, column=2, padx=10,pady=5, sticky=W) 

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=24,font=("times new romain",10 ,"bold"))
        phone_entry.grid(row=3,column=3,padx=10, pady=5,sticky=W)

#Address        

        address_label=Label(class_student_frame,text="Address",font=("Helvetica",13 ,"bold"),bg="white")
        address_label.grid(row=4, column=0, padx=10,pady=5, sticky=W) 

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=24,font=("times new romain",10,"bold"))
        address_entry.grid(row=4,column=1,padx=10, pady=5,sticky=W)
#Teacher name        

        teacher_label=Label(class_student_frame,text="Teacher's Name",font=("Helvetica",13 ,"bold"),bg="white")
        teacher_label.grid(row=4, column=2, padx=10,pady=5, sticky=W) 

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=24,font=("times new romain",10 ,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10, pady=5,sticky=W)

#radio button
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radionbtn1.grid(row=6,column=0, pady=10)

        radionbtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radionbtn2.grid(row=6,column=1)

#buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=215,width=665,height=35)

        save_btn=Button(btn_frame,text = "Save",command=self.add_data,width=15, font=("times new roman",13,"bold"),bg="dark violet",fg="white")
        save_btn.grid(row=0,column=0, padx=3)

        Update_btn=Button(btn_frame,text = "Update",command=self.update_data,width=15, font=("times new roman",13,"bold"),bg="dark violet",fg="white")
        Update_btn.grid(row=0,column=1, padx=3)

        Reset_btn=Button(btn_frame,text = "Reset",command=self.reset_data,width=15, font=("times new roman",13,"bold"),bg="dark violet",fg="white")
        Reset_btn.grid(row=0,column=2, padx=3)

        Delete_btn=Button(btn_frame,text = "Delete",command=self.delete_data,width=15, font=("times new roman",13,"bold"),bg="dark violet",fg="white")
        Delete_btn.grid(row=0,column=3, padx=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=250,width=665,height=35)

        take_photo_btn=Button(btn_frame1,text = "Take Photo Sample",command=self.generate_dataset,width=32, font=("times new roman",13,"bold"),bg="dark violet",fg="white")
        take_photo_btn.grid(row=0,column=0, padx=2)

        update_photo_btn=Button(btn_frame1,text = "Update Photo sample",width=32 ,font=("times new roman",13,"bold"),bg="dark violet",fg="white")
        update_photo_btn.grid(row=0,column=1, padx=3)


#Right label Frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details")
        Right_frame.place(x=715,y=10,width=800, height=590)

        img_right = Image.open("college_images/gettyimages-1022573162.jpg ")
        img_right=img_right.resize((800, 130),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=800,height=130)

#Search System
        
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",13,"bold"))
        Search_frame.place(x=5,y=135,width=785,height=70)

        search_label=Label(Search_frame,text="Search By",font=("Helvetica",13 ,"bold"),bg="brown",fg="white")
        search_label.grid(row=0, column=0, padx=10,pady=5, sticky=W) 

        search_combo=ttk.Combobox(Search_frame,font=("times new romain", 10, "bold"),state="readonly",width=20)
        search_combo["values"]=("Select","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W) 

        search_entry=ttk.Entry(Search_frame,width=24,font=("times new romain",10,"bold"))
        search_entry.grid(row=0,column=2,padx=10, pady=5,sticky=W)

        search_btn=Button(Search_frame,text = "Search",width=15, font=("times new roman",13,"bold"),bg="dark violet",fg="white")
        search_btn.grid(row=0,column=3,padx=3)

        showAll_btn=Button(Search_frame,text = "Showall",width=15, font=("times new roman",13,"bold"),bg="dark violet",fg="white")
        showAll_btn.grid(row=0,column=4,padx=3)

#Table Frame system Scrollbar
        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=785,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Admission Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Rollno")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=150)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100, anchor=tk.CENTER)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100, anchor=tk.CENTER)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #===============function decration=======================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()==""or self.var_id.get()=="":
            messagebox.showerror("Error","All Field are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="extra@191712",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                           self.var_dep.get(),                
                                                                                                           self.var_course.get(),                
                                                                                                           self.var_year.get(),                
                                                                                                           self.var_semester.get(),                
                                                                                                           self.var_id.get(),                
                                                                                                           self.var_name.get(),                
                                                                                                           self.var_div.get(),                
                                                                                                           self.var_roll.get(),                
                                                                                                           self.var_gender.get(),                
                                                                                                           self.var_dob.get(),                
                                                                                                           self.var_email.get(),                
                                                                                                           self.var_phone.get(),                
                                                                                                           self.var_address.get(),                
                                                                                                           self.var_teacher.get(),                
                                                                                                           self.var_radio1.get()))
                messagebox.showinfo("Success","Student details has been added", parent=self.root)
                conn.commit()
                conn.close()
                self.fetch_data()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                 
   

    #=================fetch data ============      
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="extra@191712",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()        
                     
   #=========get Cursor =============              
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]),

        
    #========== update function ============
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()==""or self.var_id.get()=="":
            messagebox.showerror("Error","All Field are required",parent=self.root)   
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student datails",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="extra@191712",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                       self.var_dep.get(),                
                                                                                                                                                                                       self.var_course.get(),                
                                                                                                                                                                                       self.var_year.get(),                
                                                                                                                                                                                       self.var_semester.get(),                
                                                                                                                                                                                       self.var_name.get(),                
                                                                                                                                                                                       self.var_div.get(),                
                                                                                                                                                                                       self.var_roll.get(),                
                                                                                                                                                                                       self.var_gender.get(),                
                                                                                                                                                                                       self.var_dob.get(),                
                                                                                                                                                                                       self.var_email.get(),                
                                                                                                                                                                                       self.var_phone.get(),                
                                                                                                                                                                                       self.var_address.get(),                
                                                                                                                                                                                       self.var_teacher.get(),                
                                                                                                                                                                                       self.var_radio1.get(),
                                                                                                                                                                                       self.var_id.get()))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()        
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    #delete function 
    def delete_data(self):
        if self.var_id.get()=="":            
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this Student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="extra@191712",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)                   
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    #reset function
    def reset_data(self):
        self.var_dep.set("Select Deparment")    
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_id.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        self.var_name.set("")
    
    # Function course
    def functionCourse(self, events = ""):
        dep = self.dep_combo.get()
        listCourse = self.dictDepartmentCourse[dep]
        self.course_combo.config(values=listCourse)
        self.course_combo.current(0)
        

     #=================== Generate data set or Take photo Sample ==============
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()==""or self.var_id.get()=="":
            messagebox.showerror("Error","All Field are required",parent=self.root)   
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="extra@191712",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                       self.var_dep.get(),                
                                                                                                                                                                                       self.var_course.get(),                
                                                                                                                                                                                       self.var_year.get(),                
                                                                                                                                                                                       self.var_semester.get(),                
                                                                                                                                                                                       self.var_name.get(),                
                                                                                                                                                                                       self.var_div.get(),                
                                                                                                                                                                                       self.var_roll.get(),                
                                                                                                                                                                                       self.var_gender.get(),                
                                                                                                                                                                                       self.var_dob.get(),                
                                                                                                                                                                                       self.var_email.get(),                
                                                                                                                                                                                       self.var_phone.get(),                
                                                                                                                                                                                       self.var_address.get(),                
                                                                                                                                                                                       self.var_teacher.get(),                
                                                                                                                                                                                       self.var_radio1.get(),
                                                                                                                                                                                       self.var_id.get()==id+1 


                                                                                                                                                                                 ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #==========Load predefined data on face frontals from opencv==========
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor=1.3
                    # Minimum Neighbor=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped 

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame)is not None:
                        img_id+=1                   
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+" .jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2) 
                        cv2.imshow("Crooped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!!", parent=self.root)     
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)       
                
                


           

        

if __name__ == "__main__":
      root=Tk()
      obj=Student(root)
      root.mainloop()