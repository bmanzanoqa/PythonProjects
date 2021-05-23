from flask_testing import TestCase
from flask import url_for



from application import app, db
from application.models import Exhibitions, Items

class TestBase(TestCase): 
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" 
        # app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@34.89.84.151:5000/dbmicex.db"
        app.config["SECRET_KEY"] = "ANYTHING"
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["DEBUG"] = True
        return app

    def setUp(self): 
    # Will be called before every test

        db.create_all() 
        sample1 = Exhibitions(name="This is a test Exhibition")
        sample2 = Items(name="This is a test Item")
        db.session.add(sample1)
        db.session.add(sample2)
        db.session.commit()

    def tearDown(self): 
    # Will be called after every test

        db.session.remove() 
        db.drop_all() 
    

class Views(TestBase): 
    
    def test_home_page_get(self):    
        response = self.client.get(url_for('home')) 
        print(response.data)
        self.assertIn(b"This is a test Exhibition", response.data)
        self.assertEqual(response.status_code, 200) 



class TestExhibitions(TestBase): 
    
    def test_UniqueValidator(self):    
        response = self.client.post(
            url_for('addex'),
            data = {'name':"This is a test Exhibition"},
            follow_redirects=True            
            ) 
        self.assertIn(b"That Exhibition already exists. Please choose another name", response.data)
        self.assertEqual(response.status_code, 200) 

    def test_add_exh(self):    
        response = self.client.post(
            url_for('addex'),
            data = {'name':"This is a SECOND test Exhibition"},
            follow_redirects=True            
            ) 
        allExh = Exhibitions.query.all()
        self.assertIn(b"This is a SECOND test Exhibition", response.data)
        
    def test_delete_exh(self):
        response = self.client.get(url_for('deletex', exhibitionsID=1))
        numExh = Exhibitions.query.count()
        self.assertEqual(numExh, 0)

    def test_updatex_get(self):
        response = self.client.get(url_for('updatex', exhibitionsID=1))
        self.assertIn(b"This is a test Exhibition", response.data)
        self.assertIn(b"Update your Exhibition", response.data)

    def test_updatex_post(self):
        response = self.client.post(url_for('updatex', exhibitionsID=1),
        data={"name":"UPDATED EXHIBITION"},
        follow_redirects=True        
        )
        self.assertIn(b"UPDATED EXHIBITION", response.data)




class TestItems(TestBase): 

    def test_home_itpage_get(self):    
            response = self.client.get(url_for('home')) 

            self.assertIn(b"This is a test Item", response.data)
            self.assertEqual(response.status_code, 200)    
    
    def test_UniqueValidator_items(self):    
        response = self.client.post(
            url_for('addit'),
            data = {'name':"This is a test Item"},
            follow_redirects=True            
            ) 
        self.assertIn(b"This Item already exists. Please choose another name", response.data)
        self.assertEqual(response.status_code, 200) 

    def test_add_it(self):    
        response = self.client.post(
            url_for('addit'),
            data = {'name':"This is a SECOND test Item"},
            follow_redirects=True            
            ) 
        allExh = Items.query.all()
        self.assertIn(b"This is a SECOND test Item", response.data)


    def test_delete_it(self):
        response = self.client.get(url_for('deletit', itemsID=1))
        numIt = Exhibitions.query.count()
        self.assertEqual(numIt, 1)

    def test_updatit_get(self):
        response = self.client.get(url_for('updatit', itemsID=1))
        self.assertIn(b"This is a test Item", response.data)
        self.assertIn(b"Update your Item", response.data)

    def test_updatit_post(self):
        response = self.client.post(url_for('updatit', itemsID=1),
        data={"name":"UPDATED ITEM"},
        follow_redirects=True        
        )
        self.assertIn(b"UPDATED ITEM", response.data)
