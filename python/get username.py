import tkinter as tk
import serial.tools.list_ports
import serial
import requests

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='RFID SCAN')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

##label2 = tk.Label(root, text='Type your Name')
##label2.config(font=('helvetica', 10))
##canvas1.create_window(100, 100, window=label2)
##
##entry1 = tk.Entry (root) 
##canvas1.create_window(300, 100, window=entry1)

label3 = tk.Label(root, text='Type your RRN')
label3.config(font=('helvetica', 10))
canvas1.create_window(140, 140, window=label3)

label4 = tk.Label(root, text='RFID:')
label4.config(font=('helvetica', 10))
canvas1.create_window(180, 180, window=label4)

rrn = tk.StringVar(root)
entry1 = tk.Entry (root, textvariable = rrn) 
canvas1.create_window(260, 140, window=entry1)
RRN = rrn.get()


def getrfid ():
    global b
    se=serial.Serial("COM3",9600)
    b=''
    b=str(se.readline())
    b=b[2:len(b)-5]
    if b:
        label2 = tk.Label(root, text='RFID Scanned Successfully')
        print(RRN)
        label2.config(font=('helvetica', 10))
        canvas1.create_window(200, 200, window=label2)
        

def upload():

    global b
    url = 'http://172.22.209.253:8000/api/rfidregister'
    RRN = rrn.get()
    #print(RRN)
    myobj = {'rrn':RRN,'RFID':b}

    x = requests.post(url, data = myobj)

    print(x.text)
    
##button1 = tk.Button(text='SCAN', command=getrfid, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
##canvas1.create_window(220, 180, window=button1)
button2 = tk.Button(text='UPLOAD', command=upload, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 240, window=button2)

root.mainloop()
##while True:
##    getrfid()
##    print("Hello")
##    root.update_idletasks()
##    root.update()
    
    
