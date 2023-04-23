from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lb1=Label(self.root,text="FACE RECOGNITION",font=("times new romain",35,"bold"),bg="white",fg="darkgreen")
        title_lb1.place(x=0, y=0, width=1530,height=45)

        #=========== 1images ===========

        img_top = Image.open("college_images/face_detector1.jpg")
        img_top=img_top.resize((650, 700),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700) 

        #==============2 images==========
        img_bottom = Image.open("college_images/detector5.jpg")
        img_bottom=img_bottom.resize((950, 700),Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)

         #================Button=============

        b1_1=Button(f_lbl,text="Face Recognition", cursor="hand2", font=("times new roman",18,"bold"),bg="darkgreen", fg="white")
        b1_1.place(x=365,y=620,width=200,height=40) 

if __name__ == "__main__":
      root=Tk()
      obj=Face_Recognition(root)
      root.mainloop()         