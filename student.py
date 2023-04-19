from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

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
#third image
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

        title_lb1=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new romain",35,"bold"),bg="white",fg="dark green")
        title_lb1.place(x=0, y=0, width=1530,height=45)
#Frame
        main_frame = Frame(bg_img, bd =2,bg="white")
        main_frame.place(x=20,y=50, width=1480,height=600)

#left label Frame
             
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details")
        Left_frame.place(x=10,y=10,width=760, height=580)

        img_left = Image.open("college_images/AdobeStock_303989091.jpeg ")
        img_left=img_left.resize((745, 130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=745,height=130)
#current course

        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course details")
        current_course_frame.place(x=5,y=135,width=745, height=110)
#Department
        dep_label=Label(current_course_frame,text="Department",font=("times new romain",12 ,"bold"),bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)
        dep_combo=ttk.Combobox(current_course_frame,font=("times new romain",12 ,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer Science","IT","Civil","mechanical","Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=10,sticky=W)
#Course
        course_label=Label(current_course_frame,text="Course",font=("times new romain",13 ,"bold"),bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)
        course_combo=ttk.Combobox(current_course_frame,font=("times new romain",13 ,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","Computer Science","FE","tr","ty","me")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=10,sticky=W)

#Year
        year_label=Label(current_course_frame,text="Year",font=("times new romain",13 ,"bold"),bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)
        dep_combo=ttk.Combobox(current_course_frame,font=("times new romain",13 ,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Year","2019-20","2020-21","2021-22","2022-23","2023-24")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=2, pady=10, sticky=W)

#Semester 
        semester_label=Label(current_course_frame,text="Department",font=("times new romain",12 ,"bold"),bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)
        semester_combo=ttk.Combobox(current_course_frame,font=("times new romain",14  ,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Department","Computer Science","IT","Civil","mechanical","Electrical")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)  

#class student information 
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class student information")
        class_student_frame.place(x=5,y=250,width=745, height=300)       
#StudentID

        studentId_label=Label(class_student_frame,text="StudentID:",font=("times new romain",13 ,"bold"),bg="white")
        studentId_label.grid(row=0, column=0, padx=10,pady=5, sticky=W) 

        studentID_entry=ttk.Entry(class_student_frame,width=20,font=("times new romain",13 ,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)
#student name        

        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new romain",13 ,"bold"),bg="white")
        studentName_label.grid(row=0, column=2, padx=10,pady=5, sticky=W) 

        studentname_entry=ttk.Entry(class_student_frame,width=20,font=("times new romain",13 ,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10, pady=5,sticky=W)

#class division
        class_div_label=Label(class_student_frame,text="Class division:",font=("times new romain",13 ,"bold"),bg="white")
        class_div_label.grid(row=1, column=0, padx=10,pady=5, sticky=W) 

        class_div_entry=ttk.Entry(class_student_frame,width=20,font=("times new romain",13 ,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10, pady=5,sticky=W)
#Roll no
        roll_no_label=Label(class_student_frame,text="Roll NO:",font=("times new romain",13 ,"bold"),bg="white")
        roll_no_label.grid(row=1, column=2, padx=10,pady=5, sticky=W) 

        roll_no_entry=ttk.Entry(class_student_frame,width=20,font=("times new romain",13 ,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10, pady=5,sticky=W)
#Gender        

        gender_label=Label(class_student_frame,text="Gender:",font=("times new romain",13 ,"bold"),bg="white")
        gender_label.grid(row=2, column=0, padx=10,pady=5, sticky=W) 

        gender_entry=ttk.Entry(class_student_frame,width=20,font=("times new romain",13 ,"bold"))
        gender_entry.grid(row=2,column=1,padx=10, pady=5,sticky=W)
#dob
        dob_label=Label(class_student_frame,text="DOB:",font=("times new romain",13 ,"bold"),bg="white")
        dob_label.grid(row=2, column=2, padx=10,pady=5, sticky=W) 

        dob_entry=ttk.Entry(class_student_frame,width=20,font=("times new romain",13 ,"bold"))
        dob_entry.grid(row=2,column=3,padx=10, pady=5,sticky=W)

#Email
        email_label=Label(class_student_frame,text="Email:",font=("times new romain",13 ,"bold"),bg="white")
        email_label.grid(row=3, column=0, padx=10,pady=5, sticky=W) 

        email_entry=ttk.Entry(class_student_frame,width=20,font=("times new romain",13 ,"bold"))
        email_entry.grid(row=3,column=1,padx=10, pady=5,sticky=W)

#phone no
        phone_label=Label(class_student_frame,text="Phone NO:",font=("times new romain",13 ,"bold"),bg="white")
        phone_label.grid(row=3, column=2, padx=10,pady=5, sticky=W) 

        phone_entry=ttk.Entry(class_student_frame,width=20,font=("times new romain",13 ,"bold"))
        phone_entry.grid(row=3,column=3,padx=10, pady=5,sticky=W)

#Address        

        address_label=Label(class_student_frame,text="Address:",font=("times new romain",13 ,"bold"),bg="white")
        address_label.grid(row=4, column=0, padx=10,pady=5, sticky=W) 

        address_entry=ttk.Entry(class_student_frame,width=20,font=("times new romain",13 ,"bold"))
        address_entry.grid(row=4,column=1,padx=10, pady=5,sticky=W)
#Teacher name        

        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new romain",13 ,"bold"),bg="white")
        teacher_label.grid(row=4, column=2, padx=10,pady=5, sticky=W) 

        teacher_entry=ttk.Entry(class_student_frame,width=20,font=("times new romain",13 ,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10, pady=5,sticky=W)

#radio button
        radionbtn1=ttk.Radiobutton(class_student_frame,text="Take Photo Sample",value="Yes")
        radionbtn1.grid(row=6,column=0)

        radionbtn2=ttk.Radiobutton(class_student_frame,text="No Photo Sample",value="Yes")
        radionbtn2.grid(row=6,column=1)

#buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame,text = "Save",width=17, font=("times new roman",13,"bold"),bg="blue",fg="pink")
        save_btn.grid(row=0,column=0)

        Update_btn=Button(btn_frame,text = "Update",width=17, font=("times new roman",13,"bold"),bg="blue",fg="pink")
        Update_btn.grid(row=0,column=1)

        Reset_btn=Button(btn_frame,text = "Reset",width=17, font=("times new roman",13,"bold"),bg="blue",fg="pink")
        Reset_btn.grid(row=0,column=2)

        Delete_btn=Button(btn_frame,text = "Delete",width=17, font=("times new roman",13,"bold"),bg="blue",fg="pink")
        Delete_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)

        take_photo_btn=Button(btn_frame1,text = "take photo sample",width=35, font=("times new roman",13,"bold"),bg="blue",fg="pink")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text = "Update Photo sample",width=35 , font=("times new roman",13,"bold"),bg="blue",fg="pink")
        update_photo_btn.grid(row=0,column=1)


#Right label Frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details")
        Right_frame.place(x=780,y=10,width=680, height=580)

        img_right = Image.open("college_images/gettyimages-1022573162.jpg ")
        img_right=img_right.resize((745, 130),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=745,height=130)

#Search System
        
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",13,"bold"))
        Search_frame.place(x=5,y=135,width=665,height=70)

        search_label=Label(Search_frame,text="Search BY:",font=("times new romain",13 ,"bold"),bg="brown",fg="white")
        search_label.grid(row=0, column=0, padx=10,pady=5, sticky=W) 

        search_combo=ttk.Combobox(Search_frame,font=("times new romain",14  ,"bold"),state="readonly",width=11)
        search_combo["values"]=("Select","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W) 

        search_entry=ttk.Entry(Search_frame,width=14,font=("times new romain",13 ,"bold"))
        search_entry.grid(row=0,column=2,padx=10, pady=5,sticky=W)

        search_btn=Button(Search_frame,text = "Search",width=12, font=("times new roman",12,"bold"),bg="blue",fg="pink")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(Search_frame,text = "Showall",width=11, font=("times new roman",12,"bold"),bg="blue",fg="pink")
        showAll_btn.grid(row=0,column=4,padx=4)
#Table Frame system
        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=665,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
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
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
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


        

           

        


 

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()