# Polls App

The project uses Django Framework in Python and MySQL as database. 

A) The Project Contains 2 Apps :
  1. The Main Polls App.
  2. A Landing Page for the user on launching the server.

B) The Following views have been created in the Polls App:
  1. Home Page (named home)
  2. Detail Page (A page containing detailed description of Every Question)
  3. Results Page (Live Detail of which options of particular question has how many votes)
  4. Vote (To record the Selected Choice)
 
 C) The Following Classes are created for Polls App :
  1. Question (Contains the Question Text [255 charecters] and Date Published)
  2. Choice (Contains Question ID [Foreign Key Reference], Text [255 chars], Votes [No. of Votes for the particular choice])
  
 D) Through Admin.py, Django Default UI has been enabled and can be used to Feed New Questions and Choices
  
 E) Templates have been written in HTML for Landing Page, Polls HomePage, Detail Page, and Results Page
