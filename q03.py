import pickle


def store_database(filename, database):
    with open(filename, "wb") as file:
        pickle.dump(database, file)


def load_database(filename):
    with open(filename, "rb") as file:
        database = pickle.load(file)

    return database


def add_contact(database, name, email):
    if name in database:
        raise KeyError("Attempt to add new email for existing contact")

    database[name] = email


def modify_contact(database, name, email):
    if name not in database:
        raise KeyError("Attempt to modify nonexistent contact")

    database[name] = email


def delete_contact(database, name):
    if name not in database:
        raise KeyError("Attempt to delete nonexistent contact")

    del database[name]
