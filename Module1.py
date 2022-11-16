# Importeer 'datetime' module om tijd van bericht vast te stellen.
# Importeer 'random' module om een willekeurig station te kiezen
import datetime
import random

stations = ['Groningen', 'Haarlem', 'Tilburg']
station = random.choice(stations)
scheldwoorden = ['klootzak','idoot', 'sukkel']

# Functie zal de gebruiker vragen om een naam en een bericht. Zodra het bericht is geschreven word de tijd vastgesteld
# en word de data geschreven naar een csv-bestand. Het bericht mag niet meer dan 140 karakters bedragen.

def reviewSchrijven():
    print('------------------------------------------------------')
    print('Welkom bij NS!')
    print('------------------------------------------------------')
    naamGebruiker = input('Voer uw naam in (Druk op "Enter" om anoniem door te gaan): ')

    if len(naamGebruiker) < 2:
        naamGebruiker = 'Anoniem'

    else:
        naamGebruiker = naamGebruiker

    while True:
        vastgelegdeTijd = datetime.datetime.now()

       
        bericht = input('Vul uw bericht in (max 140 karakters): ')
        # Zoekt of er scheldwoorden aanwezig zijn in het bericht
        for scheldwoord in scheldwoorden:
            if bericht.find(scheldwoord) == -1:
                continue
            else:
                print('Uw maakt gebruik van informele taalgebruik. Voer een nieuwe bericht in!')
                break
        datumVanBericht = f"{vastgelegdeTijd.year}-{vastgelegdeTijd.month}-{vastgelegdeTijd.day}"
        tijdVanBericht = f"{vastgelegdeTijd.hour}:{vastgelegdeTijd.minute}"

        if len(bericht) > 140:
            print('Uw bericht bevat meer dan 140 Karakters')
            continue
        else:
            break

    with open('database.csv', 'a+') as database:
        database.seek(0)
        data = database.read(100)
        if len(data) > 0:
            database.write('\n')
        database.write(f'{bericht};{datumVanBericht};{tijdVanBericht};{naamGebruiker};{station}')
        database.close()


reviewSchrijven()
