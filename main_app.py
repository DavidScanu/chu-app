from database import get_db_config, db_connect, db_close
from streamlit_view import display_streamlit_app

# CONSTANTS
VERBOSE = True
CONFIG_FILE_PATH = 'config.json'
CONFIG = get_db_config(CONFIG_FILE_PATH)

if __name__ == "__main__":

    # Database connection
    bdd = db_connect(CONFIG, VERBOSE)

    if bdd.is_connected():

        # Affiche la vue Streamlit
        display_streamlit_app(bdd)

    # Close BDD
    db_close(bdd, VERBOSE)