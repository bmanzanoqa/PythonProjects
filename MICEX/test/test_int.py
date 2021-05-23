from flask_testing import LiveServerTestCase, TestCase
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for


from application import app, db
from application.models import Exhibitions, Items

class TestBase(LiveServerTestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db" 
        #app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@34.89.84.151:5000/dbmicex.db"
        app.config["LIVESERVER_PORT"] = 5050
        app.config["SECRET_KEY"] = "ANYTHING"
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        return app

    def setUp(self):
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(options=chrome_options)

        db.create_all()

        self.driver.get('http://localhost:5050')

    def tearDown(self):
        self.driver.quit()

        db.drop_all()

  
    def test_server_is_up_and_running(self):
        response = urlopen('http://localhost:5050')
        self.assertEqual(response.code, 200)

    class TestViews(TestCase):

        def test_navigation(self):
            self.driver.find_element_by_xpath("/html/body/a[2]").click
            
            print(url_for("addex"))
            print(self.driver.current_url)

            self.assertIn(url_for("addex"), self.driver.current_url)
