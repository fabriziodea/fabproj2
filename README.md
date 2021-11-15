# QA-DevOps-Fundamental-Project- MCQ App:  
This repository contains my deliverable for the QA devops fundamental project.

## Contents:
* [Project Brief](#Project-Brief)  
* [App Design](#App-Design)
* [CI Pipeline](#CI-Pipeline)  
* [Risk Assessment](#Risk-Assessment)
* [Testing](#Testing)


## Project Brief:  
The brief for this project was to design and realise a web app of my choosing. The app needed to have CRUD (create, read, update and delete) functionality, to use the Flask micro-framework, and had to store information in a MySQL database comprised of a minimum of two tables sharing a one-to-many relationship. 

## App Design:
I have chosen to build an app to track players and stats for 5 a side football games.
It allows users to add the list of players playing each game (create functionality), display all the lists (read functionality), update lists of players (update functionality) and delete games (delete functionality).
It also displays stats for each individual player and for the whole group.
The MVP for this project comprises a Matches table and a Players table.
Each match shows the lineup for that game and the date.
The players table shows the number of games played by each player and the date of the first and last game played.
Each match has a man of the match (Player1) but every player can be the man of the match of multiple games (one-to-many relationship).
The ERD for this MVP is shown below:

![app structure](https://github.com/fabriziodea/fabproj1/blob/master/Images/ERD.png)


## Pages:
The main page displays the whole matches table in chronological order with the possibility to filter the games played by a choosen player.
The user can add or edit matches using appropriate forms.
The Stats page displays a list of all players who played at least a game ordered by number of caps
Each player has an individual page displaying his own caps, date of first and last game played.


## Extra functionality
In order to simplify data entry, the 'addgame' page allows to submit a block of text, a function will extract the names of the 10 players dealing with accents, capitalisation, special characters, numbers and spaces within player names (ex: John B, John mc are accepted)

## CI Pipeline:  
In addition to the above requirements, the project required the implementation of several stages of a typical CI pipeline. These were project tracking, version control, development environment and build server. For project tracking Jira was used to create a project tracking board. I created Epics describing biggest tasks or group of issues, each Epic was broken down into user stories, prioritised and moved from project backlog to sprint backlog, to review and then complete as the project progressed. Here there are a couple of examples of the Jira Roadmap during the project:

![Jira Board1](https://github.com/fabriziodea/fabproj1/blob/master/Images/Jira%20Board.png)
![Jira Roadmap1](https://github.com/fabriziodea/fabproj1/blob/master/Images/Jira%20Roadmap1.png)
![Jira Roadmap2](https://github.com/fabriziodea/fabproj1/blob/master/Images/Jira%20Roadmap2.png)


For version control, git was used, with the project repository hosted on github. Version control via git allows to store code in a central repository, track changes over time and create branches so that additions are made in isolation from stable code. GitHub as a repository hosting service allows the repository to be stored away from the development environment, as well as providing webhooks, which send http POST requests to the build server to automate building and testing.  
Furthermore smart commits were used to automatically move user stories in the Jira board in the appropriate state (To do - In Progress - Done). Here a few examples of smart commits:

![Smart commits](https://github.com/fabriziodea/fabproj1/blob/master/Images/Smart%20Commits.png)

Here github shows the progress of commits on features branches:

![Git Branches](https://github.com/fabriziodea/fabproj1/blob/master/Images/Branches%202.png)

Jenkins was used as a build server, providing automation of building and testing. This automation is achieved by setting up a freestyle project which executes the deploy.sh script when it recieves a webhook from github upon pushing a commit. Jenkins is also used to run the app via gunicorn once testing is complete. Gunicorn is a WSGI server which allows multiple processes to run the app simultaneously.


## Risk Assessment:
Prior to building the app, a risk assessment was undertaken to identify risks and propose measures to control these risks. These measures could then be implemented in the app. This initial risk assessment is shown below:   

![Risk Assessment](https://github.com/fabriziodea/fabproj1/blob/master/Images/RiskAssessment.png)


Some of the control measures implemented in the project as a result of the risk assessment are as follows:  
* SQLAlchemy was used with Flask to prevent SQL commands being sent directly to the database.  
* Credentials stored as secret texts on Jenkins VM and exported as environment variables to avoid accidentally publishing confidential details.  

## Testing:  
Testing the app was an essential part of the development process. Unit testing tests _units of functionality_ (i.e functions) within the app. Unit tests were written for create, read, update and delete functionality, to ensure that these worked as intended.

As this is not a production app, tests such as security tests and performance tests were not part of the scope of this project; only testing for functionality was performed. These tests are automated using Jenkins via webhooks. A successful build, in which all tests passed, is shown below:  

![Jenkins](https://github.com/fabriziodea/fabproj1/blob/master/Images/Jenkins1511.png)

The coverage reports, showing what percentage of statements were included in the tests, were output as html files, which were archived post-build. The coverage report for the above build was:  

![Coverage Report](https://github.com/fabriziodea/fabproj1/blob/master/Images/CovReport1511.png)

Showing 98% coverage overall. All tests must pass for a build to be successful, a single failed test marks the build overall as failed.
