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
  
  
 F) ScreenShots of the Project :
 
 ***PS: The UI is Pretty basic***
 1) Landing Page : 
 ![image](https://user-images.githubusercontent.com/77016507/205308200-0144c6ec-fe45-46a5-af41-21961db0b1fb.png)
 
2) Admin Page to Add Poll Questions and Choices
  a) HomePage :
  ![image](https://user-images.githubusercontent.com/77016507/205308836-78adb960-01e3-44bf-9dfe-93c70b47ee22.png)
  
  b) Add Question :
  ![image](https://user-images.githubusercontent.com/77016507/205309026-14d8e62e-4bc4-4b7f-b43d-92992e9d63ba.png)
  
  c)Add Choices :
  ![image](https://user-images.githubusercontent.com/77016507/205309151-2bf4789f-1399-4469-8f88-e87e4eadc2a2.png)

3) Polls Homepage for User :
![image](https://user-images.githubusercontent.com/77016507/205308579-643c32cc-18a0-4908-908b-816edcf6b8a4.png)

4) Voting Page For a Question :
![image](https://user-images.githubusercontent.com/77016507/205308654-1aa1fd9a-1790-4688-9f50-c0c67e764831.png)

5) After Successful Voting :
![image](https://user-images.githubusercontent.com/77016507/205308742-91036ded-8179-4ab9-9ba5-2dc1843181e8.png)

G) MySQL Migrations :
  
  ![image](https://user-images.githubusercontent.com/77016507/205309584-d5c12f81-c667-4b93-a825-a68d623a4f7e.png)
