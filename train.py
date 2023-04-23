from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Train:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lb1=Label(self.root,text="TRAIN DATA SET",font=("times new romain",35,"bold"),bg="white",fg="red")
        title_lb1.place(x=0, y=0, width=1530,height=45)

#========================Top Image ======================
        img_top = Image.open("college_images/facialrecognition.png ")
        img_top=img_top.resize((1530, 325),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325) 

        #================Button=============

        b1_1=Button(self.root,text="TRAIN DATA", cursor="hand2", font=("times new roman",30,"bold"),bg="red", fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60) 

#=========================Bottom Images =================
        img_bottom = Image.open("college_images/public.jpg")
        img_bottom=img_bottom.resize((1530, 325),Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1530,height=325)        




if __name__ == "__main__":
      root=Tk()
      obj=Train(root)
      root.mainloop()        