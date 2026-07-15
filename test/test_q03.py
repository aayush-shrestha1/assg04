import os.path
import pytest
import subprocess
from q03 import load_database, store_database, add_contact, modify_contact, delete_contact

test_database = {
    'Walter White': 'wwhite@jpwynne.albuquerque.edu',
    'Jesse Pinkman': 'CapnCook@hotmail.com',
    'Hank Schrader': 'detschrader@dea.gov',
    'Saul Goodman': 'sgoodman@goodmanassociates.org'
}

def test_load_nonexistent_file():
    # we expect a FileNotFoundError
    with pytest.raises(FileNotFoundError) as excinfo:
        filename = 'test/data/nonexistent-database.pkl'
        items = load_database(filename)
    assert "No such file or directory: 'test/data/nonexistent-database.pkl'" in str(excinfo.value)

def test_store_database_creates_file():
    filename = 'test/data/test-database.pkl'
    # make sure file does not exist before we call store to create
    if os.path.isfile(filename):
        os.remove(filename)
    # store a test database
    store_database(filename, test_database)
    assert os.path.isfile(filename)
    os.remove(filename)

def test_store_load_newfile():
    filename = 'test/data/test-database.pkl'
    # make sure file does not exist before we call store to create
    if os.path.isfile(filename):
        os.remove(filename)
    # store a test database
    store_database(filename, test_database)
    assert os.path.isfile(filename)

    database = load_database(filename)
    assert len(database) == 4
    assert 'Jesse Pinkman' in database
    assert 'Walter White' in database
    os.remove(filename)

def test_store_load_overwrites():
    filename = 'test/data/test-database.pkl'
    # make sure file does not exist before we call store to create
    if os.path.isfile(filename):
        os.remove(filename)
    # store a test database
    store_database(filename, test_database)
    assert os.path.isfile(filename)

    database = load_database(filename)
    assert len(database) == 4
    assert 'Jesse Pinkman' in database
    assert 'Walter White' in database

    database['Mike Ehrmantraut'] = 'traut@gmail.com'
    database['Gus Fring'] = 'gfring@LosPollosHermanos.com'
    store_database(filename, database)

    database = load_database(filename)
    assert len(database) == 6
    assert 'Jesse Pinkman' in database
    assert 'Walter White' in database
    assert 'Mike Ehrmantraut' in database
    assert 'Gus Fring' in database
    os.remove(filename)

def test_add_contact():
    database = test_database.copy()

    add_contact(database, 'Mike Ehrmantraut', 'traut@gmail.com')
    assert len(database) == 5
    assert 'Mike Ehrmantraut' in database
    assert 'Walter White' in database

    add_contact(database, 'Gus Fring', 'gfring@LosPollosHermanos.com')
    assert len(database) == 6
    assert 'Gus Fring' in database
    assert 'Mike Ehrmantraut' in database

def test_add_contact_duplicate():
    database = test_database.copy()
    with pytest.raises(KeyError) as excinfo:
        add_contact(database, 'Walter White', 'heisenberg@crystal-blue.pro')
    assert "Attempt to add new email for existing contact" in str(excinfo.value)

def test_modify_contact():
    database = test_database.copy()

    modify_contact(database, 'Walter White', 'heisenberg@crystal-blue.pro')
    assert len(database) == 4
    assert database['Walter White'] == 'heisenberg@crystal-blue.pro'

    modify_contact(database, 'Jesse Pinkman', 'pinkman@crystal-blue.pro')
    assert len(database) == 4
    assert database['Jesse Pinkman'] == 'pinkman@crystal-blue.pro'

def test_modify_contact_missing():
    database = test_database.copy()

    with pytest.raises(KeyError) as excinfo:
        modify_contact(database, 'Walter Black', 'heisenberg@crystal-blue.pro')
    assert "Attempt to modify nonexistent contact" in str(excinfo.value)

def test_delete_contact():
    database = test_database.copy()

    delete_contact(database, 'Walter White')
    assert len(database) == 3
    assert 'Walter White' not in database

    delete_contact(database, 'Jesse Pinkman')
    assert len(database) == 2
    assert 'Jesse Pinkman' not in database

def test_delete_contact_missing():
    database = test_database.copy()

    with pytest.raises(KeyError) as excinfo:
        delete_contact(database, 'Walter Black')
    assert "Attempt to delete nonexistent contact" in str(excinfo.value)

def test_q03_application():
    command = ['python3', 'test/test-question.py', '-c', 'q03_application.py']
    result = subprocess.run(command)
    assert result.returncode == 0