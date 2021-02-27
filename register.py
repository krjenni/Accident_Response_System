from tkinter import *
from tkinter import messagebox as mb
import random, string
def register():
    root = Tk()
    root.title("REGISTRATION")
    name = StringVar()
    email = StringVar()
    phone_num = StringVar()
    vehical_no = StringVar()
    em_cont1 = StringVar()
    em_cont2 = StringVar()
    em_cont3 = StringVar()
    em_cont4 = StringVar()
    em_cont5 = StringVar()
    bloodgroup=StringVar()
    medical_condition = StringVar()
    var1=IntVar()
    user_details = open("details.txt", "+a")
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    dict1 = {}
    reg_lable=Label(root, text="REGISTRATION FORM", font=("times new roman",25,"bold")).grid(row=0,column=0,columnspan=10)
    name_lable = Label(root, text="NAME", font=("times new roman", 20, "bold")).grid(row=1, column=0, padx=10, pady=10)
    name_entry = Entry(root, width=50, font=("times new roman", 20, "bold"), textvariable=name).grid(row=1, column=1,padx=10, pady=10)

    email_lable = Label(root, text="EMAIL", font=("times new roman", 20, "bold")).grid(row=2, column=0, padx=10,pady=10)
    email_entry = Entry(root, width=50, font=("times new roman", 20, "bold"), textvariable=email).grid(row=2, column=1,padx=10, pady=10)

    vehicalno_lable = Label(root, text="VEHICAL NUMBER", font=("times new roman", 20, "bold")).grid(row=3, column=0,padx=10, pady=10)
    vehicalno_entry = Entry(root, width=50, font=("times new roman", 20, "bold"), textvariable=vehical_no).grid(row=3,column=1,padx=10,pady=10)

    emcont1_lable = Label(root, text="EMERGENCY CONTACT 1", font=("times new roman", 20, "bold")).grid(row=4, column=0,padx=10, pady=10)
    emcont1_entry = Entry(root, width=50, font=("times new roman", 20, "bold"), textvariable=em_cont1).grid(row=4,column=1,padx=10,pady=10)

    emcont2_lable = Label(root, text="EMERGENCY CONTACT 2", font=("times new roman", 20, "bold")).grid(row=5, column=0,padx=10, pady=10)
    emcont2_entry = Entry(root, width=50, font=("times new roman", 20, "bold"), textvariable=em_cont2).grid(row=5,column=1,padx=10,pady=10)

    emcont3_lable = Label(root, text="EMERGENCY CONTACT 3", font=("times new roman", 20, "bold")).grid(row=6, column=0,padx=10, pady=10)
    emcont3_entry = Entry(root, width=50, font=("times new roman", 20, "bold"), textvariable=em_cont3).grid(row=6,column=1,padx=10,pady=10)

    emcont4_lable = Label(root, text="EMERGENCY CONTACT 4", font=("times new roman", 20, "bold")).grid(row=6, column=0,padx=10, pady=10)
    emcont4_entry = Entry(root, width=50, font=("times new roman", 20, "bold"), textvariable=em_cont4).grid(row=6,column=1,padx=10,pady=10)

    emcont5_lable = Label(root, text="EMERGENCY CONTACT 5", font=("times new roman", 20, "bold")).grid(row=7, column=0,padx=10, pady=10)
    emcont5_entry = Entry(root, width=50, font=("times new roman", 20, "bold"), textvariable=em_cont5).grid(row=7,column=1,padx=10,pady=10)

    medcond_lable = Label(root, text="MEDICAL CONDITION", font=("times new roman", 20, "bold")).grid(row=8, column=0,padx=10, pady=10)
    medcond_entry = Entry(root, width=50, font=("times new roman", 20, "bold"), textvariable=medical_condition).grid(row=8, column=1, padx=10, pady=10)
    dict1[name.get()] = x

    def write_():
        if name.get()=="" and email.get()=="" and vehical_no.get()=="" and em_cont1.get()=="" and em_cont2.get()=="" and em_cont3.get()=="" and em_cont4.get()=="" and em_cont5.get()=="" :
            mb.showerror("error","ALL FIELDS ARE REQUIRED")
        else : 
            user_details.write(x+" "+": " + email.get() + " " + vehical_no.get() + " " + em_cont1.get() + " " + em_cont2.get() + " " + em_cont3.get() + " " + em_cont4.get() + " " + em_cont5.get() + " " + medical_condition.get()+" "+bloodgroup.get()+"\n")
            mb.showinfo("SUCCESS", "REGISTRATION COMPLETED")
        

    bg_button=Checkbutton(root,text="DO YOU WISH TO DONATE BLOOD",font=("times new roman",20,"bold"),variable=var1).grid(row=9,column=0,sticky=W)
    if var1.get():
        bg_lable=Label(root,text="ENTER THE BLOOD GROUP",font=("times new roman", 20, "bold")).grid(row=10, column=0,padx=10, pady=10)
        bg_entry=Entry(root,width=3,font=("times new roman", 20, "bold"),textvariable=bloodgroup).grid(row=10,column=1,padx=10,pady=10)

    sub_button = Button(root, text="SUBMIT", font=("times new roman", 10, "bold"), command=write_).grid(row=11, column=8,padx=10,pady=10)
    root.mainloop()
register()