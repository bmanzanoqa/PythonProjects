from flask_testing import TestCase
from flask import url_for


from application import app, db
from application.models import Exhibitions, Items

# this will be our test page
class TestBase(TestCase):      # This is the test base we will use always and it inherits TestCase(we need to import from flask_testing)
   # You always need 3 methods in this class
    def creat_app(self): # allows you to define any configurations in your app. All methods need "self"
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"  # leave db name empty aas it will create a temporary database
        app.config["SECRET_KEY"] = "jksdhk"
        app.config["DEBUG"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        return app # we have made some changes to our app configuration and we need to return our new changed app

    def setUp(self): # this is done before every test
        db.create_all() # we create our database to make sure our test has access to the tables
        # sample1 = Exhibitions(name="This is a test Exhibition")
        # #sample2 = Items(name="Statute of Liberty")
        # db.session.add(sample1)
        # #db.session.add(sample2)
        # db.session.commit()

    def tearDown(self): #run at the end of every test
        db.session.remove() # removes all the data in the tables
        db.drop_all() # removes all the tables
    
# now we start writing our tests. 
# Our tests need to be in CLASSES


class Views(TestBase): # it needs to inherit the testbase class we just created so it runs the functions we just created before and after each test
    def test_home_get(self):    
        response = self.client.get(url_for('home')) # url_for + name of the function to get to the url (it's the name given in routes)
        # now we need some asserts
        self.assertEqual(response.status_code, 200) # checks that when it connects to the home page it gets a 200 code (it connects)
        # self.assertIn(b"This is a test Exhibition", response.data) # it checks that the examples given in 19 & 20 are in the database.
                                                        
        #self.assertIn(b"Statute of Liberty", response.data)
   
    # # you can have multiple tests in one class
    # def tes_home_post(self):
    #     response = self.client.post(  # this is the POST method, we are going to be passing some data
    #             url_for('home'),  
    #             data={"name":"Lelo"}, # it will send this data to the function 'home' in routes
    #             follow_redirects=True
    #         )
    #     print(response.data)  #this is OPTIONAL but it will show us what the data looks like in HTML
    #         # now we want to check if it worked. It will check if 'Lelo' is in the screen with "response.data"
    #     self.assertIn(b"Lelo", response.data)