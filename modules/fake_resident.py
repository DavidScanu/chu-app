from datetime import datetime, timedelta
from random import randint
from randomuser import RandomUser

# Generate random patients and RH

# Generate random birth date
def date_of_birth_generator(maximum_age=99, date_format="%Y-%m-%d"):
    """ Generates date of births in the specified format and age range
    Args:
        maximum_age: the maximum age (relative to the current date)
        date_format: format of the date in Python datetime.strftime format
    """
    return (datetime.today() - timedelta(days=randint(0, 365 * maximum_age))).strftime(date_format)


def generate_random_patient():
    """Generate random 'patient' variables. Use Patient class to generate the patient and save it to db."""
    # Random User
    rand_user = RandomUser()
    rand_nom = rand_user.get_last_name()
    rand_prenom = rand_user.get_first_name()
    # Random birth date
    rand_date_naissance = date_of_birth_generator()
    # Random groupe sanguin
    groupe_sanguin_list = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    rand_groupe_sanguin = groupe_sanguin_list[randint(0, 7)]

    return rand_nom, rand_prenom, rand_date_naissance, rand_groupe_sanguin


def generate_random_employe():
    """Generate random employe variables. Use Employe class to save the employe in db."""
    # Random User
    rand_user = RandomUser()
    rand_nom = rand_user.get_last_name()
    rand_prenom = rand_user.get_first_name()
    # Random birth date
    rand_date_naissance = date_of_birth_generator()
    # Random salaire
    rand_salaire = randint(10000, 100000)

    return rand_nom, rand_prenom, rand_date_naissance, rand_salaire