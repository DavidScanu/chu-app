import datetime

class Patient:
    """Classe Patient"""

    def __init__(self, nom, prenom, date_naissance, groupe_sanguin):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.groupe_sanguin = groupe_sanguin
        self.is_in_hospital = 0
        self.id = (self.nom + self.prenom + self.date_naissance.replace('-', '') + self.groupe_sanguin).lower()

    def __str__(self):
        """ Return a human-readable format, which is good for logging or to display some information about the object."""

        return f"""Patient => nom : {self.nom}, prenom : {self.prenom}, date de naissance : {self.date_naissance}, groupe sanguin : {self.groupe_sanguin}"""

    def __repr__(self):
        """ Official string representation of the object, which can be used to construct the object again."""

        return f"""Patient(nom={self.nom}, prenom={self.prenom}, date_naissance={self.date_naissance}, groupe_sanguin={self.groupe_sanguin})"""

    @staticmethod
    def get_patients(bdd):
        """Returns all patients in DB."""
        try: 
            cursor = bdd.cursor()
            query = "SELECT * FROM patients;"
            # print("Query => ", query)
            cursor.execute(query)
            patients = cursor.fetchall()

            if patients:
                return patients
            else : 
                return "There are no patients in DB."

        except:
            print('get_patients : There is an error!')

        finally:
            if bdd.is_connected():
                # Close cursor
                cursor.close()

    @staticmethod
    def get_patient(bdd, id):
        """Retourne un patient dans la base de données."""
        try: 
            cursor = bdd.cursor()
            query = f"""SELECT * FROM patients WHERE identifiant_patient = '{id}';"""
            cursor.execute(query)
            patient = cursor.fetchall()

            if patient:
                return patient
            else : 
                return False

        except Exception as e:
            print('Patient.get_patient : There is an error!')
            print(e)

        finally:
            if bdd.is_connected():
                # Close cursor
                cursor.close()

    def create_patient(self, bdd):
        """Creates patient in table 'patients' in DB."""
        try: 
            cursor = bdd.cursor()
            query = f"""INSERT INTO patients (identifiant_patient, nom, prenom, date_naissance, groupe_sanguin, is_in_hospital) VALUES ('{self.id}', '{self.nom}', '{self.prenom}', '{self.date_naissance}', '{self.groupe_sanguin}', '{self.is_in_hospital}') ON DUPLICATE KEY UPDATE identifiant_patient = '{self.id}';"""
            cursor.execute(query)
            bdd.commit()

            # print(f"""Patient : id = {self.id}, nom : {self.nom}, prenom: {self.prenom}, date de naissance : {self.date_naissance}, groupe sanguin : {self.groupe_sanguin}.""")

            # print(f"""Created with success!""")

        except Exception as e:
            print('create_patient : There is an error!')
            print(e)

        finally:
            if bdd.is_connected():
                cursor.close()
        
    # Notes chef de service
    def entrer_a_l_hopital(self, bdd):

        try: 
            cursor = bdd.cursor()
            # query = f"""UPDATE patients SET is_in_hospital = {self.is_in_hospital} WHERE identifiant_patient = '{self.id}';"""
            query = f"""UPDATE patients SET is_in_hospital = '1' WHERE identifiant_patient = '{self.id}';"""
            cursor.execute(query)
            bdd.commit()

        except Exception as e:
            print('entrer_a_l_hopital : There is an error!')
            print(e)

        finally:
            if bdd.is_connected():
                cursor.close()

    def sortir_de_l_hopital(self, bdd):

        try: 
            cursor = bdd.cursor()
            query = f"""UPDATE patients SET is_in_hospital = '0' WHERE identifiant_patient = '{self.id}';"""
            cursor.execute(query)
            bdd.commit()

        except Exception as e:
            print(e)

        finally:
            if bdd.is_connected():
                cursor.close()


class Employe:
    """Classe Employe"""

    def __init__(self, nom, prenom, date_naissance, salaire):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.salaire = salaire
        self.working_at_hospital = 0
        self.id = (self.nom + self.prenom + self.date_naissance.replace('-', '')).lower()

    def __str__(self):
        """ Return a human-readable format, which is good for logging or to display some information about the object."""

        return f"""Employe => nom : {self.nom}, prenom : {self.prenom}, date de naissance : {self.date_naissance}, salaire : {self.salaire}"""

    def __repr__(self):
        """ Official string representation of the object, which can be used to construct the object again."""

        return f"""Employe(nom={self.nom}, prenom={self.prenom}, date_naissance={self.date_naissance}, salaire={self.salaire}"""

    @staticmethod
    def get_employes(bdd):
        """Returns all Employes in DB."""
        try: 
            cursor = bdd.cursor()
            query = "SELECT * FROM rh;"
            # print("Query => ", query)
            cursor.execute(query)
            employes = cursor.fetchall()

            if employes:
                return employes
            else : 
                return "il n'y a pas d'employés dans la base de données."

        except Exception as e:
            print('get_employes : There is an error!')
            print(e)

        finally:
            if bdd.is_connected():
                # Close cursor
                cursor.close()

    @staticmethod
    def get_employe(bdd, id):
        """Retourne un employe dans la base de données."""
        try: 
            cursor = bdd.cursor()
            query = f"""SELECT * FROM rh WHERE identifiant_rh = '{id}';"""
            cursor.execute(query)
            employe = cursor.fetchall()

            if employe:
                return employe
            else :  
                return False

        except Exception as e:
            print('Patient.get_employe : There is an error!')
            print(e)

        finally:
            if bdd.is_connected():
                # Close cursor
                cursor.close()

    def create_employe(self, bdd):
        """Sauvegarde un employé dans la base de données."""
        try: 
            cursor = bdd.cursor()
            query = f"""INSERT INTO rh (identifiant_rh, nom, prenom, date_naissance, salaire, working_at_hospital) VALUES ('{self.id}', '{self.nom}', '{self.prenom}', '{self.date_naissance}', '{self.salaire}', '{self.working_at_hospital}') ON DUPLICATE KEY UPDATE identifiant_rh = '{self.id}';"""
            cursor.execute(query)
            bdd.commit()

            # print(f"""Employé => id = {self.id}, nom : {self.nom}, prenom: {self.prenom}, date de naissance : {self.date_naissance}, salaire : {self.salaire}, travail à l'hopital : {self.working_at_hospital}.""")

            # print(f"""Employé sauvegarder avec succès !""")

        except Exception as e:
            print('create_employe => Il y a une erreur !')
            print(e)

        finally:
            if bdd.is_connected():
                cursor.close()

    # Notes chef de service
    def debuter_CDD_CDI(self, bdd):

        try: 
            cursor = bdd.cursor()
            query = f"""UPDATE rh SET working_at_hospital = '1' WHERE identifiant_rh = '{self.id}';"""
            cursor.execute(query)
            bdd.commit()

        except Exception as e:
            print('Employe.debuter_CDD_CDI : Il y a une erreur !')
            print(e)

        finally:
            if bdd.is_connected():
                cursor.close()

    def quitter_CDD_CDI(self, bdd):

        try: 
            cursor = bdd.cursor()
            query = f"""UPDATE rh SET working_at_hospital = '0' WHERE identifiant_rh = '{self.id}';"""
            cursor.execute(query)
            bdd.commit()

        except Exception as e:
            print('Employe.quitter_CDD_CDI : Il y a une erreur !')
            print(e)

        finally:
            if bdd.is_connected():
                cursor.close()