import datetime
import random

stations = ['Groningen', 'Rotterdam', 'Tilburg']
station = random.choice(stations)

naamGebruiker = input('Voer uw naam in (Druk op "Enter" om anoniem door te gaan): ')

if len(naamGebruiker) < 2:
    naamGebruiker = 'Anoniem'

else:
    naamGebruiker = naamGebruiker
 
while True:
    vastgelegdeTijd = datetime.datetime.now()

    bericht = input('Vul uw bericht in (max 140 karakters): ')
    datumVanBericht = f"{vastgelegdeTijd.year}-{vastgelegdeTijd.month}-{vastgelegdeTijd.day}"
    tijdVanBericht = f"{vastgelegdeTijd.hour}:{vastgelegdeTijd.minute}"

    if len(bericht) > 140:
        print('Uw bericht bevat meer dan 140 Karakters')
        continue
    else:
        break

with open('database.txt', 'a+') as database:
    database.seek(0)
    data = database.read(100)
    if len(data) > 0:
        database.write('\n')
    database.write(f'{bericht};{datumVanBericht};{tijdVanBericht};{naamGebruiker};{station}')
    database.close()



        # print(f'Bericht: {bericht}')
        # print(f'Tijdstip: {tijdVanBericht}')
        # print(f'Naam: {naamGebruiker}')
        # print(f'Station: {station}')








