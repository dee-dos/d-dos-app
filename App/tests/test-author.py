import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import create_db
from App.models import Author
from App.controllers import (
    create_author,
    get_author_by_fname,
    get_author_by_lname,
    get_author_email,
    get_author,
    get_all_authors,
    get_all_authors_json,
    delete_author,
    update_author,
    get_author_pubs,
)

from wsgi import app


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''

class AuthorUnitTests(unittest.TestCase):

    def test_new_author(self):
        author = Author("James", "Bond", "bondjamesbond@secret.agent", "bondisbond!")
        assert author.email == "bondjamesbond@secret.agent"

    def test_toJSON(self):
        author = Author("James", "Bond", "bondjamesbond@secret.agent", "bondisbond!")
        author_json = author.toJSON()
        self.assertDictEqual(author_json, {"id":None, "email":"bondjamesbond@secret.agent"})
    
    def test_hashed_password(self):
        password = "bondisbond!"
        hashed = generate_password_hash(password, method='sha256')
        author = Author("James", "Bond", "bondjamesbond@secret.agent", password)
        assert author.password != password

    def test_check_password(self):
        password = "bondisbond!"
        author = Author("James", "Bond", "bondjamesbond@secret.agent", password)
        assert author.check_password(password)

'''
    Integration Tests
'''

# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app.config.update({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db(app)
    yield app.test_client()
    os.unlink(os.getcwd()+'/App/test.db')


def test_authenticate():
    author = create_author("James", "Bond", "bondjamesbond@secret.agent", "bondisbond!")
    assert authenticate("James", "Bond", "bondjamesbond@secret.agent", "bondisbond!") != None

class UsersIntegrationTests(unittest.TestCase):

    def test_create_author(self):
        author = create_author("James", "Bond", "bondjamesbond@secret.agent", "bondisbond!")
        assert user.email == "bondjamesbond@secret.agent"

    def test_get_all_authors_json(self):
        authors_json = get_all_authors_json()
        self.assertListEqual([{"id":"1", "email":"nmendez@gmail.com"}, {"id":"2", "email":"mbrereton@gmail.com"}], users_json)

    def test_update_user(self):
        update_author("1", "Ronnie", "Mendez", "rmendez@gmail.com", "mendez15cool!")
        user = get_user(1)
        assert user.username == "Ronnie"
