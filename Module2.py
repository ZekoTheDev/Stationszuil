# Importeer 'datetime' module om tijd van goedkeuring vast te stellen.
# Importeer 'psycopg2' module om connectie met PostgreSQL te realiseren.
import datetime
import psycopg2

vastgelegdeTijd = datetime.datetime.now()

# Vul Database Credentials in
connection_string = "host='localhost' dbname='derdedb' user='postgres' password='36802002'"
conn = psycopg2.connect(connection_string)
cursor = conn.cursor()


# Functie zal de csv-bestand inlezen en de moderator vragen om een naam en een email adress. Vervolgens word het bericht
# opgesplitst in verschillende delen, en geplaatst in verschillende variables zodat de goedgekeurde berichten direct
# weggeschreven kunnen worden in de Database.
def berichtKeuren():
    with open('database.csv', 'r+') as database:
        moderatorNaam = input('Wat is uw naam: ')
        moderatorEmail = input('Wat is uw email adress: ')
        moderatorQuery = """INSERT INTO moderator (email, naam)
        VALUES (%s,%s);"""
        cursor.execute(moderatorQuery, (moderatorNaam, moderatorEmail))
        modidQuery = """SELECT moderatorid 
                        FROM moderator
                        ORDER BY moderatorid DESC
                        LIMIT 1;"""
        cursor.execute(modidQuery)
        modid = cursor.fetchall()
        moderatorid = modid[0][0]

        tilburgQuery = """SELECT station_city
                          FROM station_service
                          WHERE station_city = 'Tilburg';"""
        cursor.execute(tilburgQuery)
        tilburgRes = cursor.fetchall()

        groningenQuery = """SELECT station_city
                          FROM station_service
                          WHERE station_city = 'Groningen';"""
        cursor.execute(groningenQuery)
        groningenRes = cursor.fetchall()

        haarlemQuery = """SELECT station_city
                          FROM station_service
                          WHERE station_city = 'Haarlem';"""
        cursor.execute(haarlemQuery)
        haarlemRes = cursor.fetchall()

        DatabaseEntries = database.readlines()
        stationid = 0
        for review in DatabaseEntries:
            bericht = review.split(';')[0]
            berichtdatum = review.split(';')[1]
            berichttijd = review.split(';')[2]
            gebruikernaam = review.split(';')[3]
            station = review.split(';')[4]
            if station.find('Groningen') != -1:
                stationid = groningenRes[0][0]
            elif station.find('Haarlem') != -1:
                stationid = haarlemRes[0][0]
            elif station.find('Tilburg') != -1:
                stationid = tilburgRes[0][0]
            print(f'\n{bericht}')
            beoordeling = input('Bericht Goedkeuren of Afkeuren? \n').lower()
            if beoordeling == 'goedkeuren':
                datumVanBeoordeling = f"{vastgelegdeTijd.year}-{vastgelegdeTijd.month}-{vastgelegdeTijd.day}"
                tijdVanBeoordeling = f"{vastgelegdeTijd.hour}:{vastgelegdeTijd.minute}"

                beoordeling = 'Goedgekeurd'
                print(f"\nReview: {bericht} is Goedgekeurd door {moderatorNaam} \n")

                # Door middel van de 'psycopg2' module kunnen we hier een INSERT query toepassen en de parameters
                # toevoegen die we naar de database gaan schrijven. Bij VALUES vullen we de placeholders '%s' in.
                berichtenQuery = """INSERT INTO berichten (bericht,berichtdatum,berichttijd,naam,beoordeling, beoordelingdatum, beoordelingtijd, moderatorid, station_city)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"""

                # Hier vullen we de daadwerkelijke waardes in die we in de '%s' placeholders willen plaatsen.
                cursor.execute(berichtenQuery, (
                bericht, berichtdatum, berichttijd, gebruikernaam, beoordeling, datumVanBeoordeling, tijdVanBeoordeling,
                moderatorid, stationid))
                conn.commit()

            else:
                print(f"\nReview: {bericht} is Afgekeurd door {moderatorNaam} \n")


berichtKeuren()
