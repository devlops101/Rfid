from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import serial.tools.list_ports
import serial
import requests


# Change this into a http request to get the RFID value from Database
def scanRfid():
    se = serial.Serial("/dev/ttyACM0", 9600)
    b = ''
    b = str(se.readline())

    b = b[2:12]
    if b == "somevalue":
        return 1
    return 0

# See if this works for checking if the port is active
def checkPort():
    return 1
    import serial.tools.list_ports
    ports = list(serial.tools.list_ports.comports())
    if not len(ports):
        messagebox.showerror("Error", "Please plug in the RFID scanner")
        return 0
    else:
        return 1


class Cycle():
    def __init__(self):
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""

    def num_press(self, num):
        temp = text_box.get()
        temp2 = str(num)
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            self.current = temp + temp2
        self.display(self.current)

    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)

    def cancel(self):
        self.current = "0"
        self.display(0)
        self.new_num = True

    def getValue(self):
        print(text_box.get())
        messagebox.showinfo("Success", "You have logged in successfully!")
        openMainMenu()

        # def closeCycle():
        #     global rootMenu, rootCycle
        #     openMainMenu()
        #     rootCycle.destroy()

        # def closeMainMenu():
        #     global rootMenu, rootLogin
        #     openLogin()
        #     rootMenu.destroy()

        # def closeRfid():
        #     global rootMenu, rootScanner
        #     openMainMenu()


def openCycleEntry():
    global rootMenu, rootCycle, rootScanner
    try:
        rootMenu.destroy()
    except:
        pass
    cycleEntry = Cycle()
    rootCycle = Tk()
    rootCycle.geometry("320x480")
    cycle = Frame(rootCycle)
    cycle.grid()

    loadLogo1 = Image.open("gateway logo.png")
    loadLogo1 = loadLogo1.resize((200, 100), Image.ANTIALIAS)
    renderLogo1 = ImageTk.PhotoImage(loadLogo1)

    loadLogo2 = Image.open("crescent.png")
    loadLogo2 = loadLogo2.resize((180, 50), Image.ANTIALIAS)
    renderLogo2 = ImageTk.PhotoImage(loadLogo2)

    logo1 = Label(rootCycle, image=renderLogo1)
    logo2 = Label(rootCycle, image=renderLogo2)

    logo2.image = renderLogo2
    logo1.image = renderLogo1

    logo2.place(relx=0.0, rely=0.1, anchor='w')
    logo1.place(relx=1.0, rely=0.1, anchor='e')

    # Cycle Entry Stuff
    rootCycle.title("")
    global text_box
    text_box = Entry(cycle, justify=RIGHT)
    text_box.grid(row=1, column=0, columnspan=3, padx=100, pady=(100, 10))
    text_box.insert(0, "0")

    bttn_Submit = Button(cycle, text="Submit")
    bttn_Submit["command"] = openRfidScanner
    bttn_Submit.grid(row=2, column=0, columnspan=3, pady=10)

    numbers = "789456123"
    i = 0
    bttn = []
    for j in range(3, 6):
        for k in range(3):
            bttn.append(Button(cycle, text=numbers[i]))
            bttn[i].grid(row=j, column=k, pady=10)
            bttn[i]["command"] = lambda x = numbers[i]: cycleEntry.num_press(x)
            i += 1

    bttn_back = Button(cycle, text="←")
    bttn_back["command"] = openMainMenu
    bttn_back.grid(row=6, column=0, pady=10)

    bttn_0 = Button(cycle, text="0")
    bttn_0["command"] = lambda: cycleEntry.num_press(0)
    bttn_0.grid(row=6, column=1, pady=10)

    clear = Button(cycle, text="C")
    clear["command"] = cycleEntry.cancel
    clear.grid(row=6, column=2, pady=10)

    rootRRN.mainloop()


def openRRNEntry():
    global rootMenu, rootCycle, rootScanner, rootRRN
    try:
        rootMenu.destroy()
    except:
        pass
    try:
        rootScanner.destroy()
    except:
        pass
    cycleEntry = Cycle()
    rootRRN = Tk()
    rootRRN.geometry("480x320")
    RRNentry = Frame(rootRRN)
    RRNentry.grid()

    loadLogo1 = Image.open("gateway logo.png")
    loadLogo1 = loadLogo1.resize((200, 100), Image.ANTIALIAS)
    renderLogo1 = ImageTk.PhotoImage(loadLogo1)

    loadLogo2 = Image.open("crescent.png")
    loadLogo2 = loadLogo2.resize((180, 50), Image.ANTIALIAS)
    renderLogo2 = ImageTk.PhotoImage(loadLogo2)

    logo1 = Label(rootRRN, image=renderLogo1)
    logo2 = Label(rootRRN, image=renderLogo2)

    logo2.image = renderLogo2
    logo1.image = renderLogo1

    logo2.place(relx=0.0, rely=0.1, anchor='w')
    logo1.place(relx=1.0, rely=0.1, anchor='e')

    # Cycle Entry Stuff
    rootRRN.title("")
    rrn = StringVar(rootRRN)
    global text_box
    text_box = Entry(RRNentry, textvariable=rrn, justify=RIGHT)
    text_box.grid(row=1, column=0, columnspan=2, padx=(130,10), pady=(80, 10))
    text_box.insert(0, "0")

    bttn_Submit = Button(RRNentry, text="Submit")
    bttn_Submit["command"] = cycleEntry.getValue
    bttn_Submit.grid(row=1, column=2, pady=(80, 10))

    numbers = "789456123"
    i = 0
    bttn = []
    for j in range(3, 6):
        for k in range(3):
            bttn.append(Button(RRNentry, text=numbers[i]))
            bttn[i].grid(row=j, column=k, padx=(130*(not(k)), 0), pady=10)
            bttn[i]["command"] = lambda x = numbers[i]: cycleEntry.num_press(x)
            i += 1

    bttn_back = Button(RRNentry, text="←")
    bttn_back["command"] = openMainMenu
    bttn_back.grid(row=6, column=0, padx=(130, 0), pady=10)

    bttn_0 = Button(RRNentry, text="0")
    bttn_0["command"] = lambda: cycleEntry.num_press(0)
    bttn_0.grid(row=6, column=1, pady=10)

    clear = Button(RRNentry, text="C")
    clear["command"] = cycleEntry.cancel
    clear.grid(row=6, column=2, pady=10)

    rootRRN.mainloop()


def openRfidScanner():
    global rootMenu, rootCycle, rootScanner, rootLogin
    try:
        rootMenu.destroy()
        print('Menu')
        flag = 1
    except:
        pass
    try:
        rootCycle.destroy()
        print('Cycle')
        flag = 2
    except:
        pass
    try:
        rootLogin.destroy()
        flag = 0
        print('Login')
    except:
        pass

    rootScanner = Tk()

    loadLogo1 = Image.open("gateway logo.png")
    loadLogo1 = loadLogo1.resize((200, 100), Image.ANTIALIAS)
    renderLogo1 = ImageTk.PhotoImage(loadLogo1)

    loadLogo2 = Image.open("crescent.png")
    loadLogo2 = loadLogo2.resize((180, 50), Image.ANTIALIAS)
    renderLogo2 = ImageTk.PhotoImage(loadLogo2)

    logo1 = Label(rootScanner, image=renderLogo1)
    logo2 = Label(rootScanner, image=renderLogo2)

    logo2.image = renderLogo2
    logo1.image = renderLogo1

    logo2.place(relx=0.0, rely=0.1, anchor='w')
    logo1.place(relx=1.0, rely=0.1, anchor='e')
    rootScanner.geometry("480x320")

    text = StringVar()
    ScannerText = Label(rootScanner, textvariable=text)
    text.set("Please place your RFID on the scanner")
    ScannerText.place(relx=0.5, rely=0.5, anchor=CENTER)
    RRNButton = Button(rootScanner, text="Don't have RFID?")
    RRNButton["command"] = openRRNEntry
    RRNButton.place(relx=0.8, rely=0.9, anchor=CENTER)

    if flag == 1:
        BackButton = Button(rootScanner, text="Back to Menu")
        BackButton["command"] = openMainMenu
        BackButton.place(relx=0.2, rely=0.9, anchor=CENTER)
    elif flag == 0:
        BackButton = Button(rootScanner, text="Back to Login")
        BackButton["command"] = openLogin
        BackButton.place(relx=0.2, rely=0.9, anchor=CENTER)

    while True:
        if checkPort():
            check = scanRfid()
            if check == 1:
                openMainMenu()
            else:
                messagebox.showinfo(
                    "Success", "You have logged in successfully")
            rootScanner.update_idletasks()
            rootScanner.update()


def openMainMenu():
    global rootMenu, rootCycle, rootLogin, rootScanner, rootRRN
    try:
        rootCycle.destroy()
        print('Cycle')
    except:
        pass
    try:
        rootLogin.destroy()
        print('Login')
    except:
        pass
    try:
        rootScanner.destroy()
        print('Scanner')
    except:
        pass
    try:
        rootRRN.destroy()
        print('RRN')
    except:
        pass
    rootMenu = Tk()
    rootMenu.geometry("480x320")

    loadLogo1 = Image.open("gateway logo.png")
    loadLogo1 = loadLogo1.resize((200, 100), Image.ANTIALIAS)
    renderLogo1 = ImageTk.PhotoImage(loadLogo1)

    loadLogo2 = Image.open("crescent.png")
    loadLogo2 = loadLogo2.resize((180, 50), Image.ANTIALIAS)
    renderLogo2 = ImageTk.PhotoImage(loadLogo2)

    logo1 = Label(rootMenu, image=renderLogo1)
    logo2 = Label(rootMenu, image=renderLogo2)

    logo2.image = renderLogo2
    logo1.image = renderLogo1

    logo2.place(relx=0.0, rely=0.1, anchor='w')
    logo1.place(relx=1.0, rely=0.1, anchor='e')

    LateEntryButton = Button(rootMenu, text="Late Entry")
    LateEntryButton["command"] = openRfidScanner
    LateEntryButton.place(relx=0.5, rely=0.3, anchor=CENTER)

    SpecialButton = Button(rootMenu, text="Special Permission")
    SpecialButton["command"] = openRfidScanner
    SpecialButton.place(relx=0.5, rely=0.5, anchor=CENTER)

    HomeButton = Button(rootMenu, text="Home")
    HomeButton["command"] = openRfidScanner
    HomeButton.place(relx=0.5, rely=0.7, anchor=CENTER)

    # CycleEntryButton = Button(rootMenu, text="Cycle Entry")
    # CycleEntryButton["command"] = openCycleEntry
    # CycleEntryButton.place(relx=0.5, rely=0.75, anchor=CENTER)

    BackButton = Button(rootMenu, text="Back to Login")
    BackButton["command"] = openLogin
    BackButton.place(relx=0.5, rely=0.9, anchor=CENTER)

    rootMenu.mainloop()


def openLogin():
    global rootLogin, rootMenu, rootCycle, rootScanner
    try:
        rootCycle.destroy()
        print('Cycle')
    except:
        pass
    try:
        rootMenu.destroy()
        print('Menu')
    except:
        pass
    try:
        rootScanner.destroy()
        print('Scanner')
    except:
        pass
    rootLogin = Tk()
    rootLogin.geometry("480x320")

    loadLogo1 = Image.open("gateway logo.png")
    loadLogo1 = loadLogo1.resize((200, 100), Image.ANTIALIAS)
    renderLogo1 = ImageTk.PhotoImage(loadLogo1)

    loadLogo2 = Image.open("crescent.png")
    loadLogo2 = loadLogo2.resize((180, 50), Image.ANTIALIAS)
    renderLogo2 = ImageTk.PhotoImage(loadLogo2)

    Login = Button(rootLogin, text="Login")
    Login["command"] = openMainMenu
    Login.place(relx=0.5, rely=0.5, anchor=CENTER)

    logo1 = Label(rootLogin, image=renderLogo1)
    logo1.image = renderLogo1
    logo2 = Label(rootLogin, image=renderLogo2)
    logo2.image = renderLogo2

    logo2.place(relx=0.0, rely=0.1, anchor='w')
    logo1.place(relx=1.0, rely=0.1, anchor='e')

    rootLogin.mainloop()


openLogin()
