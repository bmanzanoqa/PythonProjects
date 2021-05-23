# MINI BLOCKS EXHIBITION APP


## Contents
* [Summary](#Summary)
   * [History](#my-approach)
   * [Project Requirements](#project-requirements)
* [Project Tracking](#project-tracking)
* [Databases Structure](#database-structure)
* [Risk Assessment](#risk-assessment)
* [CI Pipeline](#ci-pipeline)


* [Testing](#testing)
* [Front-End Design](#front-end-design)
* [Known Issues](#known-issues)
* [Future Improvements](#future-improvements)
* [Authors](#authors)

## Summary
### History
```
I love building 'stuff' with microblock pieces. My project is based in the idea of having an APP where I can store the items I build and the rooms (called Exhibitions) where they will be displayed.  I wanted to have a login page where user(other than me, ie, my children) could create a new account or login. Once I had login I would be taken to a page where I would have the options of Items and Exhibitions. In any of these options, once I clicked on them, I would be presented with a selection of CRUD(create, Read, Update,Delete) options. This was more difficult than anticipated so I went for a simpler version.
```
So.... the simpler version:
```
The app offers you the option to create, Read, Update and Delete (CRUD) items and Exhibitions (Items are the things I built and Exhibitions the rooms where they will be display). 
The app is run on a database where the tables have a one to many relationships.
```
### Project Requirements
The objective of this project is to create a CRUD application with utilisation of supporting tools, such as:
- Jira board to cover the project management side of it
- A relational databases with at least 2 tables, showing the relationship between them
- A README.md document explaining the basis and architecture of this project
- Risk Assessment
- A functional CRUD application created in Python that will meet the requirements of the Jira Board
- Python Testing
- A functioning front-end website and integrated API's, using Flask.
- Code fully integrated into a Version Control System using the
Feature-Branch model which will subsequently be built through a CI
server and deployed to a cloud-based virtual machine.

## Project Tracking
As project Management Software I have used Jira. The link to this board can be found in here (https://trizmanz.atlassian.net/secure/admin/EditDefaultDashboard!default.jspa)

![Jira][Jira Default Dashboard 23.5.21 11.10.PNG]
![Jira][Jira Board All Sprints]

In these 2 boards I have taken a screenshoot of the Backlogs showing the Epics and User Stories this project is based on and a screenshoot of the Dashboard showing where we are with our sprints.

## Database Structure
This project needs a relational database with at least 2 tables, showing the relationship between them. 
The tables created are:
- Exhibitions
- Items

Both tables have a primary key (). The foreign key is in the Items table, showing the relationship to the Exhibitions table.

The relationship is a ```one-to-many``` relationship where an Exhibition can have many Items but an Item can belong or appear in one Exhibition (can't be in 2 places at the same time) .

In the pictures below we can see an Entity Relationship Diagram explaining the relationship between the tables used in this project. This file can be found in https://github.com/bmanzanoqa/PythonProjects/blob/main/MICEX/Screenshots.png/ERD%202%20tables.PNG

![ERD][ERD 2 tables]


## Risk Assessment

Below is a screenshot of the Risk Assessment. This file can be found in https://github.com/bmanzanoqa/PythonProjects/blob/main/MICEX/Screenshots.png/ERD%202%20tables.PNG

![Risk Assessment][RS Latest]





This application will allow you to:
1.	 Create a user account
-	You will need to enter
    -	First name
    -	Last name
    -	Email
    -	Password
-	You will have a ‘login’ button
- 	You will have a ‘cancel’ button
2.	Login 
3.	On the home page you will be presented with 2 options 
-	Items 
    -	CREATE: Create and Item (you will have to enter the following) 
        -	Item ID will be automatically added by DB 
        -	Name 
        -	Age Level 
        -   Difficulty Level 
        -	Number Of Pieces
        -   Date item was built
        -   Photo
        -   Comments  
-	READ: Sort through the items    
1.	It will have a 'choose item' field 
a.	Enter the name of the item we are looking for, or 
b.	Dropdown list  
2.	It will return the item name, a photo and no of pieces
iii.	UPDATE: Update the records 
1.	Dropdown list     
2.	?????????????  
iv.	DELETE: Delete any items 
1.	Dropdown list 
2.	Delete button 
b.	Exhibitions 
i.	CRUD (Can’t think of a name at present) 
1.	Create a Hall (where you can see the items created) 
a.	ID 
b.	Name 
c.	Description 
d.	ItemsList 
e.	Photos
ii.	HALLS 
1.	Coose what Hall Exhibition you want to see 
a.	dropdown list with Halls' names 
b.	(Wish list) if chosen a Hall, it will show the items for the Exhibition and dates and locations 
2.	Dates 
a.	dropdown list with the dates available  
 
b.	(Wish list) it will show all Halls and locations  
3.	Locations 
a.	dropdown list with locations available 
b.	(Wish list) it will show all Halls and dates    

Opening Microblocks Exhibitions ....
Deleting any previous databases, please wait .....
Creating a new database

[Link](https://google.com)

![pic](https://github.com/bmanzanoqa/PythonProjects/blob/ba09f39d1323940254550d6a17c1eba15b26bb34/MICEX/Screenshots.png/Bear%20Shopping.jpg)

| Left Align  | Centre Align | Right Align   |
| :---        |    :----:    |          ---: |
| Row1        | Row1         | Row1          |
| Row2        | Row2         | Row2          |


<details>
<summary>"Click to expand"</summary>
this is hidden
</details>
body{ 
    background-image: url('//*[@id="repo-content-pjax-container"]/div/div[3]/div[2]/div/span/img');
    color: #FFFFFF;

            <!-- <tr>
            <td>Buildings & Wonders</td>
            <td>Famous buildings, skylines and wonders</td>
            <td>Madrid</td>
            <td>24-06-2021</td>
            <td>17</td>
        </tr>
        <tr>
            <td>Animal Kingdom</td>
            <td>Our best friends</td>
            <td>London</td>
            <td>12-11-2021</td>
            <td>7</td>
        </tr> -->

                <!-- <tr>
            <th>Item Name</th>
            <th>Age Level</th>
            <th>Difficulty Level</th>
            <th>Number Of Pieces</th>
            <th>Date Built</th>
            <th>Photo</th>
            <th>Comments</th>
       </tr> -->

       
    </table>
        <td>Big Ben</td>
        <td>14</td>
        <td>4</td>
        <td>3600</td>
        <td>01-01-2019</td>
        <td></td>
        <td>"My first building!"</td>
    </tr>
