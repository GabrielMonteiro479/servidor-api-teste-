import unittest
import flask_testing
from flask_testing import TestCase
from flask_fixtures import FixturesMixin
from app import app, db
from app.routes import *

app.config.from_pyfile('../config/test.cfg')

# work around por que o flask_fixtures e o flask_testing tentam limpar o context stack. 
def _clean_ctx(stack): 
    try:
        stack._ctx.pop()
    except:
        pass
    del stack._ctx

# cria databases ou esquemas
def _attach(session, schemas):
    session.flush()
    if schemas:
        for schema in schemas:
            session.execute("ATTACH DATABASE ':memory:' AS %s;" % schema)
        

# deleta databases ou esquemas
def _detach(session, schemas):
    session.flush()
    if schemas:
        for schema in schemas:
            session.execute("DETACH DATABASE %s;" % schema)
        

class FlaskTestCase(TestCase, FixturesMixin):
    
    def create_app(self):
        return app

    @classmethod
    def setUpClass(cls):
        cls.app = app
        cls.db = db
        _attach(db.session, getattr(cls, 'other_schemas', None))

    @classmethod
    def tearDownClass(cls):
        _detach(db.session, getattr(cls, 'other_schemas', None))

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        _clean_ctx(self)


class DBTestCase(unittest.TestCase, FixturesMixin):
    
    @classmethod
    def setUpClass(cls):
        cls.app = app
        cls.db = db
        _attach(db.session, getattr(cls, 'other_schemas', None))

    @classmethod
    def tearDownClass(cls):
        _detach(db.session, getattr(cls, 'other_schemas', None))


class UnitTestCase(unittest.TestCase):
    pass