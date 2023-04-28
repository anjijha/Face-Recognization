from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        self.root.state("zoomed")

        title_lb1=Label(self.root,text="DEVELOPER",font=("times new romain",35,"bold"),bg="dark violet",fg="white")
        title_lb1.place(x=0, y=0, width=1540,height=45)

#========================Top Image ======================
        img_top = Image.open("college_images/dev.jpg")
        img_top=img_top.resize((1540, 750),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1540,height=750)
#Frame.
        main_frame = Frame(f_lbl, bd =2,bg="white")
        main_frame.place(x=1000,y=0,width=540,height=750) 

        # img_top1 = Image.open("college_images/kiran.jpg ")
        # img_top1=img_top1.resize((200, 200),Image.Resampling.LANCZOS)
        # self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        # f_lbl=Label(main_frame,image=self.photoimg_top1)
        # f_lbl.place(x=300,y=0,width=200,height=200) 

 #Developer info       
        dev_label=Label(main_frame,text="Hello my name ,Anjali",font=("times new romain",20 ,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="I am full stack developer",font=("times new romain",20 ,"bold"),bg="white")
        dev_label.place(x=0,y=40)

        img2 = Image.open("college_images/devlp.jpg ")
        img2=img2.resize((500, 390),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=330,y=0,width=200,height=200) 



if __name__ == "__main__":
      root=Tk()
      obj=Developer(root)
      root.mainloop()        