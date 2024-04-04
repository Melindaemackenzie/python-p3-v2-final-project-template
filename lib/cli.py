# lib/cli.py

from helpers import (
    exit_program,
    view_all_runners,
    view_all_races,
    find_runner_by_id,
    add_runner,
    add_race,
    delete_runner,
    delete_race,
    find_race_by_distance,
    find_runner_by_gender
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            view_all_runners()
        elif choice == "2":
            view_all_races()
        elif choice == "3":
            find_runner_by_id()
        elif choice == "4":
            add_runner()
        elif choice == "5":
            add_race()
        elif choice == "6":
            delete_runner()
        elif choice == "7":
            delete_race()
        elif choice == "8":
            find_race_by_distance()
        elif choice == "9":
            find_runner_by_gender()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. View all runners")
    print("2. View all races")
    print("3. Find Runner By ID")
    print("4. Add runner")
    print("5. Add race")
    print("6. Delete runner")
    print("7. Delete race")
    print("8. Find race by distance")
    print("9. Find runner by gender")


if __name__ == "__main__":
    main()
