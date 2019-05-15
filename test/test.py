from flask_testing import TestCase
from app import app, db
from models import User, Message
import unittest


class FlaskAppTest(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flaskAppTest:flaskAppTest@localhost:3306/flaskAppTest'
        return app

    def setUp(self):
        db.create_all()
        db.session.add(
            User(name='Adonay', email='ado@ado.com', password='aaa'))
        db.session.add(
            User(name='Mark', email='mark@mark.com', password='mmm'))
        db.session.add(
            User(name='John', email='john@john.com', password='jjj'))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
    def test_messages_loads(self):
      response = self.client.get('/messages', follow_redirects=True)
      self.assert200(response)

    def test_newpost(self):
      response = self.client.post(
        '/newpost',
        data=dict(title='Urgent', category='Urgent', shift='Morning', content='This is a test urgent message.'),
        follow_redirects = True
      )
      self.assert200(response)
      self.assertMessageFlashed('Posted Note Successfully', 'success')
      self.assertIn(b'Urgent', response.data)