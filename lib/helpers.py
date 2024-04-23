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
    try:
        race_name = input("Enter the name of the race to add the athlete to: ")
        race = Race.find_by_name(race_name)
        if race:
            name = input('Enter athlete name:  ')
            age = int(input('Enter athlete age:  '))
            gender = input('Enter gender; M or F:  ')
            athlete = Athlete.create(name, age, gender, race.id)
            if athlete:
                print(f'Athlete {athlete.name} succesfully added to race {race.name}.')
            else:
                print('Failed to add athlete')
        else:
            print('Race not found. Please enter a valid race name')
    except ValueError as ve:
        print('Error: Invalid input. Please enter a valid age')
    except Exception as exc:
        print('Error adding athlete:', exc)
       # athlete = Athlete.create(name, age, gender, race_id)
       # print(athlete) if athlete else None
    #except Exception as exc:
        #print ('Error adding athlete:  ', exc)

def add_race():
    print('')
    name = input('Enter race name:  ')
    race_type = input ('Enter race type; bike, run, swim:  ')
    distance = float(input('Enter race distance in miles:  '))
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
    race_name = input("Enter the name of the race: ")
    race = Race.find_by_name(race_name)
    
    if race:
        athletes = Athlete.get_all(race.id)
        if athletes:
            print(f"Athletes participating in race {race_name}:")
            for athlete in athletes:
                print(athlete)
        else:
            print("No athletes found for the specified race.")
    else:
        print(f"No race found with the name '{race_name}.")
        print("If you'd like to add a race, select '3'.")


def delete_athlete():
    print('')
    name= input("Enter the athlete's name: ")
    athlete = Athlete.find_by_name(name)
    if athlete:
        athlete.delete()
        print(f'Athlete {name} deleted')
    else:
        print(f'Athlete {name} not found')
    

def delete_race():
    print('')
    name= input("Enter the race name: ")
    race = Race.find_by_name(name)
    if race:
        race.delete()
        print(f'Race {name} deleted')
    else:
        print(f'Race {name} not found')
    
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
    name = input("Enter the athlete name: ")
    athlete = Athlete.find_by_name(name)
    if athlete:
        try:
            new_name = input('Enter the athlete new name: ')
            athlete.name = new_name
            age = (int(input('Enter the athlete age: ')))
            athlete.age = age
            gender = input('Enter the athlete gender; M or F: ')
            athlete.gender = gender
            new_race_name = input('Enter the athlete race name: ')
            new_race = Race.find_by_name(new_race_name)
            if new_race:
                athlete.race_id=new_race.id
            else:
                print(f'Race {new_race_name} not found.')
                return
            
            
            



            athlete.update()
            print(f'Success: {athlete}')
        except Exception as exc:
            print('Error updating athlete: ',exc)
    else:
        print(f'Athlete {name} not found')

def update_race():
        print('')
        name= input("Enter the race name: ")
        if race := Race.find_by_name(name):
            try:
                new_name = input('Enter the race new name: ')
                race.name = new_name
                race_type = input('Enter the race type; run, bike, or swim: ')
                race.race_type = race_type
                distance = float(input('Enter the race distance in miles: '))
                race.distance = distance
                

                race.update()
                print(f'Success: {race}')
            except Exception as exc:
                print('Error updating race: ',exc)
        else:
            print(f'Race {name} not found')
