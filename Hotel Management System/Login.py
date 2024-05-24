from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow
from tkinter import messagebox



class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
    

        
        
     
        #=================backround==========
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\HP\OneDrive\Desktop\Hotel_Management_system\hotel_images\login3.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        #====login logo==============
        img2=Image.open(r"C:\Users\HP\OneDrive\Desktop\Hotel_Management_system\hotel_images\main.jpg")
        img2=img2.resize((140,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img2)
        
        lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),bg="black",fg="white")
        get_str.place(x=95,y=100)

        #========label========

        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),bg="black",fg="white")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="black",fg="white")
        password.place(x=70,y=225)

        self.txtpass =ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass .place(x=40,y=250,width=270)
        
        #===========icon img===========
        img2=Image.open(r"C:\Users\HP\OneDrive\Desktop\Hotel_Management_system\hotel_images\log.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg1=Label(image=self.photoimg2,bg="black",borderwidth=0)
        lblimg1.place(x=640,y=323,width=25,height=25)

        img3=Image.open(r"C:\Users\HP\OneDrive\Desktop\Hotel_Management_system\hotel_images\pass2.jpg")
        img3=img3.resize((30,30),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lblimg1=Label(image=self.photoimg3,bg="black",borderwidth=0)
        lblimg1.place(x=640,y=395,width=25,height=25)

        #=======login btn=======
        login_btn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,bg="red",fg="white")
        login_btn.place(x=110,y=300,width=120,height=35)

        #=========register btn======
        reg_btn=Button(frame,text="New User Register",font=("times new roman",12,"bold"),bd=3,borderwidth=0,bg="black",fg="white")
        reg_btn.place(x=90,y=350,width=160)
        #===========forget pass btn=========
        forget_btn=Button(frame,text="Forget Password",font=("times new roman",12,"bold"),borderwidth=0,bg="black",fg="white")
        forget_btn.place(x=90,y=380,width=160)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields required")
        elif self.txtuser.get()=="vishwa" or self.txtpass.get()=="9909":
            messagebox.showinfo("Success","Welcome to Hotel Mangaement Systeam ")
        else:
            messagebox.showerror("Error","Invaild Username and Password")    





if __name__ == '__main__':
    root=Tk()
    obj=Login_Window(root)
    root.mainloop()
