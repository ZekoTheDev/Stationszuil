import datetime
import psycopg2

vastgelegdeTijd = datetime.datetime.now()
connection_string = "host='localhost' dbname='StationZuil' user='postgres' password='36802002'"
conn = psycopg2.connect(connection_string)
cursor = conn.cursor()

with open('database.txt', 'r+') as database:
    moderatorNaam = input('Wat is uw naam: ')
    moderatorEmail = input('Wat is uw email adress: ')
    DatabaseEntries = database.readlines()
    stationid = 0
    for review in DatabaseEntries:
        bericht = review.split(';')[0]
        berichtdatum = review.split(';')[1]
        berichttijd = review.split(';')[2]
        naam = review.split(';')[3]
        station = review.split(';')[4]
        if station.find('Groningen') != -1:
            stationid = 1
        elif station.find('Rotterdam') != -1:
            stationid = 2
        elif station.find('Tilburg') != -1:
            stationid = 3
        print(f'\n{bericht}')
        beoordeling = input('Bericht Goedkeuren of Afkeuren? \n').lower()
        if beoordeling == 'goedkeuren':
            datumVanBeoordeling = f"{vastgelegdeTijd.year}-{vastgelegdeTijd.month}-{vastgelegdeTijd.day}"
            tijdVanBeoordeling = f"{vastgelegdeTijd.hour}:{vastgelegdeTijd.minute}"


            beoordeling = 'Goedgekeurd'
            print(f"\nReview: {bericht} is Goedgekeurd door {moderatorNaam} \n")
            query = """INSERT INTO berichten (bericht, berichtdatum, berichttijd, naam, 
            beoordeling, beoordelingdatum, beoordelingtijd, stationid)
            
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"""
            cursor.execute(query, (bericht,berichtdatum,berichttijd,naam,beoordeling,
                                   datumVanBeoordeling, tijdVanBeoordeling, stationid))
            conn.commit()

        else:
            print(f"\nReview: {bericht} is Afgekeurd door {moderatorNaam} \n")