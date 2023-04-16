from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Face_Recognition_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

#first image
        img = Image.open("college_images/Stanford.jpg ")
        img=img.resize((500, 130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
#second image
        img1 = Image.open("college_images/facialrecognition.png ")
        img1=img1.resize((500, 130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130) 
#third image
        img2 = Image.open("college_images/u.jpg ")
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

        title_lb1=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SOFTWARE",font=("times new romain",35,"bold"),bg="white",fg="red")
        title_lb1.place(x=0, y=0, width=1530,height=45)
#Student button
        img4 = Image.open("college_images/gettyimages-1022573162.jpg ")
        img4=img4.resize((220, 220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(self.root,image=self.photoimg4, cursor="hand2")
        b1.place(x=250,y=220,width=220,height=220) 

        b1_1=Button(bg_img,text="Student Details", cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=248,y=307,width=220,height=40) 

#Detect face button        
        img5 = Image.open("college_images/face_detector1.jpg ")
        img5=img5.resize((220, 220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(self.root,image=self.photoimg5, cursor="hand2")

        b1.place(x=490,y=220,width=220,height=220) 
        

        b1_1=Button(bg_img,text="Face Detector", cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=490,y=307,width=215,height=40) 

#Attendance face button      

        img6 = Image.open("college_images/report.jpg ")
        img6=img6.resize((220, 220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(self.root,image=self.photoimg6, cursor="hand2")

        b1.place(x=750,y=220,width=220,height=220) 
        

        b1_1=Button(bg_img,text="ATTENDANCE", cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=750,y=307,width=215,height=40)
    
#Help face button        

        img7 = Image.open("college_images/help.jpg ")
        img7=img7.resize((220, 220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(self.root,image=self.photoimg7, cursor="hand2")

        b1.place(x=1000,y=220,width=220,height=220) 
        

        b1_1=Button(bg_img,text="HELP DESK", cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=1000,y=307,width=215,height=40)

 #train data       
        img8 = Image.open("college_images/Train.jpg ")
        img8=img8.resize((220, 220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(self.root,image=self.photoimg8, cursor="hand2")

        b1.place(x=250,y=500,width=220,height=220) 
        

        b1_1=Button(bg_img,text="TRAIN DATA", cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=250,y=580,width=215,height=40)

 #photo data       
        img9 = Image.open("college_images/public.jpg ")
        img9=img9.resize((220, 220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(self.root,image=self.photoimg9, cursor="hand2")

        b1.place(x=500,y=500,width=220,height=220) 
        

        b1_1=Button(bg_img,text="PHOTOS", cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=500,y=580,width=215,height=40)
 #DEVELOPER       

        img10 = Image.open("college_images/developer.jpg ")
        img10=img10.resize((220, 220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(self.root,image=self.photoimg10, cursor="hand2")

        b1.place(x=750,y=500,width=220,height=220) 
        

        b1_1=Button(bg_img,text="DEVELOPER", cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=750,y=580,width=215,height=40)
 
 #exit       
        img11 = Image.open("college_images/exit.jpg ")
        img11=img11.resize((220, 220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(self.root,image=self.photoimg11, cursor="hand2")

        b1.place(x=1000,y=500,width=220,height=220) 
        

        b1_1=Button(bg_img,text="EXIT", cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=1000,y=580,width=215,height=40)








if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

        
 