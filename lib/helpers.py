# lib/helpers.py

from models.athlete import Athlete
from models.race import Race

def view_all_athletes():
    print('')
    athletes = Athlete.get_all()
    for athlete in athletes:
        print(athlete)


def exit_program():
    print("Goodbye!")
    exit()

def add_athlete():
    print('')
    name = input('Enter athlete name:  ')
    age = int(input('Enter athlete age:  '))
    gender = input('Enter gender; M or F:  ')
    race_id = int(input('Enter the race:  '))
    try:
        athlete = Athlete.create(name, age, gender, race_id)
        print(athlete) if athlete else None
    except Exception as exc:
        print ('Error adding athlete:  ', exc)

def add_race():
    print('')
    name = input('Enter race name:  ')
    race_type = input ('Enter race type; bike, run, swim:  ')
    distance = input('Enter race distance in miles:  ')
    try:
        race = Race.create(name, race_type, distance)
        print(race) if race else None
    except Exception as exc:
        print('Error adding race: ', exc)

def find_athlete_by_name():
    print('')
    name = input("Enter name of athlete: ")
    athlete = Athlete.find_by_name(name)
    if athlete:
        print("Athlete found")
        print(athlete)
    else:
        print("Athlete not found.")


def view_all_races():
    print('')
    races = Race.get_all()
    for race in races:
        print(race)

def view_athletes_in_race():
    print('')
    race_id = input("Enter the ID of the race: ")
    athletes = Athlete.get_all(race_id)
    if athletes:
        print(f"Athletes participating in race with ID {race_id}:")
        for athlete in athletes:
            print(athlete)
    else:
        print("No athletes found for the specified race.")


def delete_athlete():
    print('')
    id_= input("Enter the athlete's id: ")
    if athlete := Athlete.find_by_id(id_):
        athlete.delete()
        print(f'Athlete {id_} deleted')
    else:
        print(f'Athlete {id_} not found')
    

def delete_race():
    print('')
    id_= input("Enter the race id: ")
    if race := Race.find_by_id(id_):
        race.delete()
        print(f'Race {id_} deleted')
    else:
        print(f'Race {id_} not found')
    
def find_race_by_type():
    print('')
    race_type = input('Enter race type; run, bike, swim: ')
    race = Race.find_by_race_type(race_type)
    if race:
        print("Race found")
        print(race)
    else:
        print("Error finding race, try again.")
    

def update_athlete():
    print('')
    id_= input("Enter the athlete id: ")
    if athlete := Athlete.find_by_id(id_):
        try:
            name = input('Enter the athlete new name: ')
            athlete.name = name
            age = input('Enter the athlete age: ')
            athlete.age = age
            gender = input('Enter the athlete gender; M or F: ')
            athlete.gender = gender
            athlete_id = input("Enter the athlete new ID: ")
            athlete.id = athlete_id

            athlete.update()
            print(f'Success: {athlete}')
        except Exception as exc:
            print('Error updating athlete: ',exc)
        else:
            print(f'Athlete {id_} not found')

def update_race():
        print('')
        id_= input("Enter the race id: ")
        if race := Race.find_by_id(id_):
            try:
                name = input('Enter the race new name: ')
                race.name = name
                race_type = input('Enter the race type; run, bike, or swim: ')
                race.race_type = race_type
                distance = input('Enter the race distance in miles: ')
                race.distance = distance
                

                race.update()
                print(f'Success: {race}')
            except Exception as exc:
                print('Error updating race: ',exc)
            else:
                print(f'Race {id_} not found')
