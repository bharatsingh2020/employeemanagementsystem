from multiprocessing import Manager
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Employee Management System')
        lbl_title=Label(self.root,text="EMPLOYEE MANAGEMENT SYSTEM",
        font=('times new roman',37,'bold'),fg='darkblue',bg='white')
        lbl_title.place(x=0,y=0,width=1530,height=50)

        img_logo=Image.open("college images/emplogo.png")
        img_logo=img_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=270,y=0,width=50,height=50)

        #Image Frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1530,height=160)
        
        #1st image
        img1=Image.open("college images/emp5.jpg")
        img1=img1.resize((540,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)
        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0, y=0)


        #2nd image
        img_2=Image.open("college images/emp2.png")
        img_2=img_2.resize((540,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img_2)
        self.img_2= Label(img_frame,image=self.photo2)
        self.img_2.place(x=540, y=0)

        #3rd image
        img_3=Image.open("college images/emp3.png")
        img_3=img_3.resize((540,160), Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img_3)
        self.img_3=Label(self.root, image=self.photo3)
        self.img_3.place(x=1050, y=50)

        # Main Frame
        Main_frame=Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Main_frame.place(x=10,y=210,width=1500,height=560)

        # Upper Frame
        upper_frame=LabelFrame(Main_frame,bd=2, relief=RIDGE, 
        bg="white",text="Employee Information",font=('times new roman',11,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1480,height=270)


        # Labels and entry
 
        lbl_dep=Label(upper_frame,text='Department',font=('arial',11,'bold'),fg='black')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(upper_frame,font=('arial',12,'bold'),width=17,state='readonly' )
        combo_dep['value']=('Select Department','HR','Software Engineer','Manager')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        #Name
        lbl_name=Label(upper_frame,font=('arial', 12,'bold'),text="Name:",bg="white")
        lbl_name.grid(row=0, column=2,sticky=W, padx=2,pady=7)
 
        txt_name=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_name.grid(row=0,column=3,padx=2,pady=7)
        #Email
        lbl_email= Label(upper_frame, font=('arial', 12, 'bold'), 
        text='Email:', bg='white')
        lbl_email.grid(row=1, column=2, padx=2, pady=7, sticky=W)
        txt_email= ttk.Entry(upper_frame, width=22, font=('arial', 11, 'bold'))
        txt_email.grid(row=1, column=3,padx=2, pady=7)  
         #address
        lbl_address= Label(upper_frame, font=('arial', 12, 'bold'), 
        text='Address:', bg='white')
        lbl_address.grid(row=2, column=0, padx=2, pady=7, sticky=W)
        txt_address = ttk.Entry(upper_frame, width=22, font=('arial', 11, 'bold'))
        txt_address.grid(row=2, column=1, padx=2, pady=7,sticky=W) 

         #married
        lbl_married_status= Label(upper_frame, font=('arial', 12, 'bold'), 
        text='Married Status', bg='white')
        lbl_married_status.grid(row=2, column=2, padx=2, pady=7, sticky=W)
        combo_txt_married=ttk.Combobox(upper_frame,state='readonly', font=('arial', 12, 'bold'), width=18 )
        combo_txt_married['value'] = ("Married","Unmarried","Single")
        combo_txt_married.current(0)
        combo_txt_married.grid(row=2, column=3, padx=2, pady=7, sticky=W)

         #DOB
        lbl_dob= Label(upper_frame, font=('arial', 12, 'bold'), 
        text='DOB:', bg='white')
        lbl_dob.grid(row=3, column=0, padx=2, pady=7, sticky=W)
        txt_dob= ttk.Entry(upper_frame, width=22, font=('arial', 11, 'bold'))
        txt_dob.grid(row=3, column=1, padx=2, pady=7)
        
         # DOJ
        lbl_doj = Label(upper_frame, font=('arial', 12, 'bold'), 
        text='DOJ:', bg='white')
        lbl_doj.grid(row=3, column=2, padx=2, pady=7, sticky=W)
        txt_doj = ttk.Entry(upper_frame, width=22, font=('arial', 11, 'bold'))
        txt_doj.grid(row=3, column=3, padx=2, pady=7)

         #ID proof
 
        com_txt_proof=ttk.Combobox(upper_frame,state="readonly",font=('arial', 12, 'bold'),width=17)
        com_txt_proof['value']=("Select ID Proof","PAN CARD","ADHAR CARD","DRIVING LICENCE")
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4,column=1,sticky=W,padx=2,pady=7)
        txt_proof= ttk.Entry(upper_frame, font=('arial', 12, 'bold'))
        txt_proof.grid(row=4, column=1, padx=2, pady=7)
        

         #gender
        lbl_gender= Label(upper_frame, font=('arial', 12, 'bold'), 
        text="Gender:", bg='white')
        lbl_gender.grid(row=4, column=2, padx=2, pady=7, sticky=W)
        com_txt_gender = ttk.Combobox(upper_frame, state="readonly", 
        font=('arial', 12, 'bold'), width=17)
        com_txt_gender['value'] = ("Male","Female","Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4, column=3, sticky=W, padx=2, pady=7)

         #phone no
        lbl_phone= Label(upper_frame, font=('arial', 12, 'bold'), 
        text='Phone No:', bg='white')
        lbl_phone.grid(row=0, column=4, padx=2, pady=7, sticky=W)
        txt_phone= ttk.Entry(upper_frame,width=22, font=('arial', 11, 'bold'))
        txt_phone.grid(row=0, column=5, padx=2, pady=7)

         #country
        lbl_country= Label(upper_frame, font=('arial', 12, 'bold'), 
        text='Country:', bg='white')
        lbl_country.grid(row=1, column=4, padx=2, pady=7, sticky=W)
        txt_country = ttk.Entry(upper_frame, width=22, font=('arial', 11, 'bold'))
        txt_country.grid(row=1, column=5, padx=2, pady=7)

         #CTC
        lbl_ctc= Label(upper_frame, font=('arial', 12, 'bold'), 
        text='Salary(CTC):', bg='white')
        lbl_ctc.grid(row=2, column=4, padx=2, pady=7, sticky=W)
        txt_ctc= ttk.Entry(upper_frame, width=22, font=('arial', 11, 'bold'))
        txt_ctc.grid(row=2, column=5, padx=2, pady=7)

         #mask image
        img_mask=Image.open("college images/emp4.jpg")
        img_mask=img_mask.resize((220,220),Image.ANTIALIAS)
        self.photomask=ImageTk.PhotoImage(img_mask)
        self.img_mask= Label(upper_frame,image=self.photomask)
        self.img_mask.place(x=1000, y=0,width=220,height=220)

          # Down Frame
        down_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg="white", 
        text="Employee Table Information",font=('times new roman', 11, 
        'bold'),fg='blue')
        down_frame.place(x=10,y=280,width=1480,height=270)



if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()        