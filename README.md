# QA-DevOps-Fundamental-Project- MCQ App:  
This repository contains my deliverable for the QA devops fundamental project.

## Contents:
* [Project Brief](#Project-Brief)  
* [App Design](#App-Design)
* [CI Pipeline](#CI-Pipeline)  
* [Risk Assessment](#Risk-Assessment)
* [Testing](#Testing)
* [The App](#The-App)
* [Updates](#Updates)
* [Known Issues](#Known-Issues)
* [Future Work](#Future-Work)

## Project Brief:  
The brief for this project was to design and produce a web app of my choosing. The app needed to have CRUD (create, read, update and delete) functionality, needed to use the Flask micro-framework, and had to store information in a MySQL database comprised of a minimum of two tables sharing a one-to-many relationship. This structure is represented below:  

## App Design:
I have chosen to build an app to track players and stats for 5 a side football games.
It allows users to add the list of players playing each game (create functionality), display all the lists (read functionality), update lists of players (update functionality) and delete games (delete functionality).
It also displays stats for each individual player and for the whole group.
The MVP for this project comprises a Matches table and a Players table.
Each match shows the lineup for that game and the date.
The players table shows the number of games played by each player and the date of the first and last game played.
Each match has a captain but every captain can play more than one match (one-to-many relationship).
The ERD for this MVP is shown below:


## Pages:
The main page displays the whole matches table in chronological order with the possibility to filter the games played by a choosen player.
The user can add or edit matches using appropriate forms.
The Stats page displays a list of all players who played at least a game ordered by number of caps
Each player has an individual page displaying his own caps, first and last game.


## Extra functionality
In order to simplify data entry, the 'addgame' page allows to submit a block of text, a function will extract the name of the first 10 player names, dealing with accents, capitalisation, special characters, numbers and spaces within player names (ex: John B, John mc are accepted)

## CI Pipeline:  
In addition to the above requirements, the project required the implementation of several stages of a typical CI pipeline. These were project tracking, version control, development environment and build server. For project tracking Jira was used to create a project tracking board. I created Epics describing biggest tasks or group of issues, each Epic was broken down into user stories, prioritised and moved from project backlog to sprint backlog, to review and then complete as the project progressed. Here there are a couple of examples of the Jira Roadmap during the project:

xxxxxxxxx

For version control, git was used, with the project repository hosted on github. Version control via git allows changes to the project to be made and committed whilst keeping the commit history for access to earlier versions. GitHub as a repository hosting service allows the repository to be stored away from the development environment, as well as providing webhooks, which send http POST requests to the build server to automate building and testing.  

