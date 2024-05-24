from logging import exception
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox



class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management system")
        self.root.geometry("1295x560+230+220")


        #================title=================
        lbl_title=Label(self.root,text="ROOMBOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #==================logo===============
        img2=Image.open(r"C:\Users\HP\OneDrive\Desktop\Hotel_Management_system\hotel_images\logohotel1.png")
        img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)


        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        #===============Lebal frame==============
        lebal_frame_left=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("times new roman",12,"bold"),padx=2,)
        lebal_frame_left.place(x=5,y=50,width=540,height=350)

        #========== Floor ===========
        lbl_floor=Label(lebal_frame_left,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W,padx=20)

        self.var_floor=StringVar()
        entry_floor=ttk.Entry(lebal_frame_left,textvariable=self.var_floor,font=("arial",13,"bold"),width=20,)
        entry_floor.grid(row=0,column=1,sticky=W)

        #========== Room No ===========
        lbl_Room_no=Label(lebal_frame_left,text="Room No",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Room_no.grid(row=1,column=0,sticky=W,padx=20)

        self.var_room_no=StringVar()
        entry_Room_no=ttk.Entry(lebal_frame_left,textvariable=self.var_room_no,font=("arial",13,"bold"),width=20,)
        entry_Room_no.grid(row=1,column=1,sticky=W)

        
        #========== Room Type ===========
        lbl_Room_Type=Label(lebal_frame_left,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Room_Type.grid(row=2,column=0,sticky=W,padx=20)

        self.var_room_type=StringVar()
        entry_Room_Type=ttk.Entry(lebal_frame_left,textvariable=self.var_room_type,font=("arial",13,"bold"),width=20,)
        entry_Room_Type.grid(row=2,column=1,sticky=W)

        #============button======
        btn_frame=Frame(lebal_frame_left,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=432,height=40)


        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        
        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        
        btndelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btndelete.grid(row=0,column=2,padx=1)

        
        btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnreset.grid(row=0,column=3,padx=1)

        #====================Tabel frame serch systeam ===================
        table_frame_left=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details ",font=("times new roman",12,"bold"),padx=2,)
        table_frame_left.place(x=600,y=55,width=600,height=350)

        scroll_x=ttk.Scrollbar(table_frame_left,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame_left,orient=VERTICAL)
        self.room_table=ttk.Treeview(table_frame_left,columns=("floor","roomno","roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room No")
        self.room_table.heading("roomtype",text="Room Type")
       


        self.room_table["show"]="headings"

        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomtype",width=100)

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    
    #================Add  data=================

    def add_data(self):
            if self.var_floor.get()=="" or self.var_room_type.get()=="":
                messagebox.showerror("Error","All field are requaied",parent=self.root)
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Admin@123",database="management")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                                self.var_floor.get(),
                                                                                self.var_room_no.get(),
                                                                                self.var_room_type.get()
                                                                                
                                                                                
                                                                                                                ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()                                                            
                    messagebox.showinfo("success","New Room Added Successfully",parent=self.root)
                except Exception as es:
                    messagebox.showwarning("Waring",f"some thing went wrong:{str(es)}",parent=self.root)        

           
    #================fetch data=================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Admin@123",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
                conn.commit()
        conn.close()

    #===================get cursor===================
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_floor.set(row[0])
        self.var_room_no.set(row[1])
        self.var_room_type.set(row[2])
        

    #upadate function
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","plese enter the Floor number",parent=self.root) 
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Admin@123",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(
                                                                                                                                                                       
                                                                                                                                        
                                                                                                self.var_floor.get(),
                                                                                                self.var_room_type.get(),
                                                                                                self.var_room_no.get(),
                                                                                                                                         
                                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","New Room has been update successfully",parent=self.root)    

    #=============delete function===================== 
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want delete this room",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Admin@123",database="management")
            my_cursor=conn.cursor()
            qurey="delete from details where RoomNo=%s"
            value=(self.var_room_no.get(),)
            my_cursor.execute(qurey,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()    

    #===================reset==================
    def reset(self):
        self.var_floor.set("")
        self.var_room_no.set("")
        self.var_room_type.set("")


if __name__ == '__main__':
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()