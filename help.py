from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lb1=Label(self.root,text="HELP DESK",font=("times new romain",35,"bold"),bg="white",fg="red")
        title_lb1.place(x=0, y=0, width=1530,height=45)

#========================Top Image ======================
        img_top = Image.open("college_images/h.jpeg")
        img_top=img_top.resize((1530, 720),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        dev_label=Label(f_lbl,text="Email:anjalijha301@gmail.com",font=("times new romain",20 ,"bold"),bg="white")
        dev_label.place(x=550,y=220)

if __name__ == "__main__":
      root=Tk()
      obj=Help(root)
      root.mainloop()        