import requests
from tkinter import *
from tkinter.ttk import *

master = Tk()
master.minsize(800, 300)
master.geometry("200x200")


def rotterdam():
    newWindow = Toplevel(master)
    newWindow.title("Station Rotterdam")
    newWindow.geometry("720x580")

    Label(newWindow,
          text="Welkom op Station Rotterdam!").pack()


def tilburg():
    newWindow = Toplevel(master)
    newWindow.title("Station Tilburg")
    newWindow.geometry("720x580")
    Label(newWindow,
          text="Welkom op Station Tilburg!").pack()


def groningen():
    newWindow = Toplevel(master)
    newWindow.title("Station Groningen")
    newWindow.geometry("720x580")
    Label(newWindow,
          text="Welkom op Station Groningen!").pack()


label = Label(master,
              text="Kies een station")

label.pack(pady=10)

master.title('NS Stationszuil')

btn = Button(master,
             text="Rotterdam",
             command=rotterdam)
btn.pack(pady=10)

btn = Button(master,
             text="Groningen",
             command=groningen)
btn.pack(pady=10)

btn = Button(master,
             text="Tilburg",
             command=tilburg)
btn.pack(pady=10)

mainloop()

# Openweather Api

appid = "203806fcf1ddff2d3a9937e6b90ca80c"

URL = f'http://api.openweathermap.org/data/2.5/weather?q=Groningen,nl&APPID=203806fcf1ddff2d3a9937e6b90ca80c'

r = requests.get(URL)

res = r.json()
