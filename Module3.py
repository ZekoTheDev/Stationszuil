# Importeer 'requests' module API Requests te kunnen maken
# Importeer 'tkinter' module om een GUI te realiseren
import psycopg2
import requests
from tkinter import *
from tkinter.ttk import *

# Openweather Api

import requests
from math import *

appid = "203806fcf1ddff2d3a9937e6b90ca80c"

urlGroningen = f'http://api.openweathermap.org/data/2.5/weather?q=Groningen,nl&APPID=203806fcf1ddff2d3a9937e6b90ca80c'
urlTilburg = f'http://api.openweathermap.org/data/2.5/weather?q=Tilburg,nl&APPID=203806fcf1ddff2d3a9937e6b90ca80c'
urlHaarlem = f'http://api.openweathermap.org/data/2.5/weather?q=Haarlem&unit=metric,nl&APPID=203806fcf1ddff2d3a9937e6b90ca80c'

rGr = requests.get(urlGroningen)
rTi = requests.get(urlTilburg)
rHa = requests.get(urlHaarlem)

resGr = rGr.json()
resTi = rTi.json()
resHa = rHa.json()


basisGr = resGr['main']
basisTi = resGr['main']
basisHa = resGr['main']

tempKevGr = basisGr['temp']
tempKevTi = basisTi['temp']
tempKevHa = basisHa['temp']


def kelvinToCelsius(kelvin):
    return f'Het is momenteel {ceil(kelvin - 273.15)} Graden'


celsiusGr = kelvinToCelsius(tempKevGr)
celsiusTi = kelvinToCelsius(tempKevTi)
celsiusHa = kelvinToCelsius(tempKevHa)


# Vul Database Credentials in
connection_string = "host='localhost' dbname='derdedb' user='postgres' password='36802002'"
conn = psycopg2.connect(connection_string)
cursor = conn.cursor()

queryHaarlem = """SELECT bericht 
                  FROM berichten
                  WHERE station_city = 'Haarlem'
                  ORDER BY berichtdatum ASC LIMIT 5;
;"""

cursor.execute(queryHaarlem)
haarlemRes = cursor.fetchall()


queryTilburg = """SELECT bericht 
                  FROM berichten
                  WHERE station_city = 'Tilburg'
                  ORDER BY berichtdatum ASC LIMIT 5;
;"""

cursor.execute(queryTilburg)
tilburgRes = cursor.fetchall()


queryGroningen =  """SELECT bericht
                  FROM berichten
                  WHERE station_city = 'Groningen'
                  ORDER BY berichtdatum ASC LIMIT 5;
;"""

cursor.execute(queryGroningen)
groningenRes = cursor.fetchall()
conn.close()


# Roep de Tkinter module aan
master = Tk()
master.minsize(600, 300)
master.geometry("235x270")

labeltwee = Label(master=master, text='Welkom bij NS!')
labeltwee.pack()




# Laat linksboven zien dat de venster een 'NS Stationzuil' Applicatie is
master.title('NS Stationszuil')


# Functie zorgt ervoor dat er een nieuw venster word geopend zodra gebruiker op 'Haarlem' klikt
def haarlem():
    newWindow = Toplevel(master)
    newWindow.title("Station Haarlem")
    newWindow.geometry("720x580")
    # x = 0
    # y = 0
    # for i in range(4):
    #     label = Label(master=master, text='dd')
    #     label.grid(row=x, column=y)
    #     x += 1
    Label(newWindow,
          text="Welkom op Station Haarlem!").pack()
    Label(newWindow,
          text=f"{haarlemRes}!",background='white').pack()
    Label(newWindow,
          text=f"{celsiusHa}").pack()


# Functie zorgt ervoor dat er een nieuw venster word geopend zodra gebruiker op 'Tilburg' klikt
def tilburg():
    newWindow = Toplevel(master)
    newWindow.title("Station Tilburg")
    newWindow.geometry("720x580")
    Label(newWindow,
          text="Welkom op Station Tilburg!").pack()
    Label(newWindow,
          text=f"{tilburgRes}!",background='white').pack()
    Label(newWindow,
          text=f"{celsiusTi}").pack()



# Functie zorgt ervoor dat er een nieuw venster word geopend zodra gebruiker op 'Groningen' klikt
def groningen():
    newWindow = Toplevel(master)
    newWindow.title("Station Groningen")
    newWindow.geometry("720x580")
    Label(newWindow,
          text="Welkom op Station Groningen!").pack()
    Label(newWindow,
          text=f"{groningenRes}!",background='white').pack()
    Label(newWindow,
          text=f"{celsiusGr}").pack()



# Maak een label aan om te laten zien aan de gebruikers te zien dat de knoppen er zijn om een station te kiezen
label = Label(master,
              text="Kies een station")
label.pack(pady=10)

# Alle knoppen. Deze zorgen ervoor zodra de gebruiker op de knop drukt, de juiste functie word aangeroepen. Elke knop
# bevat ook wat 'Padding' om de uiterlijk wat mooier te maken

btn = Button(master,
             text="Haarlem",
             command=haarlem)
btn.pack(pady=10)

btn = Button(master,
             text="Groningen",
             command=groningen)
btn.pack(pady=10)

btn = Button(master,
             text="Tilburg",
             command=tilburg)
btn.pack(pady=10)

# De mainloop zorgt ervoor dat de Event Loop word gestart zodat de Programma constant actief blijft
mainloop()






