# Phase 3 python comand line project Notes

## Projects Requirements
- [Project Requirements](https://my.learn.co/courses/653/pages/phase-3-project-cli?module_item_id=95439)

## TO DO LIST
    [] Models
        [] Artist
        [] Songs
    [] SQLAlchemy migrations
        []
        []
    [] Building CLI
        []
        []
Instructions
Welcome to the end of Phase 3! You've learned about a lot in this unit:

Python fundamentals.
Data structures (and more recently, algorithms).
Object-oriented programming.
Object inheritance.
Class attributes and methods.
Configuring applications.
SQL fundamentals.
Table relations in SQL.
Object-relational mapping with Python.
Object-relational mapping with SQLAlchemy.
Building CLIs.
In this project, we're going to use these skills to create a CLI. You won't be able to fit everything in from phase 3, but the following are the minimum requirements:

### The minimum requirements

[ ]A CLI application 
- - that solves a real-world problem
- - adheres to best practices.

[ ] A database created with SQLAlchemy ORM
- - modified with SQLAlchemy ORM 
- - with 2+ related tables.

[ ] A well-maintained virtual environment using Pipenv.

[ ] Proper package structure in your application.

[ ] Use of lists and dicts.


### Stretch goals
A database created and modified with SQLAlchemy ORM with 3+ related tables.
Use of many-to-many relationships with SQLAlchemy ORM.
Use of additional data structures, such as ranges and tuples.

### Project rebric 
a. This criterion is linked to a Learning OutcomeBuild classes using OO Python Syntax - 5 pts.
Correct class syntax for all of the submitted code. Code express intent: method and variable names indicate their behavior and data types. Follows DRY principles and reuses code where applicable.

b. This criterion is linked to a Learning OutcomeObject Relationship Methods - 5 pts.
Relationships properly created. Uses all correct SQLAlchemy methods, and has foreign keys on the correct tables. Uses relationship methods to solve other deliverables.

c. Aggregate and Association Methods - 5 pts.
All aggregate and association methods are implemented and function correctly. Most use appropriate SQLAlchemy built-in methods where applicable, rather than using Python iteration.

d. This criterion is linked to a Learning OutcomeData Structures - 5 pts. 
Lists and dictionaries used appropriately, as well as other data structures if applicable such as tuples or sets. Uses list comprehensions as appropriate.

e. This criterion is linked to a Learning OutcomePipenv - 5pts
Pipfile included and contains all used dependencies in the project. No unused dependencies are listed in the Pipfile. Project runs properly upon set up of virtual environment.

f. This criterion is linked to a Learning OutcomeCommit History (50) - 5 pts.

g. This criterion is linked to a Learning OutcomeDemo Video and README - 5 pts. 
README and Demo Video both present and following best practices. README contains all necessary items (project name, description, installation instructions, brief description of how to use your app, a Contributor's Guide, and a License). Demo video is 3 minutes or less in length and provides a nontechnical demo of app features.

h. This criterion is linked to a Learning OutcomeProject Turned in on Time (8/27/2023) 5 pts 


### PROJECT PROPOSALS
- Main idea: <Enter the title and main idea of your app>

### User story: 
-   Pull up a list of songs 
-   Pull up a list of artists
-   See a list of favorites songs
-   Remove a song from the list

### How I will use the concepts I recently learned to meet the project requirements: 
- Object Oriented Python 
    - Class for Songs
    - Class for Artists

- Database Tables 
    - Describe how you will use SQLAlchemy to create and interact with 2 or more related database tables
        - Table: Songs
            - Atrist id (INTEGER FOREIGN KEY) 
            - title (STRING NOT NULL UNIQUE)
            - category (STRING NOT NULL UNIQUE)
        - Table: Artists
            - id (INTEGER PRIMARY KEY)
            - name (STRING NOT NULL UNIQUE)
            - nationality (STRING NOT NULL UNIQUE)
        - Table: (One-to-Many) Artist => Songs == "List of favorite songs by an artist"
            - ID
            - song ID
            - Artist ID

- Object Relationships 
     - Describe the types of relationships your different classes and tables will have with each other
     - Artist can have many songs
     - Many songs can be put in a favorite list
- Aggregate and Association Methods 
    - Describe a few of the methods you plan on including in your application to query your database
        -   List all Songs
            - Create
                - Create a list of songs
                - Create a list of Artists
            - Read
                - Display all Songs
                - Display all Artists
            - Update
                - Change the title of a song
            - Delete
                - Remove a song from the list
        -   List all Artists
- Use of Data Structures 
    - Describe how you plan on using data structures like lists and dictionaries in your project
        - LIST: A list of songs as ID's
        - DICTIONARY: Each song has a set of Attributes and values
- What area I think will be most challenging
    - Describe which aspect of the project you think will present the greatest challenge, or the topic that you feel least familiar with at present.