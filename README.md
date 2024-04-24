# EVENT MANAGER READEME

INTRO

'EVENT MANAGER' is a Python CLI application created to manage various athletic events and participating athletes. 

USE

Users are able to interact with the DB of athletes and events, creating events, and athletes as well as updating 
exisiting athletes and events. At this time, athletes are only able to participate in one athletic event. Type 
and distance of event will be listed along with name. Users are able to do view all athletes, search by name, 
update, add, and remove athletes. Users are also able to view all races, search race by type, view all athletes 
in specific race, update, add, and remove a race. 

BRIEF WALK THROUGH

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





SUMMARY
'EVENT MANAGER' is a user friendly tool to organize your next athletic event.



  


---

## Updating README.md

`README.md` is a Markdown file that should describe your project. You will
replace the contents of this `README.md` file with a description of **your**
actual project.

Markdown is not a language that we cover in Flatiron's Software Engineering
curriculum, but it's not a particularly difficult language to learn (if you've
ever left a comment on Reddit, you might already know the basics). Refer to the
cheat sheet in this assignments's resources for a basic guide to Markdown.

### What Goes into a README?

This README serves as a template. Replace the contents of this file to describe
the important files in your project and describe what they do. Each Python file
that you edit should get at least a paragraph, and each function should be
described with a sentence or two.

Describe your actual CLI script first, and with a good level of detail. The rest
should be ordered by importance to the user. (Probably functions next, then
models.)

Screenshots and links to resources that you used throughout are also useful to
users and collaborators, but a little more syntactically complicated. Only add
these in if you're feeling comfortable with Markdown.

---

## Conclusion

A lot of work goes into a good CLI, but it all relies on concepts that you've
practiced quite a bit by now. Hopefully this template and guide will get you off
to a good start with your Phase 3 Project.

Happy coding!

---

## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
