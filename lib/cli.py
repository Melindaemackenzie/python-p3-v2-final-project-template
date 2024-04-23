# lib/cli.py

from models.athlete import Athlete
from models.race import Race

from helpers import (
    exit_program,
    view_all_athletes,
    view_athletes_in_race,
    view_all_races,
    find_athlete_by_name,
    add_athlete,
    add_race,
    delete_athlete,
    delete_race,
    find_race_by_type,
    update_athlete,
    update_race
)


class Main():

    def display_main_menu(self):
        print('\nEvent Manager')
        print('1. Manage Athletes')
        print('2. Manage Races')
        print('3. Quit')

    def display_athlete_menu(self):
        print('\n Athlete Management Menu')
        print('1.View all athletes')
        print('2. Update an athlete')
        print('3. Add an athlete')
        print('4. Remove athlete')
        print('5. Find athlete by name')
        print('6. Back to Event Manager Menu')

    def display_race_menu(self):
        print('\nRace Management Menu')
        print('1. View all races')
        print('2. Update a race')
        print('3. Add a race')
        print('4. Remove a race')
        print('5. Find race by type')
        print('6. View all athletes in race')
        print('7. Exit back to Event Manager Menu')

    def run(self):
        while True:
            self.display_main_menu()
            choice = input('Enter choice: ')
            if choice == '1':
                self.athlete_management()
            elif choice == '2':
                self.race_management()
            elif choice == '3':
                print('Exiting event manager..')
                exit_program()
            else:
                print('Invalid choice. Please select another.')

    def athlete_management(self):
         while True:
            self.display_athlete_menu()
            choice = input('Enter choice: ')
            if choice == '1':
                view_all_athletes()
            elif choice == '2':
                view_all_athletes()
                update_athlete()
            elif choice == '3':
                view_all_races()
                print('If race does not exist, add race in Race Management Menu')
                add_athlete()
            elif choice == '4':
                view_all_athletes()
                delete_athlete()
            elif choice == '5':
                find_athlete_by_name()
            elif choice == '6':
                break
            else:
                print('Invalid choice, try again.')

    def race_management(self):
        while True:
            self.display_race_menu()
            choice = input('Enter choice:  ')
            if choice == '1':
                view_all_races()
            elif choice == '2':
                view_all_races()
                update_race()
            elif choice == '3':
                add_race()
            elif choice == '4':
                view_all_races()
                delete_race()
            elif choice == '5':
                find_race_by_type()
            elif choice == '6':
                view_all_races()
                view_athletes_in_race()
            elif choice == '7':

                    break
            else:
                    print ('Invalid choice, try again.')

  

if __name__ == "__main__":
    cli = Main()
    cli.run()
