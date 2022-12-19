class Archive:
    """Classe Archive"""

    def __init__(self, id):
        self.id = id
    
    def __str__(self):
        pass

    def __repr__(self):
        pass

    @staticmethod
    def get_archives(bdd):
        """Fonction qui retourne toutes les lignes dans la table 'archives'."""
        try: 
            cursor = bdd.cursor()
            query = "SELECT * FROM archives;"
            cursor.execute(query)
            archives = cursor.fetchall()

            if archives:
                return archives
            else : 
                return "il n'y a pas d'archives dans la base de données."

        except Exception as e:
            print('Archive.get_archives : Il y a une erreur !')
            print(e)

        finally:
            if bdd.is_connected():
                # Close cursor
                cursor.close()

    def enregister_entree(self, bdd, date_entree):
        """Fonction qui enregistre la date d'entrée d'un patient ou d'un employé dans la base de données (table : archives)."""

        try: 
            cursor = bdd.cursor()
            query = f"""INSERT INTO archives (identifiant_resident, date_entree) VALUES ('{self.id}', '{date_entree}') ON DUPLICATE KEY UPDATE date_entree = '{date_entree}';"""
            cursor.execute(query)
            bdd.commit()

        except Exception as e:
            print('Archive.enregister_entree : Il y a une erreur !')
            print(e)

        finally:
            if bdd.is_connected():
                cursor.close()

    def enregistrer_sortie(self, bdd, date_sortie):
        """Fonction qui enregistre la date de sortie d'un patient ou d'un employé dans la base de données (table : archives)."""

        try: 
            cursor = bdd.cursor()
            query = f"""UPDATE archives SET date_sortie = '{date_sortie}' WHERE identifiant_resident = '{self.id}';"""
            cursor.execute(query)
            bdd.commit()

        except Exception as e:
            print(e)

        finally:
            if bdd.is_connected():
                cursor.close()

    # @staticmethod
    # def afficher_les_archives_streamlit():
    #     pass

    # @staticmethod
    # def afficher_les_archives_console():
    #     pass