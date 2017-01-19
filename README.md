[![Build Status](https://travis-ci.org/hollabaq86/haikuna-matata.svg?branch=master)](https://travis-ci.org/hollabaq86/haikuna-matata)

# Haikuna-Matata
---
## A Machine Learning Haiku Generator

### A project developed by Holly Stotelmyer (@hollabaq86), Noah Guy (@NoahRGuy), Dennis Marchetti (@dmarchet) and Joan Petersohn (@jepetersohn)


## Description
---

Haikuna-Matata generates completely original, correctly formatted haikus based on user input. A user types an input word into the console when running the program, and the program will return a 5/7/5 style haiku concerning whatever input the user put in.  Haikus will meet the following requirements, moving from Basic to Advanced as the program learns over time.

Basic Haiku Requirements
---
All Haikus are defined by the following structure
* Each haiku has 3 lines.
* Each haiku follows the following syllable construction for each line
* 5 syllables for the first line
* 7 syllables for the second line
* 5 syllables for the third line

Intermediate Haiku Requirements
---
All Haikus must
* Be centered around a user provided word, or given no user input, centered around a randomly generated word
* Have no line ending in a preposition

Advanced Haiku Requirements
---
Stretch Goals for the machine to learn
* Haikus must make sense.
* All haikus will follow proper grammatical structure.

## Installation & Usage
---
[Python 2.7](https://www.python.org/downloads/) is required to run this program. If your computer does not use Python yet, click the link and download Python 2.7 before attempting to run this program.

To use this program, simply clone the repository to your computer and navigate to its directory.

A virtual development environment has been set up for this project, which has all of the current and needed versions of all modules needed to run the program.  To install virtualenv on your machine, enter the following.

```
$ pip install virtualenv
```

You can now enter the following from the terminal to load the pre-defined environment and set all necessary environment variables.

```
$ source env/bin/activate
$ export APP_SETTINGS="config.DevelopmentConfig"
$ export DATABASE_URL="postgresql://localhost/haiku"
```

To return to the normal world and exit the virtual environment, simply enter "deactivate" in the terminal.  Whenever you are ready to do more work on this project, you just need to reload the virtualenv, which can be done by re-entering the above commands.

In order for this program to function, you will need to create a local database on your machine, and seed it with text......a lot of text.  This database is used by the haiku algorithm as its reference to the english language and helps it put together proper sentence structure.  In order to create the database, enter the following.

```
$ psql
# create database haiku;
# \q
$ python manage.py db upgrade
```

Now that your local developement database is set up, you simply need to seed it.  You will need to create some sample text for your database (in .txt files) which you can put in the example_poetry folder.  Then put your text file path into the "files" variable at the bottom seed_database.py.  Then just run the following from the command line, and your database will be up and running!

```
$ python seed_database.py
```

To open the web page locally, simply launch the app.py file:

```
$ python app.py
```

Navigate to http://localhost:5000/.  There you can enter in a word and Haikuna Matata will generate a haiku for you

```
Haiku (Created by Haikuna Matata):
This is a sample
Haiku made all by myself
Bask in its glory
```

To close your local server, type CTRL+C

