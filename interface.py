from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
#import os
import sqlite3
import time
import datetime

global items
items = ['ADIDAS SHOES', 'FILA SHOES', 'ROASTER SHOES','NIKE SHOES']
global pppp
pppp=0
global offer
offer=False
def mainPage():
    global appm
    appm = Tk()
    appm.title("MOCHI App")
    appm.configure(background="light green")
    w=850
    h=550
    ws = appm.winfo_screenwidth()
    hs = appm.winfo_screenheight()
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    appm.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    img=PhotoImage(file='Mochi-logo.gif').subsample(4,4)
    item1=Label(appm,image=img)
    item1.pack(pady=(10,0))
    sub=Label(appm,text="Estd. in 2019",fg="red",bg="yellow",font="Times")
    sub.pack(pady=(0,0))
    sub=Label(appm,text="We believe in quality.",fg="red",bg="yellow",font="Italic")
    sub.pack(pady=(0,0))
    
    welcomeLabel = Label(appm, text='Welcome To \n Shoe store',bg="light green", font='Times 36 bold')
    welcomeLabel.pack(pady=(20,20))

    loginButton = Button(appm, text="Login", command=login,bg="light blue", width=14, font="Times 16")
    loginButton.pack(pady=10)

    registerButton = Button(appm, text="Register", command=register,bg="light blue", width=14, font="Times 16")
    registerButton.pack(pady=10)

    appm.mainloop()

def login():
    try:
        appr.destroy()
    except:
        try:
            appm.destroy()
        except:    
            apps.destroy()
    
    global appl
    appl = Tk()
    appl.configure(background="sky blue")
    w=850
    h=550
    ws=appl.winfo_screenwidth()
    hs=appl.winfo_screenheight()
    
    loginPg = Label(appl, text="",bg="sky blue")
    loginPg.pack()
    
    img=PhotoImage(file='Mochi-logo.gif').subsample(4,4)
    item1=Label(appl,image=img)
    item1.pack(pady=0)
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    appl.geometry('%dx%d+%d+%d' % (w, h, x, y))
    appl.title("Login")

    loginPg = Label(appl, text="Login Page",bg="sky blue", font="Times 32 bold")
    loginPg.pack(pady=(40,40))

    info = Frame(height=500, width=500)
    info.pack()

    usernameLabel = Label(info, text="Username  : ",bg="sky blue", font="Times 15")
    usernameLabel.grid(column=0, row=0)

    passwordLabel = Label(info, text="Password  : ",bg="sky blue", font="Times 15")
    passwordLabel.grid(column=0, row=1)

    usernameEntry = Entry(info)
    usernameEntry.grid(column=1, row=0)

    passwordEntry = Entry(info,show='*')
    passwordEntry.grid(column=1, row=1)

    loginButton = Button(appl, text="Login",bg="orange", command=lambda: [loginUser(usernameEntry.get(), passwordEntry.get())], width=10, font="Times 14")
    loginButton.pack(pady=20)

    appl.mainloop()

def loginUser(eusername, epassword):
    
    db = sqlite3.connect("userdata.db")
    cursor = db.cursor()
    sql = "select * from user where username = '%s'"%(eusername)
    cursor.execute(sql)
    val = cursor.fetchall()
    db.commit()
    try:
        if(str(val[0][2])==str(eusername)):
            if(str(val[0][3])==str(epassword)):
                app = Tk()
                w=300
                h=200
                ws = app.winfo_screenwidth()
                hs = app.winfo_screenheight()
                x = (ws/2) - (w/2)    
                y = (hs/2) - (h/2)
                app.geometry('%dx%d+%d+%d' % (w, h, x, y))
                app.title("User Loged in")
                app.configure(background="yellow")
                tlabel = Label(app, text="Loged in Successfully",bg="yellow", font="Times 16 bold")
                tlabel.pack(pady=10)
                tlabel1 = Label(app, text="big trillion days\n coming soon!!!",bg="light green",fg="red", font="Italic")
                tlabel1.pack(pady=10)
                tButton = Button(app, text="OK",bg="orange", command=lambda:[app.destroy(), shoppingCart(eusername, epassword)], width=10, font="Times 12")
                tButton.pack(pady=10)

                app.mainloop()
                
            else:
                app = Tk()
                w=300
                h=180
                ws = app.winfo_screenwidth()
                hs = app.winfo_screenheight()
                x = (ws/2) - (w/2)    
                y = (hs/2) - (h/2)
                app.geometry('%dx%d+%d+%d' % (w, h, x, y))
                app.title("Wrong Password")

                tlabel = Label(app, text="Wrong Password", font="Times 16 bold")
                tlabel.pack(pady=10)

                tButton = Button(app, text="Try Again", command=lambda:[app.destroy()], width=10, font="Times 12")
                tButton.pack(pady=10)

                app.mainloop()
        else:
            app = Tk()
            w=300
            h=300
            ws = app.winfo_screenwidth()
            hs = app.winfo_screenheight()
            x = (ws/2) - (w/2)    
            y = (hs/2) - (h/2)
            app.geometry('%dx%d+%d+%d' % (w, h, x, y))
            app.title("Error")

            tlabel = Label(app, text="Something Went Wrong \n Check Login Details \n or \n Register", font="Times 16 bold")
            tlabel.pack(pady=10)

            tButton = Button(app, text="Login", command=lambda:[app.destroy()], width=10, font="Times 12")
            tButton.pack(pady=10)

            t2Button = Button(app, text="Register", command=lambda:[app.destroy(), register()], width=10, font="Times 12")
            t2Button.pack(pady=10)

            app.mainloop()

    except:
        app = Tk()
        w=300
        h=300
        ws = app.winfo_screenwidth()
        hs = app.winfo_screenheight()
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        app.geometry('%dx%d+%d+%d' % (w, h, x, y))
        app.title("yooo")

        tlabel = Label(app, text="Couldn't connect to the database \n or \n Register", font="Times 16 bold")
        tlabel.pack(pady=10)

        tButton = Button(app, text="Login", command=lambda:[app.destroy()], width=10, font="Times 12")
        tButton.pack(pady=10)

        t2Button = Button(app, text="Register", command=lambda:[app.destroy(), register()], width=10, font="Times 12")
        t2Button.pack(pady=10)

        app.mainloop()

def register():
    try:
        appm.destroy()
    except:
        appl.destroy()
    
    global appr
    appr = Tk()
    w=850
    h=550
    ws = appr.winfo_screenwidth()
    hs = appr.winfo_screenheight()
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    appr.geometry('%dx%d+%d+%d' % (w, h, x, y))
    appr.title("Register")
    appr.configure(background="light blue")
   # cred=True
    registerPg = Label(text="Register Page",bg="light blue", font="Times 32 bold")
    registerPg.pack(pady=(100,60))

    info = Frame(height=150, width=300)
    info.pack()

    fullnameLabel = Label(info, text="Full Name  : ",bg="light blue", font="Times 15")
    fullnameLabel.grid(column=0, row=0)

    emailLabel = Label(info, text="Email  : ",bg="light blue", font="Times 15")
    emailLabel.grid(column=0, row=1)

    usernameLabel = Label(info, text="User name  : ",bg="light blue", font="Times 15")
    usernameLabel.grid(column=0, row=2)

    passwordLabel = Label(info, text="Password  : ",bg="light blue", font="Times 15")
    passwordLabel.grid(column=0, row=3)

    fullnameEntry = Entry(info)
    fullnameEntry.grid(column=1, row=0)

    emailEntry = Entry(info)
    emailEntry.grid(column=1, row=1)
    usernameEntry = Entry(info)
    usernameEntry.grid(column=1, row=2)

    passwordEntry = Entry(info, show='*')
    passwordEntry.grid(column=1, row=3)
    """mail=emailEntry.get(info)
    if(mail[-1:-11:-1]!="moc.liamg@"):
        messagebox.showerror("Invalid gmail","Gmail should end with @gmail.com")
        cred=False"""
    registerButton = Button(appr, text="Register",bg="orange", command=lambda:[addUser(fullnameEntry.get(), emailEntry.get(), usernameEntry.get(), passwordEntry.get())], width=10, font="Times 14")
    registerButton.pack(pady=20)

    appr.mainloop()

def addUser(name, email, username, password):

    db = sqlite3.connect("userdata.db")
    cursor = db.cursor()
    qur = "select count(*) from user where username = '%s'"%(username)
    cursor.execute(qur)
    val = cursor.fetchall()[0]
    if(val==0):
        try:
            sql = "insert into user(name, email, username, password) values ('%s','%s','%s','%s')"%(name, email, username, password)
            cursor.execute(sql)
            db.commit()

            app = Tk()
            w=300
            h=200
            ws = app.winfo_screenwidth()
            hs = app.winfo_screenheight()
            x = (ws/2) - (w/2)    
            y = (hs/2) - (h/2)
            app.geometry('%dx%d+%d+%d' % (w, h, x, y))
            app.title("User Added")

            tlabel = Label(app, text="User Added Successfully \n Try To Login ", font="Times 16 bold")
            tlabel.pack(pady=10)

            tButton = Button(app, text="Login", command=lambda:[app.destroy(), login()], width=10, font="Times 12")
            tButton.pack(pady=10)

            app.mainloop()

        except:
            app = Tk()
            w=300
            h=300
            ws = app.winfo_screenwidth()
            hs = app.winfo_screenheight()
            x = (ws/2) - (w/2)    
            y = (hs/2) - (h/2)
            app.geometry('%dx%d+%d+%d' % (w, h, x, y))
            app.title("Error")

            elabel = Label(app, text="Something Went Wrong \n Try Again \n ", font="Times 16 bold")
            elabel.pack(pady=10)

            eButton = Button(app, text="Try Again", command=lambda:[app.destroy()], width=10, font="Times 12")
            eButton.pack(pady=10)

            app.mainloop()

    else:
        app = Tk()
        w=300
        h=200
        ws = app.winfo_screenwidth()
        hs = app.winfo_screenheight()
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        app.geometry('%dx%d+%d+%d' % (w, h, x, y))
        app.title("Error")

        elabel = Label(app, text="Username Already Exist \n Try Again With \n Unique Username", font="Times 16 bold")
        elabel.pack(pady=10)

        eButton = Button(app, text="Try Again", command=lambda:[app.destroy()], width=10, font="Times 10")
        eButton.pack(pady=10)

        app.mainloop()


def shoppingCart(username, password):
    try:
        appl.destroy()
    except:
        appc.destroy()

    global apps
    apps = Tk()
    w=700
    h=620
    ws = apps.winfo_screenwidth()
    hs = apps.winfo_screenheight()
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    apps.geometry('%dx%d+%d+%d' % (w, h, x, y))
    apps.geometry('700x650')
    apps.title("Shoping Cart App")
    colour="skyblue"
    apps.configure(background=colour)

    title = Label(apps, text='All Products',bg=colour, font='Times 30 bold')
    title.grid(padx=(100,40), pady=(10,0), column=1, row=0)
    
    back=Button(apps,text='back',command=lambda:[login()],bg=colour)
    back.grid(column=2,row=0)

    img1 = ImageTk.PhotoImage(Image.open("shoe1.jpg"))
    panel1 = Label(apps, image = img1)
    panel1.grid(padx=(20,0), pady=10, column=0, row=2, sticky='w')

    name1 = Label(apps, text='ADIDAS SHOES  1999 RS',bg=colour, font='Times 16')
    name1.grid(padx=30, column=1, row=2, sticky='w')

    cartButton = Button(apps, text='Add To Cart',bg="orange", command=lambda:[cartAdd(username, password, items[0])],width=10, font="Times 14")
    cartButton.grid(column=2, row=2)

    img2 = ImageTk.PhotoImage(Image.open("shoe2.jpg"))
    panel2 = Label(apps, image = img2)
    panel2.grid(padx=(20,0), pady=10, column=0, row=3, sticky='w')

    name2 = Label(apps, text='FILA SHOES 2699 RS',bg=colour, font='Times 16')
    name2.grid(padx=30, column=1, row=3, sticky='w')

    cartButton = Button(apps, text='Add To Cart',bg="orange", command=lambda:[cartAdd(username, password, items[1])],width=10, font="Times 14")
    cartButton.grid(column=2, row=3)

    img3 = ImageTk.PhotoImage(Image.open("shoe3.jpg"))
    panel3 = Label(apps, image = img3)
    panel3.grid(padx=(20,0), pady=10, column=0, row=4, sticky='w')

    name3 = Label(apps, text='ROADSTER SHOES 999 RS',bg=colour, font='Times 16')
    name3.grid(padx=30, column=1, row=4, sticky='w')

    cartButton = Button(apps, text='Add To Cart',bg="orange", command=lambda:[cartAdd(username, password, items[2])],width=10, font="Times 14")
    cartButton.grid(column=2, row=4)

    img4 = ImageTk.PhotoImage(Image.open("shoe4.jpg"))
    panel4 = Label(apps, image = img4)
    panel4.grid(padx=(20,0), pady=10, column=0, row=5, sticky='w')

    name4 = Label(apps, text='NIKE SHOES 1799 RS',bg=colour, font='Times 16')
    name4.grid(padx=30, column=1, row=5, sticky='w')

    cartButton = Button(apps, text='Add To Cart',bg="orange", command=lambda:[cartAdd(username, password, items[3])],width=10, font="Times 14")
    cartButton.grid(column=2, row=5)

    viewButton = Button(apps, text='Show Cart',bg="light green",command=lambda: [cartDetails(username, password)], fg='green',width=10, font="Times 14")
    viewButton.grid(padx=(50,0), column=1, row=6)    
    class App():
        def __init__(self):
            self.label1=Label(apps,text="GET FLAT 10% OFF FROM\n 12:00 AM TO 4:00 AM",bg="red",fg="yellow",font=('Arial', 12, 'bold', 'italic'))
            self.label1.grid(row=0,column=0)
            self.label = Label(apps,text="",bg="sky blue",font=('Arial', 12, 'bold', 'italic'))
            self.label.grid(row=1,column=0)
            self.update_clock()
            apps.mainloop()

        def update_clock(self):
            now = time.strftime("%H:%M:%S")
            pres=datetime.datetime.now()
            if((pres.hour>=21)and(pres.hour<=22)):
                global offer
                offer=True
            self.label.configure(text=now)
            apps.after(1000, self.update_clock)
    app=App()

def cartAdd(username, password, item):
    ( username, password, item)
    db = sqlite3.connect("userdata.db")
    global pppp
    if(offer):
        messagebox.showinfo("offer","you've got an offer!!!")
    cursor = db.cursor()
    a='ADIDAS SHOES'
    b='FILA SHOES'
    c='ROADSTER SHOES'
    d='NIKE SHOES'
    if item==items[0]:
        pppp=pppp+1999
    if item==items[1]:
        pppp=pppp+2699
    if item==items[2]:
        pppp=pppp+999
    if item==items[3]:
        pppp=pppp+1799
    
    try:
        sql = "insert into cart(username, password, cart) values ('%s','%s','%s')"%(username, password, item)
        cursor.execute(sql)
        db.commit()
        app = Tk()
        w=300
        h=200
        ws = app.winfo_screenwidth()
        hs = app.winfo_screenheight()
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        app.geometry('%dx%d+%d+%d' % (w, h, x, y))
        app.title("Product Added")
        app.configure(background="yellow")
        tlabel = Label(app, text="Product Added Successfully", bg="yellow",font="Times 16 bold")
        tlabel.pack(pady=10)

        tButton = Button(app, text="OK", command=lambda:[app.destroy()],bg="red", width=10, font="Times 12")
        tButton.pack(pady=10)

        app.mainloop()

    except:
        app = Tk()
        w=300
        h=200
        ws = app.winfo_screenwidth()
        hs = app.winfo_screenheight()
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        app.geometry('%dx%d+%d+%d' % (w, h, x, y))
        app.title("Error")

        elabel = Label(app, text="Something Went Wrong \n Try Again", font="Times 16 bold")
        elabel.pack(pady=10)

        eButton = Button(app, text="Try Again", command=lambda:[app.destroy()], width=10, font="Times 12")
        eButton.pack(pady=10)

        app.mainloop()
#==========================================================================================================================
def payment():
        import random
        global offer
        global pppp
        otp=random.randint(100000,999999)
        payment_page=Tk()
        payment_page.geometry("850x600")
        payment_page.title("Payment")
        welcmeLabel = Label(payment_page, text='Payment', font='Times 30 bold')
        welcmeLabel.pack(pady=(0,0))
        if(offer):
            pppp=pppp-(pppp//10)
            label_amt = Label(payment_page, text=pppp,width=20,font="Times 12 bold")
            label_amt.place(x=280,y=100)
            offer=False
        else:
            label_amt = Label(payment_page, text=pppp,width=20,font="Times 12 bold")
            label_amt.place(x=280,y=100)    
        label_10 = Label(payment_page, text="CARD NUMBER",width=20,font=("bold", 10))
        label_10.place(x=250,y=130)
        card=IntVar() 
        entry_10 = Entry(payment_page,textvariable=card)
        entry_10.place(x=440,y=130)
        label_10 = Label(payment_page, text="CVV",width=20,font=("bold", 10))
        label_10.place(x=250,y=170)
        cvv=IntVar() 
        entry_10 = Entry(payment_page,textvariable=cvv,show='*')
        entry_10.place(x=440,y=170)
        def press():
            pp=str(card.get())
            pp=len(pp)
            cvv1=str(cvv.get())
            cvv1=len(cvv1)
            if pp<16 and cvv1<3  :
                messagebox.showerror("Error", "Invalid card/cvv number please try Again After some time")
            elif pp>16 and cvv1>3 :
                messagebox.showerror("Error", "Invalid card/cvv number please try Again After some time")
            elif pp>16 and cvv1<3 :
                messagebox.showerror("Error", "Invalid card/cvv number please try Again After some time")
            elif pp<16 and cvv1>3 :
                messagebox.showerror("Error", "Invalid card/cvv number please try Again After some time")
            else:
                (otp)
                
        #press()
        pressB=Button(payment_page, text="Generate OTP",bg='brown', command=press)
        pressB.place(x=300,y=200)
        inotp=IntVar()
        entry_10 = Entry(payment_page,textvariable=inotp)
        entry_10.place(x=460,y=220)
        def pay():
            if inotp.get() == otp:
                ida=random.randint(100,100000)
                id1=ida
                ph=phone.get()
                ida=str(ida)
                idb="Paymennt Success Reference ID -> "+ida
                messagebox.showinfo("Succesfull",idb)
                co = sqlite3.connect('payments.db')
                d = co.cursor()
                d.execute('INSERT INTO payments(username,id,price) VALUES(?,?,?)' ,(name,id1,pppp))
                co.commit()
                co.close()
                
            else:
                messagebox.showerror("Payent failed", "Invalid OTP please try Again After some time")
                
        pressB=Button(payment_page, text="PAY",bg='brown',command=pay)
        pressB.place(x=480,y=240)

#==========================================================================================================================

def cartDetails(username, password):
    apps.destroy()

    global appc
    appc = Tk()
   
    appc.geometry('1300x800')
    appc.title("Shoping Cart App")

    db = sqlite3.connect("userdata.db")
    cursor = db.cursor()
    def clearcart():
        db = sqlite3.connect("userdata.db")
        cursor = db.cursor()
        sql = "delete from cart where username='%s'"%(username)
        cursor.execute(sql)
        aitem = cursor.fetchall()
        db.commit()
        shoppingCart(username, password)
        try:
            appc.destroy()
        except:
            apps.destroy()
    

    try:
        sql = "select * from user where username='%s' "%(username)
        cursor.execute(sql)
        details = cursor.fetchall()
        elabel = Label(appc, text="User Details", font="Times 28 bold")
        elabel.pack(pady=(10,20))
        elabel = Label(appc, text="Name  -  %s"%(str(details[0][0])), font="Times 16")
        elabel.pack(pady=3)
        elabel = Label(appc, text="Email  -  %s"%(str(details[0][1])), font="Times 16")
        elabel.pack(pady=3)
        elabel = Label(appc, text="Username  -  %s"%(str(details[0][2])), font="Times 16")
        elabel.pack(pady=(3,40))



        elabel = Label(appc, text="Cart Items", font="Times 28 bold")
        elabel.pack(pady=(0,20))
        backButton = Button(appc, text='Back',command=lambda: [shoppingCart(username, password)], width=10, font="Times 14")
        backButton.pack(pady=(25,10))
        buyButton = Button(appc, text='Payment',command=lambda: payment(), width=10, font="Times 14")
        buyButton.pack(pady=(25))
        clearcartButton = Button(appc, text='Clear cart',command=lambda: clearcart(), width=10, font="Times 14")
        clearcartButton.pack()

        sql = "select cart from cart where username='%s' "%(username)
        cursor.execute(sql)
        aitem = cursor.fetchall()

        for row in aitem:
            elabel = Label(appc, text='%s'%(row), font="Times 16")
            elabel.pack(pady=5)

        db.commit()

       

    except:
        app = Tk()
        w=300
        h=200
        ws = app.winfo_screenwidth()
        hs = app.winfo_screenheight()
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        app.geometry('%dx%d+%d+%d' % (w, h, x, y))
        app.title("Error")

        elabel = Label(app, text="Something Went Wrong \n Try Again", font="Times 16 bold")
        elabel.pack(pady=10)

        eButton = Button(app, text="Try Again", command=lambda:[app.destroy()], width=10, font="Times 12")
        eButton.pack(pady=10)

        app.mainloop()   

    appc.mainloop()

if __name__ == '__main__':
    mainPage()
    
    
