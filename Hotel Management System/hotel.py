from tkinter import*
from PIL import Image,ImageTk  #pip install pillow
from customer import cust_win
from room import Roombooking
from details import DetailsRoom


class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management system")
        self.root.geometry("1900x800+0+0")

        #============ist img ==============
        img1=Image.open(r"C:\Users\HP\OneDrive\Desktop\Hotel_Management_system\hotel_images\hotel2.jpg")
        img1.resize((1900,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)


        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1900,height=140)

        #===============logo================
        img2=Image.open(r"C:\Users\HP\OneDrive\Desktop\Hotel_Management_system\hotel_images\logohotel1.png")
        img2.resize((300,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)


        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=300,height=140)

        #============title=============
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        #===========main frame==========
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=800)

        #============menu==============
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=260)

        #===========btn frame==========
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=258,height=180)    

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0)

        room_btn=Button(btn_frame,text="ROOM",width=22,command=self.roombooking,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0)

        details_btn=Button(btn_frame,text="DETAILS",width=22,command=self.DetailsRoom,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0)

        report_btn=Button(btn_frame,text="REPORT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0)

        logout_btn=Button(btn_frame,text="LOGOUT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0)

        #================== right side image=============
        img3=Image.open(r"C:\Users\HP\OneDrive\Desktop\Hotel_Management_system\hotel_images\my.jpg")
        img3.resize((1310,610),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=225,y=0,width=1310,height=610)

        #==================down img============

        img4=Image.open(r"C:\Users\HP\OneDrive\Desktop\Hotel_Management_system\hotel_images\mys.jpg")
        img4.resize((230,210),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=225,width=230,height=210)

        img5=Image.open(r"C:\Users\HP\OneDrive\Desktop\Hotel_Management_system\hotel_images\khana.jpg")
        img5.resize((230,190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=420,width=230,height=190)


    def cust_details(self):
        self.new_window=Toplevel(self.root)  
        self.app=cust_win(self.new_window)  
        

    def roombooking(self):
        self.new_window=Toplevel(self.root)  
        self.app=Roombooking(self.new_window) 
         

    def DetailsRoom(self):
        self.new_window=Toplevel(self.root)  
        self.app=DetailsRoom(self.new_window)
        

    
        

if __name__ == '__main__':
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()
