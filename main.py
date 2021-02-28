import numpy as np
import pickle

def accident() :
	import random
	temp = random.uniform(66,100)
	hum = random.uniform(0,100)
	pes = random.uniform(25.69,31.15)
	vis = random.uniform(0,140)
	wd = random.randint(0,8)
	ws = random.uniform(0,256)
	wc = random.randint(0,126)
	m = random.randint(1,12)
	d = random.randint(1,31)
	h = random.randint(0,23)
	min = random.randint(0,59)
	weekday = random.randint(0,6)
	lat = random.uniform(15,30)
	long = random.uniform(60,90)
	X = [[temp,hum,pes,vis,wd,ws,wc,m,d,h,min,weekday]]
	X = np.array(X)
	#X.reshape(1, 1, 12)
	
	loaded_model = pickle.load(open('rf.sav', 'rb'))
	severity = loaded_model.predict(X)
	print(severity)
	
	newWindow = Toplevel(f)
	
	newWindow.geometry("1650x1650")
	fontStyle3 = Font(family="Lucida Grande", size=35)
	fontStyle4 = Font(family="Lucida Grande", size=25)
	fontStyle5 = Font(family="Lucida Grande", size=45)
	fontStyle6 = Font(family="Lucida Grande", size=25)
	l1 = Label(newWindow,text = "Accident has Happened",font = fontStyle3).pack()
	l2 = Label(newWindow,text = "temperature : ",font = fontStyle4).place(x = 200,y =150)
	l14 = Label(newWindow,text = temp,font = fontStyle4).place(x = 500,y = 150)
	l3 = Label(newWindow,text = "humidity : ",font = fontStyle4).place(x = 200, y=200)
	l15 = Label(newWindow,text = hum,font = fontStyle4).place(x = 500, y= 200)
	l4 = Label(newWindow,text = "pressure : ",font = fontStyle4).place(x = 200,y=250)
	l16 = Label(newWindow,text = pes,font = fontStyle4).place(x = 500,y = 250)
	l5 = Label(newWindow,text = "Visibility : ",font = fontStyle4).place(x = 200,y = 300)
	l17 = Label(newWindow,text = vis,font = fontStyle4).place(x = 500, y= 300)
	l6 = Label(newWindow,text = "Wind direction : ",font = fontStyle4).place(x = 200,y = 350)
	l18 = Label(newWindow,text = wd,font = fontStyle4).place(x = 500,y = 350)
	l7 = Label(newWindow,text = "Weather condition : ",font = fontStyle4).place(x = 200,y = 400)
	l19 = Label(newWindow,text = wc,font = fontStyle4).place(x = 500,y= 400)
	l8 = Label(newWindow,text = "Month : ",font = fontStyle4).place(x = 200, y =450)
	l20 = Label(newWindow,text = m,font = fontStyle4).place(x = 500, y =450)
	l9 = Label(newWindow,text = "Day : ",font = fontStyle4).place(x = 200, y= 500)
	l21 = Label(newWindow,text = d,font = fontStyle4).place(x = 500, y = 500)
	l10 = Label(newWindow,text = "Hour : ",font = fontStyle4).place(x = 200, y =550)
	l22 = Label(newWindow,text = h,font = fontStyle4).place(x = 500,y =550)
	l13 = Label(newWindow,text = "minute : ",font = fontStyle4).place(x = 200,y = 600)
	l12 = Label(newWindow,text = min,font = fontStyle4).place(x = 500,y = 600)
	l13 = Label(newWindow,text = "Weekday :",font = fontStyle4).place(x = 200, y=650)
	l13 = Label(newWindow,text = weekday,font = fontStyle4).place(x = 500,y=650)
	if severity>2:
		nw2 = Toplevel(newWindow)
		nw2.geometry("500x500")
		ls1 = Label(nw2,text = "Severity is :",font = fontStyle5,fg = "red").place(x = 10,y=10)
		ls = Label(nw2,text = severity[0],font = fontStyle5, fg = "red").place(x =350,y =10)
		ls2 = Label(nw2,text = "Severity is on a higher scale",font = fontStyle5,fg = "red").place(x = 10, y =150)
		if lat<20 and long<75:
			ls3 = Label(nw2,text = "Alert message has been sent to control room 1 and emergency contact numbers",font = fontStyle6,fg = "red").place(x = 10,y =300)
			t = open("details.txt","r")
			x= open("alert.txt","+a")
			t2 = t.readlines()
			t2 = str(t2)
			t2 = t2.split(' ')
			t.close()
			
			for i in range(4,8):
				print("Alert message has been sent to :",t2[i],file = x)
			x.close()

		else:
			ls4 = Label(nw2,text = "Alert message has been sent to control room 2 and emergency contact numbers",font = fontStyle6,fg = "red").place(x = 10,y =300)
			t = open("details.txt","r")
			x = open("alert.txt","+a")
			t2 = t.readlines()
			t2 = str(t2)
			t2 = t2.split(' ')
			t.close()
			
			for i in range(4,8):
				print("Alert message has been sent to :",t2[i],file = x)
			x.close()
			
	else :
		nw3 = Toplevel(newWindow)
		nw3.geometry("500x500")
		ls1 = Label(nw3,text = "Severity is :",font = fontStyle5,fg = "blue").place(x = 10,y=10)
		ls = Label(nw3,text = severity[0],font = fontStyle5, fg = "blue").place(x =350,y =10)
		ls2 = Label(nw3,text = "Severity is on a lower scale",font = fontStyle5,fg = "blue").place(x = 10, y =150)
		if lat<20 and long<75:
			ls3 = Label(nw3,text = "Alert message has been sent to control room 1",font = fontStyle6,fg = "red").place(x = 10,y =300)
		else:
			ls4 = Label(nw3,text = "Alert message has been sent to control room 2",font = fontStyle6,fg = "red").place(x = 10,y =300)
			
		
		
	
 


from tkinter import *
from tkinter.font import *
from tkinter import messagebox
f = Tk()
f.geometry("1650x1650")
use_var = StringVar()
pas_var = StringVar()
def book2():
	u = use_var.get()
	p = pas_var.get()
	t = open("details.txt","r")
	t2 = t.readlines()
	t.close()
	
	if u in str(t2) and p in str(t2):
		nw = Toplevel(f)
		nw.geometry("1650x1650")
		fontStyle2 = Font(family="Lucida Grande", size=55)
		fontStyle3 = Font(family="Lucida Grande", size=35)
		l = Label(nw,text = "Accident Response System",font = fontStyle2).pack()
		b = Button(nw,text = "Accident",font = fontStyle3,command = accident).pack()
	else:
		messagebox.showerror(title = "Error", message = "Invalid username or password")


fontStyle3 = Font(family="Lucida Grande", size=30)
Label(f,text ="Please Fill in the login credentials",font = fontStyle3).pack()
		
L1 = Label(f, text="User Name",font = fontStyle3).place(x=620,y=200)
e1 = Entry(f,textvariable = use_var,font = fontStyle3).place(x=900,y=200)
L2 = Label(f, text="Password : ",font = fontStyle3).place(x=620,y=450)
e2 = Entry(f,textvariable = pas_var,font = fontStyle3,show = "*").place(x = 900,y =450)
b4 = Button(f,text = "submit",font = fontStyle3, command = book2).place(x =750,y=600)
		




f.mainloop()







