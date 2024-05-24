from logging import exception
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk 
import random
import mysql.connector
from tkinter import messagebox



class cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management system")
        self.root.geometry("1295x560+230+220")

        #==================Veriables===============

        self.Var_ref=StringVar()
        v=random.randint(1000,9999)
        self.Var_ref.set(str(v))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_ref=StringVar()
        self.var_mobile=StringVar()
        self.var_post=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        self.var_address=StringVar()

        #===================title=============
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #==================logo==============
        img2=Image.open(r"C:\Users\HP\OneDrive\Desktop\Hotel_Management_system\hotel_images\logohotel1.png")
        img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)


        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        #===============Lebal frame==============
        lebal_frame_left=LabelFrame(self.root,bd=2,relief=RIDGE,text="CUSTOMER DETAILS",font=("times new roman",12,"bold"),padx=2,)
        lebal_frame_left.place(x=5,y=50,width=450,height=490)

        #==============Lebal and entry=============

        #cust ref
        lbl_cust_ref=Label(lebal_frame_left,text="Customer Ref:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(lebal_frame_left,textvariable=self.Var_ref,font=("arial",13,"bold"),width=29,state="readonly")
        entry_ref.grid(row=0,column=1)
        # cust name

        cname=Label(lebal_frame_left,text="Customer Name:",font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)

        txtcname=ttk.Entry(lebal_frame_left,textvariable=self.var_cust_name,font=("arial",13,"bold"),width=29)
        txtcname.grid(row=1,column=1)

        #mother name

        lblmname=Label(lebal_frame_left,text="Mother Name:",font=("arial",12,"bold"),padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)

        txtmname=ttk.Entry(lebal_frame_left,textvariable=self.var_mother,font=("arial",13,"bold"),width=29)
        txtmname.grid(row=2,column=1)

        #gender combobox
        lbl_gender=Label(lebal_frame_left,text="Gender:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(lebal_frame_left,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("MALE","FEMALE","OTHER")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)



        #post code
        lblpostcode=Label(lebal_frame_left,text="Post Code:",font=("arial",12,"bold"),padx=2,pady=6)
        lblpostcode.grid(row=4,column=0,sticky=W)

        txtpostcode=ttk.Entry(lebal_frame_left,textvariable=self.var_post,font=("arial",13,"bold"),width=29)
        txtpostcode.grid(row=4,column=1)

        #mobile number
        lblmobile=Label(lebal_frame_left,text="Mobile Number:",font=("arial",12,"bold"),padx=2,pady=5)
        lblmobile.grid(row=5,column=0,sticky=W)

        txtmobile=ttk.Entry(lebal_frame_left,textvariable=self.var_mobile,font=("arial",13,"bold"),width=29)
        txtmobile.grid(row=5,column=1)

        #Email
        lblemail=Label(lebal_frame_left,text="Email Id:",font=("arial",12,"bold"),padx=2,pady=6)
        lblemail.grid(row=6,column=0,sticky=W)

        txtemail=ttk.Entry(lebal_frame_left,textvariable=self.var_email,font=("arial",13,"bold"),width=29)
        txtemail.grid(row=6,column=1)


        #nationality
        lbl_nationality=Label(lebal_frame_left,text="Nationality:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_nationality.grid(row=7,column=0,sticky=W)
        combo_nationality=ttk.Combobox(lebal_frame_left,textvariable=self.var_nationality,font=("arial",12,"bold"),width=27,state="readonly")
        combo_nationality["value"]=("INDIA","AMERICA","SPAIN")
        combo_nationality.current(0)
        combo_nationality.grid(row=7,column=1)





        #Id type combobox
        lblidtype=Label(lebal_frame_left,text="Id Proof Type:",font=("arial",12,"bold"),padx=2,pady=6)
        lblidtype.grid(row=8,column=0,sticky=W)
        combo_id=ttk.Combobox(lebal_frame_left,textvariable=self.var_id_proof,font=("arial",12,"bold"),width=27,state="readonly")
        combo_id["value"]=("ADHAR CARD","DRIVING LICENCE","PASSPORT")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)
      




        #ID number 
        lblidnumber=Label(lebal_frame_left,text="Id Number:",font=("arial",12,"bold"),padx=2,pady=6)
        lblidnumber.grid(row=9,column=0,sticky=W)

        txtidnumber=ttk.Entry(lebal_frame_left,textvariable=self.var_id_number,font=("arial",13,"bold"),width=29)
        txtidnumber.grid(row=9,column=1)


        #Address
        lbladdress=Label(lebal_frame_left,text="Address:",font=("arial",12,"bold"),padx=2,pady=6)
        lbladdress.grid(row=10,column=0,sticky=W)

        txtaddress=ttk.Entry(lebal_frame_left,textvariable=self.var_address,font=("arial",13,"bold"),width=29)
        txtaddress.grid(row=10,column=1)


        #============button======
        btn_frame=Frame(lebal_frame_left,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=432,height=40)


        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        
        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        
        btndelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btndelete.grid(row=0,column=2,padx=1)

        
        btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnreset.grid(row=0,column=3,padx=1)

        #====================Tabel frame===================
        table_frame_left=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search Systeam ",font=("times new roman",12,"bold"),padx=2,)
        table_frame_left.place(x=435,y=50,width=860,height=490)

        lblSearchBy=Label(table_frame_left,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)



        self.serch_var=StringVar()
        combo_Search=ttk.Combobox(table_frame_left,textvariable=self.serch_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("Mobile","Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)
      
        self.txt_serch=StringVar()
        txtSearch=ttk.Entry(table_frame_left,textvariable=self.txt_serch,font=("arial",13,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        
        btnSearch=Button(table_frame_left,text="Search",command=self.Serch,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        
        btnShowAll=Button(table_frame_left,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

        #=============Show data table=============

        Details_tebal=Frame(table_frame_left,bd=2,relief=RIDGE)
        Details_tebal.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(Details_tebal,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Details_tebal,orient=VERTICAL)

        self.Cust_Details_Tebal=ttk.Treeview(Details_tebal,columns=("Ref","Name","Mother","Gender","Post","Mobile","Email","Nationality","Id_Number","Id_Proof","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Tebal.xview)
        scroll_y.config(command=self.Cust_Details_Tebal.yview)

        self.Cust_Details_Tebal.heading("Ref",text="Refer No")
        self.Cust_Details_Tebal.heading("Name",text="Name")
        self.Cust_Details_Tebal.heading("Mother",text="Mother Name ")
        self.Cust_Details_Tebal.heading("Gender",text="Gender")
        self.Cust_Details_Tebal.heading("Post",text="Post Code")
        self.Cust_Details_Tebal.heading("Mobile",text="Mobile")
        self.Cust_Details_Tebal.heading("Email",text="Email")
        self.Cust_Details_Tebal.heading("Nationality",text="Nationality")
        self.Cust_Details_Tebal.heading("Id_Proof",text="Id_Proof")
        self.Cust_Details_Tebal.heading("Id_Number",text="Id_Number")
        self.Cust_Details_Tebal.heading("Address",text="Address")

        self.Cust_Details_Tebal["show"]="headings"

        self.Cust_Details_Tebal.column("Ref",width=100)
        self.Cust_Details_Tebal.column("Name",width=100)
        self.Cust_Details_Tebal.column("Mother",width=100)
        self.Cust_Details_Tebal.column("Gender",width=100)
        self.Cust_Details_Tebal.column("Post",width=100)
        self.Cust_Details_Tebal.column("Mobile",width=100)
        self.Cust_Details_Tebal.column("Email",width=100)
        self.Cust_Details_Tebal.column("Nationality",width=100)
        self.Cust_Details_Tebal.column("Id_Proof",width=100)
        self.Cust_Details_Tebal.column("Id_Number",width=100)
        self.Cust_Details_Tebal.column("Address",width=100)


        self.Cust_Details_Tebal.pack(fill=BOTH,expand=1)
        self.Cust_Details_Tebal.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    
    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
         
           messagebox.showerror("Error","All field are requaied",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Admin@123",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.Var_ref.get(),
                                                                                self.var_cust_name.get(),
                                                                                self.var_mother.get(),
                                                                                self.var_gender.get(),
                                                                                self.var_post.get(),
                                                                                
                                                                                self.var_mobile.get(),
                                                                                self.var_email.get(),
                                                                                self.var_nationality.get(),
                                                                                self.var_id_proof.get(),
                                                                                self.var_id_number.get(),
                                                                                self.var_address.get()
                                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()                                                            
                messagebox.showinfo("success","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Waring",f"some thing went wrong:{str(es)}",parent=self.root)    

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Admin@123",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Tebal.delete(*self.Cust_Details_Tebal.get_children())
            for i in rows:
                self.Cust_Details_Tebal.insert("",END,values=i)
                conn.commit()
        conn.close()
    
    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Tebal.focus()
        content=self.Cust_Details_Tebal.item(cursor_row)
        row=content["values"]

        self.Var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want delete this customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Admin@123",database="management")
            my_cursor=conn.cursor()
            qurey="delete from customer where Ref=%s"
            value=(self.Var_ref.get(),)
            my_cursor.execute(qurey,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()            

    def reset(self):
       # self.Var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")

        v=random.randint(1000,9999)
        self.Var_ref.set(str(v))
                                                                                                                                                   
    def Serch(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Admin@123",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer where "+str(self.serch_var.get())+"  LIKE '%"+str(self.txt_serch.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.Cust_Details_Tebal.delete(*self.Cust_Details_Tebal.get_children())
            for i in rows:
                self.Cust_Details_Tebal.insert("",END,values=i)
            conn.commit()
        conn.close()       

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","plese enter the mobile number",parent=self.root) 
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Admin@123",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where ref=%s",(
                                                                                                                                                                       
                                                                                                                                                                        self.var_cust_name.get(),
                                                                                                                                                                        self.var_mother.get(),
                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                        self.var_post.get(),
                                                                                                                                                                            
                                                                                                                                                                        self.var_mobile.get(),
                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                        self.var_nationality.get(),
                                                                                                                                                                        self.var_id_proof.get(),
                                                                                                                                                                        self.var_id_number.get(),
                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                        self.Var_ref.get()
                                                                                                                                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","customer has been update successfully",parent=self.root)



if __name__ == '__main__':
    root=Tk()
    obj=cust_win(root)
    root.mainloop()