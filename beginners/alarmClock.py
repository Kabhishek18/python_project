from tkinter import *
import datetime
import time
import winsound

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        if now == set_alarm_timer:
            print("Time to Wake up")
            winsound.PlaySound("sound.wav",winsound.SND_NOSTOP)
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

def time():
    current_time = datetime.datetime.now()
    now = current_time.strftime("%H:%M:%S")
    date = current_time.strftime("%d/%m/%Y")
    lbl.config(text=now)
    lbl.after(1000, time)


clock=Tk()
clock.title("DataFlair Alarm Clock")
clock.geometry("500x330")
canvas= Canvas(clock, bg='black', width=1000)


Welcome = Label(clock,text = "WELCOME TO MY ALARM CLOCK",fg="black",relief = "solid",font=("Arial",20,'bold')).place(x=20, y=80)

lbl = Label(clock, font=('calibri', 40, 'bold'),background='black',foreground='white', width=60)
lbl.pack(anchor='center')
time()
canvas.pack()

time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=220)
addTime = Label(clock,text = "Hour   Min     Sec",font=60).place(x = 110,y=130)
setYourAlarm = Label(clock,text = "ALARM ",fg="black",relief = "solid",font=("Helevetica",9,"bold")).place(x=50, y=160)

hour = StringVar()
min = StringVar()
sec = StringVar()


hourTime= Entry(clock,textvariable = hour,bg = "yellow",width = 10).place(x=110,y=160)
minTime= Entry(clock,textvariable = min,bg = "yellow",width = 10).place(x=150,y=160)
secTime = Entry(clock,textvariable = sec,bg = "yellow",width = 10).place(x=200,y=160)


submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =110,y=190)
clock.mainloop()












