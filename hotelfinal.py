import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="hashamsql",
    database="rdbms"
    )
print(mydb)

mycursor=mydb.cursor()

#mycursor.execute("create table hotel03 (hotel_name VARCHAR(20),hotel_id varchar(20),location varchar(20),owner_name VARCHAR(30),contact VARCHAR(25))")

#mycursor.execute("create table customer03 (customer_name VARCHAR(20),customer_id varchar(20),contact varchar(20),email VARCHAR(30),cnic VARCHAR(25),primary key(customer_id))")

#mycursor.execute("create table employee04 (employee_name VARCHAR(20),employee_id varchar(20),contact varchar(20),email VARCHAR(30),salary int,primary key(employee_id))")

#mycursor.execute("create table room03 (room_id VARCHAR(20),no_of_bed int,room_description varchar(30),room_category VARCHAR(30),floor int,primary key(room_id))")

#mycursor.execute("create table booking03 (booking_id VARCHAR(20),booking_date date,booked_by varchar(20),description VARCHAR(30),booking_type VARCHAR(25),primary key(booking_id))")

#mycursor.execute("create table payment03 (payment_id VARCHAR(20),payment_date date,amount int,paid_by VARCHAR(30),description VARCHAR(25),primary key(payment_id))")


mycursor=mydb.cursor()

from tkinter import *
from PIL import ImageTk,Image
from time import *
import tkinter.font as font
import matplotlib.pyplot as plt
import numpy as np

root=Tk()
current_time=localtime()
c_day=current_time.tm_mday
d_month=current_time.tm_mon
e_year=current_time.tm_year
f_hour=current_time.tm_hour
g_min=current_time.tm_min
h_sec=current_time.tm_sec

root.title("HOTEL MANAGEMENT")
root.minsize(1340,900)
root.maxsize(1340,900)

a=Label(root,text="           HOTEL                                                                                                                                             CUSTOMER                                                                                                                EMPLOYEE                                                                   QUIRIES REULT                                                           ",bg="green",fg="white")
a.place(x=0,y=0)


b=Label(root,text="HOTEL NAME")
b.place(x=10,y=80)
c=Label(root,text="HOTEL ID")
c.place(x=10,y=120)
d=Label(root,text="HOTEL LOCATION")
d.place(x=10,y=160)
e=Label(root,text="OWNER NAME")
e.place(x=10,y=200)
f=Label(root,text="HOTEL CONTACT")
f.place(x=10,y=240)
"""
g=Label(root,text="****")
g.place(x=10,y=400)
h=Label(root,text="****")
h.place(x=10,y=520)
i=Label(root,text="****")
i.place(x=10,y=560)
j=Label(root,text="****")
j.place(x=10,y=440)
k=Label(root,text="****")
k.place(x=10,y=480)
"""
b_entry=Entry(root)
b_entry.place(x=150,y=80)
c_entry=Entry(root)
c_entry.place(x=150,y=120)
d_entry=Entry(root)
d_entry.place(x=150,y=160)
e_entry=Entry(root)
e_entry.place(x=150,y=200)
f_entry=Entry(root)
f_entry.place(x=150,y=240)
"""
g_entry=Entry(root)
g_entry.place(x=150,y=400)
h_entry=Entry(root)
h_entry.place(x=150,y=520)
i_entry=Entry(root)
i_entry.place(x=150,y=560)
j_entry=Entry(root)
j_entry.place(x=150,y=440)
k_entry=Entry(root)
k_entry.place(x=150,y=480)


m=StringVar(root)
m.set("           ********")
l=OptionMenu(root,m,"****","****","****","****","******")
l.pack()
l.place(x=80,y=248)

#first_name VARCHAR(20),last_name VARCHAR(20),mobile int(15),email VARCHAR(30),cnic_number VARCHAR(25),date_of_journey date,way_of_payment varchar(20),amount_of_charge int(5),train VARCHAR(20),no_of_ticket int(3),location
"""
#hotel_name VARCHAR(20),hotel_id varchar(20),location varchar(20),owner_name VARCHAR(30),contact
def save_info():
    try:
        sql = "INSERT INTO hotel03(hotel_name,hotel_id,location,owner_name,contact) VALUES (%s,%s,%s,%s,%s)"
        val = (b_entry.get(),c_entry.get(),d_entry.get(),e_entry.get(),f_entry.get())
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    except Exception as e:
        p=Label(root,text=e)
        p.place(x=80,y=600)
        p.pack()


q=Button(root,text="SUBMIT",width="25",fg="white",bg="green",command=save_info)
q.pack()
q.place(x=70,y=300)

def sql1():
    sql_a=Tk()
    sql_a.title("VIEW")
    sql_a.geometry("1340x680+0+0")
        
    import mysql.connector
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="hashamsql",
        database="rdbms"
        )
    print(mydb)
    cursor=mydb.cursor()
    import tkinter as tk
    from tkinter import ttk
    sql="SELECT * FROM hotel03"
    cursor.execute(sql)
    rows=cursor.fetchall()
    frn=Frame(sql_a)
    frn.pack(side=tk.LEFT,padx=0)
    tv=ttk.Treeview(frn,columns=(1,2,3,4,5),show="headings",height="26")
    tv.pack()
    tv.heading(1,text="HOTEL NAME")
    tv.heading(2,text="HOTEL ID")
    tv.heading(3,text="LOCATION")
    tv.heading(4,text="OWNER")
    tv.heading(5,text="CONTACT")
    for i in rows:
        tv.insert("",'end',values=i)
    hor_scroll=ttk.Scrollbar(frn,orient="horizontal",command=tv.xview)
    hor_scroll.pack(side=BOTTOM,fill=X)
    tv.config(xscrollcommand=hor_scroll)
        
buttonFont = font.Font(family='Helvetica', size=8, weight='bold')
bbb=Button(root,text="      HOTEL VIEW     ",command=sql1,font=buttonFont)
bbb.pack()
bbb.place(x=1150,y=80)


def sql2():
    sq2_a=Tk()
    sq2_a.title("VIEW")
    sq2_a.geometry("1340x680+0+0")
        
    import mysql.connector
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="hashamsql",
        database="rdbms"
        )
    print(mydb)
    cursor=mydb.cursor()
    import tkinter as tk
    from tkinter import ttk
    sq2="SELECT * FROM customer03"
    cursor.execute(sq2)
    rows=cursor.fetchall()
    frn=Frame(sq2_a)
    frn.pack(side=tk.LEFT,padx=0)
    tv=ttk.Treeview(frn,columns=(1,2,3,4,5),show="headings",height="26")
    tv.pack()
    tv.heading(1,text="CUSTOMER NAME")
    tv.heading(2,text="CUSTOMER ID")
    tv.heading(3,text="CONTACT")
    tv.heading(4,text="EMAIL")
    tv.heading(5,text="CNIC")
    """
    tv.heading(6,text="DATE OF JOURNEY")
    tv.heading(7,text="WAY OF PAYMENT")
    tv.heading(8,text="AMOUNT OF PAYMENT")
    tv.heading(9,text="TRAIN")
    tv.heading(10,text="NUMBER OF TICKET")
    tv.heading(11,text="LOCATION")
    """
    for i in rows:
        tv.insert("",'end',values=i)
    hor_scroll=ttk.Scrollbar(frn,orient="horizontal",command=tv.xview)
    hor_scroll.pack(side=BOTTOM,fill=X)
    tv.config(xscrollcommand=hor_scroll)
    
        
buttonFont = font.Font(family='Helvetica', size=8, weight='bold')
bbb=Button(root,text="  CUSTOMER VIEW  ",command=sql2,font=buttonFont)
bbb.pack()
bbb.place(x=1150,y=130)

def sql10():    
    import mysql.connector
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="hashamsql",
        database="rdbms"
        )
    print(mydb)
    cursor=mydb.cursor()
    import tkinter as tk
    from tkinter import ttk
    delete='''DELETE FROM hotel03 WHERE location="GULSHAN-E-IQBAL"'''
    cursor.execute(delete)
    mydb.commit()
    
    """
    rows=cursor.fetchall()
    frn=Frame(sq10_a)
    frn.pack(side=tk.LEFT,padx=0)
    tv=ttk.Treeview(frn,columns=(1,2,3,4,5),show="headings",height="26")
    tv.pack()
    tv.heading(1,text="HOTEL NAME")
    tv.heading(2,text="HOTEL ID")
    tv.heading(3,text="LOCATION")
    tv.heading(4,text="OWNER")
    tv.heading(5,text="CONTACT")
    
    tv.heading(6,text="DATE OF JOURNEY")
    tv.heading(7,text="WAY OF PAYMENT")
    tv.heading(8,text="AMOUNT OF PAYMENT")
    tv.heading(9,text="TRAIN")
    tv.heading(10,text="NUMBER OF TICKET")
    tv.heading(11,text="LOCATION")
    
    for i in rows:
        tv.insert("",'end',values=i)
    hor_scroll=ttk.Scrollbar(frn,orient="horizontal",command=tv.xview)
    hor_scroll.pack(side=BOTTOM,fill=X)
    tv.config(xscrollcommand=hor_scroll)
    """
    
        
buttonFont = font.Font(family='Helvetica', size=8, weight='bold')
bbb=Button(root,text=" HOTEL DELETION ",command=sql10,font=buttonFont)
bbb.pack()
bbb.place(x=1150,y=230)

def sql3():
    sq3_a=Tk()
    sq3_a.title("VIEW")
    sq3_a.geometry("1340x680+0+0")
        
    import mysql.connector
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="hashamsql",
        database="rdbms"
        )
    print(mydb)
    cursor=mydb.cursor()
    import tkinter as tk
    from tkinter import ttk
    sq3="SELECT * FROM employee04 where salary=(select max(salary) from employee04)"
    cursor.execute(sq3)
    rows=cursor.fetchall()
    frn=Frame(sq3_a)
    frn.pack(side=tk.LEFT,padx=0)
    tv=ttk.Treeview(frn,columns=(1,2,3,4,5),show="headings",height="26")
    tv.pack()
    tv.heading(1,text="EMPLOYEE NAME")
    tv.heading(2,text="EMPLOYEE ID")
    tv.heading(3,text="CONTACT")
    tv.heading(4,text="EMAIL")
    tv.heading(5,text="SALARY")
    for i in rows:
        tv.insert("",'end',values=i)
    hor_scroll=ttk.Scrollbar(frn,orient="horizontal",command=tv.xview)
    hor_scroll.pack(side=BOTTOM,fill=X)
    tv.config(xscrollcommand=hor_scroll)
        
buttonFont = font.Font(family='Helvetica', size=8, weight='bold')
bbb=Button(root,text="  EMPLOYEE VIEW  ",command=sql3,font=buttonFont)
bbb.pack()
bbb.place(x=1150,y=180)

def sql4():
    sq4_a=Tk()
    sq4_a.title("VIEW")
    sq4_a.geometry("1340x680+0+0")
        
    import mysql.connector
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="hashamsql",
        database="rdbms"
        )
    print(mydb)
    cursor=mydb.cursor()
    import tkinter as tk
    from tkinter import ttk
    sq4='''SELECT * FROM room03 where room_category="VVIP"'''
    cursor.execute(sq4)
    rows=cursor.fetchall()
    frn=Frame(sq4_a)
    frn.pack(side=tk.LEFT,padx=0)
    tv=ttk.Treeview(frn,columns=(1,2,3,4,5),show="headings",height="26")
    tv.pack()
    tv.heading(1,text="ROOM ID")
    tv.heading(2,text="NUMBER OF BED")
    tv.heading(3,text="ROOM DESCRIPTION")
    tv.heading(4,text="ROOM CATEGORY")
    tv.heading(5,text="FLOOR NUMBER")
    for i in rows:
        tv.insert("",'end',values=i)
    hor_scroll=ttk.Scrollbar(frn,orient="horizontal",command=tv.xview)
    hor_scroll.pack(side=BOTTOM,fill=X)
    tv.config(xscrollcommand=hor_scroll)
        
buttonFont = font.Font(family='Helvetica', size=8, weight='bold')
bbb=Button(root,text="    VVIP ROOM VIEW   ",command=sql4,font=buttonFont)
bbb.pack()
bbb.place(x=1150,y=400)

def sql5():
    sq5_a=Tk()
    sq5_a.title("VIEW")
    sq5_a.geometry("1340x680+0+0")
        
    import mysql.connector
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="hashamsql",
        database="rdbms"
        )
    print(mydb)
    cursor=mydb.cursor()
    import tkinter as tk
    from tkinter import ttk
    sq5='''SELECT * FROM booking03 where booking_date>"2021-01-01"'''
    cursor.execute(sq5)
    rows=cursor.fetchall()
    frn=Frame(sq5_a)
    frn.pack(side=tk.LEFT,padx=0)
    tv=ttk.Treeview(frn,columns=(1,2,3,4,5),show="headings",height="26")
    tv.pack()
    tv.heading(1,text="BOOKING ID")
    tv.heading(2,text="BOOKING DATE")
    tv.heading(3,text="BOOKED BY")
    tv.heading(4,text="DESCRIPTION")
    tv.heading(5,text="BOOKING TYPE")

    for i in rows:
        tv.insert("",'end',values=i)
    hor_scroll=ttk.Scrollbar(frn,orient="horizontal",command=tv.xview)
    hor_scroll.pack(side=BOTTOM,fill=X)
    tv.config(xscrollcommand=hor_scroll)
        
buttonFont = font.Font(family='Helvetica', size=8, weight='bold')
bbb=Button(root,text="BOOKING AFTER 2021 ",command=sql5,font=buttonFont)
bbb.pack()
bbb.place(x=1150,y=450)

def sql6():
    sq6_a=Tk()
    sq6_a.title("VIEW")
    sq6_a.geometry("1340x680+0+0")
        
    import mysql.connector
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="hashamsql",
        database="rdbms"
        )
    print(mydb)
    cursor=mydb.cursor()
    import tkinter as tk
    from tkinter import ttk
    sq6="SELECT sum(amount),payment_date FROM payment03 group by payment_date"
    cursor.execute(sq6)
    rows=cursor.fetchall()
    frn=Frame(sq6_a)
    frn.pack(side=tk.LEFT,padx=0)
    tv=ttk.Treeview(frn,columns=(1,2),show="headings",height="26")
    tv.pack()
    tv.heading(1,text="TOTAL AMOUNT")
    tv.heading(2,text="PAYMENT DATE")

    for i in rows:
        tv.insert("",'end',values=i)
    hor_scroll=ttk.Scrollbar(frn,orient="horizontal",command=tv.xview)
    hor_scroll.pack(side=BOTTOM,fill=X)
    tv.config(xscrollcommand=hor_scroll)
        
buttonFont = font.Font(family='Helvetica', size=8, weight='bold')
bbb=Button(root,text="   TOTAL PAYMENT ",command=sql6,font=buttonFont)
bbb.pack()
bbb.place(x=1150,y=500)


def sql55():
    sql_a=Tk()
    sql_a.title("VIEW")
    sql_a.geometry("1340x680+0+0")
        
    import mysql.connector
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="hashamsql",
        database="rdbms"
        )
    print(mydb)
    cursor=mydb.cursor()
    import tkinter as tk
    from tkinter import ttk
    sq6="SELECT * FROM room03"
    cursor.execute(sq6)
    rows=cursor.fetchall()
    frn=Frame(sql_a)
    frn.pack(side=tk.LEFT,padx=0)
    tv=ttk.Treeview(frn,columns=(1,2,3,4,5),show="headings",height="26")
    tv.pack()
    tv.heading(1,text="ROOM ID")
    tv.heading(2,text="NO OF BED")
    tv.heading(3,text="DESCRIPTION")
    tv.heading(4,text="CATEGORY")
    tv.heading(5,text="FLOOR NUMBER")
    

    for i in rows:
        tv.insert("",'end',values=i)
    hor_scroll=ttk.Scrollbar(frn,orient="horizontal",command=tv.xview)
    hor_scroll.pack(side=BOTTOM,fill=X)
    tv.config(xscrollcommand=hor_scroll)
        
buttonFont = font.Font(family='Helvetica', size=8, weight='bold')
bbb=Button(root,text="   ROOM RECORD ",command=sql55,font=buttonFont)#BUTTON NAME
bbb.pack()
bbb.place(x=1150,y=600)#PLACEMENT/LOCATION

#mycursor.execute("create table train_emp4 (slip_number int NOT NULL AUTO_INCREMENT,first_name VARCHAR(20),last_name VARCHAR(20),mobile int,email VARCHAR(30),cnic_number VARCHAR(25),salary int,father_name varchar(20),date_of_birth date,joining_date date,department varchar(25),location varchar(20),primary key(slip_number))")

bemp1=Label(root,text="CUSTOMER NAME")
bemp1.place(x=400,y=80)
cemp1=Label(root,text="CUSTOMER ID")
cemp1.place(x=400,y=120)
demp1=Label(root,text="CONTACT")
demp1.place(x=400,y=160)
eemp1=Label(root,text="EMAIL")
eemp1.place(x=400,y=200)
femp1=Label(root,text="CNIC")
femp1.place(x=400,y=240)
"""
gemp=Label(root,text="****")
gemp.place(x=400,y=400)
hemp=Label(root,text="****")
hemp.place(x=400,y=520)
iemp=Label(root,text="****")
iemp.place(x=400,y=560)
jemp=Label(root,text="****")
jemp.place(x=400,y=440)
kemp=Label(root,text="****")
kemp.place(x=400,y=480)
"""


bemp1_entry=Entry(root)
bemp1_entry.place(x=540,y=80)
cemp1_entry=Entry(root)
cemp1_entry.place(x=540,y=120)
demp1_entry=Entry(root)
demp1_entry.place(x=540,y=160)
eemp1_entry=Entry(root)
eemp1_entry.place(x=540,y=200)
femp1_entry=Entry(root)
femp1_entry.place(x=540,y=240)
"""
gemp_entry=Entry(root)
gemp_entry.place(x=540,y=400)
hemp_entry=Entry(root)
hemp_entry.place(x=540,y=520)
iemp_entry=Entry(root)
iemp_entry.place(x=540,y=560)
jemp_entry=Entry(root)
jemp_entry.place(x=540,y=440)
kemp_entry=Entry(root)
kemp_entry.place(x=540,y=480)




memp=StringVar(root)
memp.set("           ******")
lemp=OptionMenu(root,memp,"ACCOUNTS","MANUFACTURING","SALES","REPAIRING","FINANCIAL")
lemp.pack()
lemp.place(x=430,y=248)



#salary int(8),father_name varchar(20),date_of_birth date,joining_date date,department varchar(25),location
"""
#customer_name VARCHAR(20),customer_id varchar(20),contact varchar(20),email VARCHAR(30),cnic VARCHAR(25),primary key(customer_id))")

def save_info1():
    try:
        sql = "INSERT INTO customer03(customer_name,customer_id,contact,email,cnic) VALUES (%s,%s,%s,%s,%s)"
        val = (bemp1_entry.get(),cemp1_entry.get(),demp1_entry.get(),eemp1_entry.get(),femp1_entry.get())
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    except Exception as e:
        p=Label(root,text=e)
        p.place(x=80,y=600)
        p.pack()

q=Button(root,text="SUBMIT",fg="white",bg="green",width="25",command=save_info1)
q.pack()
q.place(x=450,y=300)


#mycursor.execute("create table train_train10 (train_name VARCHAR(20),train_id VARCHAR(5),shift varchar(10),timing VARCHAR(20),capacity int,shells int,next_journey varchar(20),recent_journey varchar(20),number_of_stations int,root_of_train varchar(35),fault varchar(20),primary key(train_id))")

btra1=Label(root,text="EMPLOYEE NAME")
btra1.place(x=780,y=80)
ctra1=Label(root,text="EMPLOYEE ID")
ctra1.place(x=780,y=120)
dtra1=Label(root,text="CONTACT")
dtra1.place(x=780,y=160)
etra1=Label(root,text="EMAIL")
etra1.place(x=780,y=200)
ftra1=Label(root,text="SALARY")
ftra1.place(x=780,y=240)
"""
gtra=Label(root,text="****")
gtra.place(x=780,y=400)
htra=Label(root,text="****")
htra.place(x=780,y=520)
itra=Label(root,text="****")
itra.place(x=780,y=560)
jtra=Label(root,text="****")
jtra.place(x=780,y=440)
ktra=Label(root,text="****")
ktra.place(x=780,y=480)
"""
btra1_entry=Entry(root)
btra1_entry.place(x=915,y=80)
ctra1_entry=Entry(root)
ctra1_entry.place(x=915,y=120)
dtra1_entry=Entry(root)
dtra1_entry.place(x=915,y=160)
etra1_entry=Entry(root)
etra1_entry.place(x=915,y=200)
ftra1_entry=Entry(root)
ftra1_entry.place(x=915,y=240)
"""
gtra_entry=Entry(root)
gtra_entry.place(x=915,y=400)
htra_entry=Entry(root)
htra_entry.place(x=915,y=520)
itra_entry=Entry(root)
itra_entry.place(x=915,y=560)
jtra_entry=Entry(root)
jtra_entry.place(x=915,y=440)
ktra_entry=Entry(root)
ktra_entry.place(x=915,y=480)


mtra=StringVar(root)
mtra.set("           ****")
ltra=OptionMenu(root,mtra,"KARACHI TO LAHORE","LAHORE TO PINDI","PINDI TO MULTAN","MULTAN TO QUETTA","QUETTA TO FAISLABAD")
ltra.pack()
ltra.place(x=830,y=248)

#train_name VARCHAR(20),train_id VARCHAR(5),shift varchar(10),timing VARCHAR(20),capacity int(25),shells int(8),next_journey varchar(20),recent_journey varchar(20),number_of_stations int(8),root_of_train varchar(25),fault
"""
#employee_name,employee_id,contact varchar(20),email VARCHAR(30),cnic )")

def save_info2():
    try:
        sql = "INSERT INTO employee04(employee_name, employee_id,contact,email,salary) VALUES (%s,%s,%s,%s,%s)"
        val = (btra1_entry.get(),ctra1_entry.get(),dtra1_entry.get(),etra1_entry.get(),ftra1_entry.get())
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    except Exception as e:
        p=Label(root,text=e)
        p.place(x=80,y=600)
        p.pack()

q=Button(root,text="SUBMIT",fg="white",bg="green",width="25",command=save_info2)
q.pack()
q.place(x=850,y=300)

a=Label(root,text="           ROOM                                                                                                                                             BOOKING                                                                                                                PAYMENT                                                                   QUIRIES REULT                                                           ",bg="green",fg="white")
a.place(x=0,y=350)

bb=Label(root,text="ROOM ID")
bb.place(x=10,y=390)
cc=Label(root,text="NO: OF BED")
cc.place(x=10,y=430)
dd=Label(root,text="ROOM DESCRIPTION")
dd.place(x=10,y=470)
ee=Label(root,text="ROOM CATEGORY")
ee.place(x=10,y=510)
ff=Label(root,text="FLOOR NUMBER")
ff.place(x=10,y=550)

bb_entry=Entry(root)
bb_entry.place(x=150,y=390)
cc_entry=Entry(root)
cc_entry.place(x=150,y=430)
dd_entry=Entry(root)
dd_entry.place(x=150,y=470)
ee_entry=Entry(root)
ee_entry.place(x=150,y=510)
ff_entry=Entry(root)
ff_entry.place(x=150,y=550)

#room (room_id ,no_of_bed,room_description ,room_category,floor int")


def save_info_d():
    try:
        sql = "INSERT INTO room03(room_id,no_of_bed,room_description,room_category,floor) VALUES (%s,%s,%s,%s,%s)"
        val = (bb_entry.get(),cc_entry.get(),dd_entry.get(),ee_entry.get(),ff_entry.get())
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    except Exception as e:
        p=Label(root,text=e)
        p.place(x=80,y=600)
        p.pack()

q=Button(root,text="SUBMIT",width="25",fg="white",bg="green",command=save_info_d)
q.pack()
q.place(x=70,y=620)

bemp=Label(root,text="BOOKING ID")
bemp.place(x=400,y=390)
cemp=Label(root,text="BOOKING DATE")
cemp.place(x=400,y=430)
demp=Label(root,text="BOOKED BY")
demp.place(x=400,y=470)
eemp=Label(root,text="DESCRIPTION")
eemp.place(x=400,y=510)
femp=Label(root,text="BOOKING TYPE")
femp.place(x=400,y=550)

bemp_entry=Entry(root)
bemp_entry.place(x=540,y=390)
cemp_entry=Entry(root)
cemp_entry.place(x=540,y=430)
demp_entry=Entry(root)
demp_entry.place(x=540,y=470)
eemp_entry=Entry(root)
eemp_entry.place(x=540,y=510)
femp_entry=Entry(root)
femp_entry.place(x=540,y=550)

# booking (booking_id,booking_date,booked_by,description,booking_type")


def save_info1_d():
    try:
        sql = "INSERT INTO booking03(booking_id,booking_date,booked_by,description,booking_type) VALUES (%s,%s,%s,%s,%s)"
        val = (bemp_entry.get(),cemp_entry.get(),demp_entry.get(),eemp_entry.get(),femp_entry.get())
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    except Exception as e:
        p=Label(root,text=e)
        p.place(x=80,y=600)
        p.pack()

q=Button(root,text="SUBMIT",fg="white",bg="green",width="25",command=save_info1_d)
q.pack()
q.place(x=450,y=620)

btra=Label(root,text="PAYMENT ID")
btra.place(x=780,y=390)
ctra=Label(root,text="PAYMENT DATE")
ctra.place(x=780,y=430)
dtra=Label(root,text="AMOUNT")
dtra.place(x=780,y=470)
etra=Label(root,text="PAID BY")
etra.place(x=780,y=510)
ftra=Label(root,text="DESCRIPTION")
ftra.place(x=780,y=550)

btra_entry=Entry(root)
btra_entry.place(x=915,y=390)
ctra_entry=Entry(root)
ctra_entry.place(x=915,y=430)
dtra_entry=Entry(root)
dtra_entry.place(x=915,y=470)
etra_entry=Entry(root)
etra_entry.place(x=915,y=510)
ftra_entry=Entry(root)
ftra_entry.place(x=915,y=550)

# payment (payment_id,payment_date,amount,paid_by,description


def save_info2():
    try:
        sql = "INSERT INTO payment03(payment_id,payment_date,amount,paid_by,description) VALUES (%s,%s,%s,%s,%s)"
        val = (btra_entry.get(),ctra_entry.get(),dtra_entry.get(),etra_entry.get(),ftra_entry.get())
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    except Exception as e:
        p=Label(root,text=e)
        p.place(x=80,y=600)
        p.pack()

q=Button(root,text="SUBMIT",fg="white",bg="green",width="25",command=save_info2)
q.pack()
q.place(x=850,y=620)


root.mainloop()
