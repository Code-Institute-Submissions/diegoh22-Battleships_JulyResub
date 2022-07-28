# Battleship is a terminal game programed with Python, which runs in the Code Institute mock terminal on Heroku.

## Battleship is a funny and a widely-known board game in which the goal is to destroy the opposing player's fleet. It all depends on the luck of your finding shots to initially hit your targets.

# Single Battleships
![Capture](https://user-images.githubusercontent.com/83575427/181646108-e9445c9f-407b-49dc-a9f5-3ed8954e12dc.JPG)

### The computer place 5 ships randomly in both board and you will have to sunk the 5 ships before the 10 tunrs are over!
## ENjoy.
https://single-battleships.herokuapp.com/

# How to play
### In this version of Battleship the user starts the game by first typing the size of the grid they would like to play on. By typing in the name of the player, the game will then fire on and the user will have the ability to strike their first move by guessing and calling out coordinates to find out the computer ships and sink them. The game will randomly generate and populate 5 ships on each board. The grid always start on: 0 row and 0 columns. Guesses are marked on the board with an X and hits are marked by * . To gain a win, you have to sink all the computer's ships before your run out of tunrs or the computer sunk all your ships

# Features
![startgame](https://user-images.githubusercontent.com/83575427/181641997-dd07e999-cb15-4778-89ce-472b6455b5d4.JPG)

## Exiting Features
![Boards](https://user-images.githubusercontent.com/83575427/181642040-04b4bdda-4114-4ac3-baa6-a893f0e5b3dd.JPG)
![guesees](https://user-images.githubusercontent.com/83575427/181642068-153e3b63-c4e1-44b9-838d-40e285100361.JPG)
![endgame](https://user-images.githubusercontent.com/83575427/181642077-b023ec12-e653-47c7-b09a-c64558a10ab6.JPG)
### Randon 


Board Generation
  ### Ships are place randomly by the computer
  ### Scoring system and Turns sytem.
# Input validation and errors-cheking
  ### you must enter A colunm and a row both with number from 0 to 9
  ### you cannot enter the same guess twice
  ### nothing outside the grid of 9

# Furture Features
  ### count down timer
  ### Ships larger than 1x1
  ### music in the Game

# Data Model
# I decided to use two classes for the game model. One Board class and one Game class.

# Board Class

#### self.size = To set the board size
#### self.num_ships = To set number of ships in-game
#### self.player = Bolian indicate if the board belongs to a player or computer
#### self.guesses = List of passed guesses
#### self.populate = Creates in-memory board with the players ship
# Game Class

### self.size = To set the board size
### self.num_ships = To set number of ships in-game
### self.scores = Set score when ship is sunk

# Testing
  #### Passed the code through a PEP* linter and confirmed there no problems
  ### Tested in my local terminal and the code isntitute Heroki terminal

# Bugs
 ### Still a bug went you run the debugging the system stops on the name input part, i could find the way to fix that bug.


# Remaining Bugs

 ### No remainding bugs in this code


# Valitor Testing 
  ### PeP8
  ### No errors

![Pip8](https://user-images.githubusercontent.com/83575427/181643364-448aaaa0-3323-45ee-8ed2-734fac510282.JPG)

# Languages, Frameworks, IDE, Libraries and Programs
 # Python:

### The programming language Python was used.
  # Python random library:

### random.randint was used to generate random integer numbers in the game.
# GitHub:

### GitHub was used to store the projects code after being pushed from Git.

# Gitpod:

### Was used to complement the development and write my project and push all commits through integrated "git" to Github.
# Heroku:

#### Was used for deployment of the project live in the cloud.
# Deployment
### This project was published and deplyed using the Code Institute mock teminal for Heroku
### Steps for deployment:
### Fork or clone this repository
### Create a new Heroku application
#### Set the buildpack in the setting to "heroku/python" and "heroku/nodejs"
#### In the "Deploy" menu chose "Deployment method" GitHub
### Connect and choose the repository in the "App connected to GitHub"
### Choose either "Automatic deployment" = which means that every push to the branch you specify will deploy a new version of this app
### "Manual deploy" = this will deploy the current state/version of the branch

## The live link can be found here -https://single-battleships.herokuapp.com/

# Credits
### Code Institute idea from Project Portfolio 3 
### Code Institute project 3 Scope video
### To all code institute Studen support
