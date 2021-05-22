from flask_testing import TestCase
from flask import url_for


from application import app, db
from application.models import Exhibitions, Items

class TestBase(TestCase): 
    def creat_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"  
        app.config["SECRET_KEY"] = "jksdhk"
        app.config["DEBUG"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        return app

    def setUp(self): 
        db.create_all() 
        sample1 = Exhibitions(name="This is a test Exhibition")
        db.session.add(sample1)
        db.session.commit()

    def tearDown(self): 
        db.session.remove() 
        db.drop_all() 
    

class Views(TestBase): 
    def test_home_page_get(self):    
        response = self.client.get(url_for('home')) 
        self.assertEqual(response.status_code, 200) 
        self.assertIn(b"This is a test Exhibition", response.data)
       