# -*- codi9ng: utf-8 -*-
import pyowm
from tkinter import *
import time
import calendar
from datetime import date


owm = pyowm.OWM(API_key='7929ea8c436a38a5367c4b53cd53944b',language='pt')
observation = owm.weather_at_place("Barueri,br")
w = observation.get_weather()
temperatureC = w.get_temperature('celsius')

mirror = Tk()
mirror.title("Smart Mirror")
width, height = mirror.winfo_screenwidth(), mirror.winfo_screenheight()

def smartMirror():
    mirror.configure(background='black')
    w = observation.get_weather()
    hour = time.strftime("%H:%M:%S %Z")
    date = "%s" % (time.strftime("%A, %B %dth"))

    wind = w.get_wind()
    temperature = w.get_temperature('celsius')
    tomorrow = pyowm.timeutils.tomorrow()
    status = w.get_detailed_status()

    #Tkinter
    ico_cloudy = PhotoImage(file="cloudy.png")

    lbl_hour = Label(mirror, text=str(hour)[:5], background="black", fg="white", font='DistrictThin 100 bold')
    lbl_date = Label(mirror, text=str(date), background="black", fg="white", font='DistrictThin 12 bold')

    #lbl_today = Label(mirror, text=str(days[today.weekday()]), background="black", fg="white", font='DistrictThin 12 bold')

    lbl_ico = Label(mirror,image= ico_cloudy, background="black", fg="white")
    lbl_temp = Label(mirror, text= str(temperature.get('temp'))[:2] + "o", background="black", fg="white",font='DistrictThin 100 bold', justify="right")
    lbl_temp2 = Label(mirror, text= "Barueri", background="black", fg="white", justify="right",font='DistrictThin 30 bold')
    lbl_status = Label(mirror, text = str(status.title()), background="black", fg="white",font='DistrictThin 12 bold')
    lbl_wind = Label(mirror, text = "Ventos a " + str(wind.get("speed")*1.60934)[:4] + "Km/h", background="black", fg="white",font='DistrictThin 12 bold')

    lbl_hour.place (x=0, y=30)
    lbl_date.place (x=0, y=0)

    lbl_ico.place (x=600, y=0)
    lbl_temp.place (x=800, y=0)
    lbl_temp2.place (x=805, y=130)
    lbl_wind.place (x=805, y=180)
    lbl_status.place (x=620, y=180)

    #mirror.geometry("300x300+200+200")
    mirror.geometry("%dx%d+0+0" % (width, height))
    mirror.update()

    #print (days[today.weekday()])

    return

smartMirror()
time.sleep(60)
