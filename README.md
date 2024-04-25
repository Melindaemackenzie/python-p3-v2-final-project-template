# EVENT MANAGER README

## INTRO

'EVENT MANAGER' is a Python CLI application created to manage various athletic events and participating athletes. 

## USE

Users are able to interact with the DB of athletes and events, creating events, and athletes as well as updating 
exisiting athletes and events. At this time, athletes are only able to participate in one athletic event. Type 
and distance of event will be listed along with name. Users are able to do view all athletes, search by name, 
update, add, and remove athletes. Users are also able to view all races, search race by type, view all athletes 
in specific race, update, add, and remove a race. 

## BRIEF WALK THROUGH

Directory structure is as follows:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   └── athlete.py
    │   └── race.py
    ├── cli.py
    ├── debug.py
    └── helpers.py
    └── seed.py
    
```


Upon opening the CLI, users will be greeted with a simple "main menu"

<img width="188" alt="Screen Shot 2024-04-24 at 6 46 30 PM" src="https://github.com/Melindaemackenzie/python-p3-v2-final-project-template/assets/89819551/bac4521c-61ee-49f0-9bad-10a3805e4925">

Users are then prompted to make their selection (1, or 2) to enter the desired menu.

Race Management Menu and Athlete Management Menu are as follows: 

<img width="229" alt="Screen Shot 2024-04-24 at 6 59 26 PM" src="https://github.com/Melindaemackenzie/python-p3-v2-final-project-template/assets/89819551/4e37c2f5-1f95-4d47-a15f-30c977bb5cfd">


<img width="255" alt="Screen Shot 2024-04-24 at 7 00 02 PM" src="https://github.com/Melindaemackenzie/python-p3-v2-final-project-template/assets/89819551/9f20c16b-053b-4e6a-8583-f47ab22ddab4">

Users may navigate into either menu based on their selections and follow simple prompts from there to interact with their events and athletes.



## SUMMARY
'EVENT MANAGER' is a user friendly tool developed to help to organize your next athletic event.





Happy coding!

---

## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
