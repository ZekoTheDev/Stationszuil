import datetime
vastgelegdeTijd = datetime.datetime.now()


with open('database.csv', 'r+') as database:
    moderatorNaam = input('Wat is uw naam: ')
    moderatorEmail = input('Wat is uw email adress: ')
    DatabaseEntries = database.readlines()
    for review in DatabaseEntries:
        print(f'\n{review}')
        status = input('Bericht Goedkeuren of Afkeuren? \n')
        if status == 'Goedkeuren':
            print(f"\nReview: {review} is Goedgekeurd door {moderatorNaam} \n")
        else:
            print(f"\nReview: {review} is Afgekeurd door {moderatorNaam} \n")