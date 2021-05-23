# Hello
## Hello smaller and so on up to 6

_this is in italic_

**this is in bold**

_**this is italic and bold**

- First thing
- Second thing

1. third thing

Hello
Ben

Hello 

Ben

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

from ssl import Options
from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for

from application import app, db
from application.models import Exhibitions, Items

class TestBase(LiveServerTestCase): 
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
        app.config["LIVESERVER_PORT"] = 5000
        app.config["SECRET_KEY"] = "ANYTHING"
        app.config["DEBUG"] = True
        app.config["TESTING"] = True
        return app

    def setUp(self): 
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

        db.create_all() 

        self.driver.get('http://localhost:5000')

    def tearDown(self): 
        self.driver.quit()

        db.drop_all() 

    def test_server_is_up_and_running(self):
        response = urlopen('http://localhost:5050')
        self.assertEqual(response.code, 200) 




# MINI BLOCKS EXHIBITION APP
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


version= $(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$(chromium-browser --version ¦ grep -oP 'Chromium \K\d+'))


chromium-browser --product-version
90.0.4430.93

wget https://chromedriver.storage.googleapis.com/${90.0.4430.93}/chromedriver_linux64.zip

wget https://chromedriver.storage.googleapis.com/${version}/chromedriver_linux64.zip
