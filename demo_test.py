from tkinter import * 
from tkinter import ttk
import requests


def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=50786b2f704cf27b21df2360dc7adfc7").json()
    w_label1.config(text=data["weather"][0]["main"])
    w_description1.config(text=data["weather"][0]["description"])
    w_temparature1.config(text=str(data["main"]["temp"]-273.15))
    w_pressure1.config(text=data["main"]["pressure"])

win = Tk() 
win.title("My Weather App")
win.config(bg="blue")
win.geometry("570x500")

name_label = Label(win,text='Weather App',font=("Time New Roman",40,"bold"))

name_label.place(x=50,y=25,height=50,width=420)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com = ttk.Combobox(win,text="Weather App",values=list_name,font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=50,y=100,height=40,width=420)

done_bth = Button(win,text='Done',font=("Time New Roman",25,"bold"),command=data_get)
done_bth.place(x=240,y=180,height=50,width=100)

w_label = Label(win,text='Weather Climate',font=("Time New Roman",15,"bold"))
w_label.place(x=50,y=240,height=30,width=200)

w_label1 = Label(win,text='',font=("Time New Roman",15,"bold"))
w_label1.place(x=270,y=240,height=30,width=200)


w_description = Label(win,text='Weather Description',font=("Time New Roman",15,"bold"))
w_description.place(x=50,y=290,height=30,width=200)

w_description1 = Label(win,text='',font=("Time New Roman",15,"bold"))
w_description1.place(x=270,y=290,height=30,width=200)


w_temparature = Label(win,text='Weather Temparature',font=("Time New Roman",15,"bold"))
w_temparature.place(x=50,y=340,height=30,width=210)

w_temparature1 = Label(win,text='',font=("Time New Roman",15,"bold"))
w_temparature1.place(x=270,y=340,height=30,width=210)

w_pressure = Label(win,text='Weather Pressure',font=("Time New Roman",15,"bold"))
w_pressure.place(x=50,y=390,height=30,width=200)

w_pressure1 = Label(win,text='',font=("Time New Roman",15,"bold"))
w_pressure1.place(x=270,y=390,height=30,width=200)


win.mainloop()