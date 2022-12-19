import streamlit as st
import datetime
import time
import pandas as pd
from modules.resident import Patient, Employe
from modules.administration import Archive
from modules.fake_resident import generate_random_patient, generate_random_employe

def display_streamlit_app(bdd):

    st.set_page_config(
        page_title="CHU App",
        page_icon=":hospital:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    with st.container():
        st.header(':hospital: CHU App')

    tab1, tab2, tab3 = st.tabs(["Patients", "Employés", "Archives"])
    with st.container():
            
        with tab1:
            st.header("Patients")
            with st.container():
                col1, col2 = st.columns([1,2])
                # Left column
                with col1:
                    # Add random patient
                    with st.form("add_random_patient"):
                        st.write("Ajouter un patient aléatoire")
                        rand_nom, rand_prenom, rand_date_naissance, rand_groupe_sanguin = generate_random_patient()
                        rand_patient_submitted = st.form_submit_button("Ajouter patient aléatoire")
                        if rand_patient_submitted:
                            with st.spinner('Processus en cours...'):
                                # Instance du patient
                                rand_patient = Patient(rand_nom, rand_prenom, rand_date_naissance, rand_groupe_sanguin)
                                # Sauvegarde le patient dans la table 'patients'
                                rand_patient.create_patient(bdd)
                                time.sleep(1)
                            st.success('Nouveau patient ajouté avec succès !')
                            st.balloons()
                    # Add patient
                    with st.form("add_patient"):
                        st.write("Ajouter un patient")
                        patient_nom = st.text_input('Nom', max_chars=200, label_visibility="visible")
                        patient_prenom = st.text_input('Prénom', max_chars=200, label_visibility="visible")
                        patient_date_naissance = st.date_input('Date de naissance', value=datetime.date(1990, 1, 1), label_visibility="visible").strftime("%Y-%m-%d")
                        patient_groupe_sanguin = st.selectbox( 'Groupe sanguin', ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'))
                        patient_submitted = st.form_submit_button("Ajouter patient")
                        if patient_submitted:
                            if patient_nom and patient_prenom and patient_date_naissance:
                                with st.spinner('Processus en cours...'):
                                    # Instance du patient
                                    patient = Patient(patient_nom, patient_prenom, patient_date_naissance, patient_groupe_sanguin)
                                    # Sauvegarde le patient dans la table 'patients'
                                    patient.create_patient(bdd)
                                    time.sleep(1)
                                st.success('Nouveau patient ajouté avec succès !')
                                st.balloons()
                            else : 
                                st.warning("Veuillez entrer un nom, un prénom et une date de naissance pour ajouter un nouveau patient.")

                # Right Column
                with col2:
                    patients = Patient.get_patients(bdd)
                    patients_df = pd.DataFrame(data=patients, columns=['ID', 'Nom', 'Prénom', 'Date de naissance', 'Groupe sanguin', "Est dans l'hopital"])
                    st.write(patients_df)

        with tab2:
            st.header("Employés")
            with st.container():
                col1, col2 = st.columns([1,2])
                # Left column
                with col1:
                    # Add random employee
                    with st.form("add_random_employe"):
                        st.write("Ajouter un employé aléatoire")
                        rand_nom, rand_prenom, rand_date_naissance, rand_salaire = generate_random_employe()
                        rand_employe_submitted = st.form_submit_button("Ajouter employé aléatoire")
                        if rand_employe_submitted:
                            with st.spinner('Processus en cours...'):
                                # Instance du patient
                                rand_employe = Employe(rand_nom, rand_prenom, rand_date_naissance, rand_salaire)
                                # Sauvegarde le patient dans la table 'patients'
                                rand_employe.create_employe(bdd)
                                time.sleep(1)
                            st.success('Nouvel employé ajouté avec succès !')
                            st.balloons()
                    # Add patient
                    with st.form("add_employe"):
                        st.write("Ajouter un employé")
                        employe_nom = st.text_input('Nom', max_chars=200, label_visibility="visible")
                        employe_prenom = st.text_input('Prénom', max_chars=200, label_visibility="visible")
                        employe_date_naissance = st.date_input('Date de naissance', value=datetime.date(1990, 1, 1), label_visibility="visible").strftime("%Y-%m-%d")
                        employe_salaire = st.slider('Salaire', 1000, 200000, 30000) 
                        employe_submitted = st.form_submit_button("Ajouter employé")
                        if employe_submitted:
                            if employe_nom and employe_prenom and employe_date_naissance and employe_salaire:
                                with st.spinner('Processus en cours...'):
                                    # Instance du patient
                                    employe = Employe(employe_nom, employe_prenom, employe_date_naissance, employe_salaire)
                                    # Sauvegarde l'employé dans la table 'rh'
                                    employe.create_employe(bdd)
                                st.success('Nouvel employé ajouté avec succès !')
                                st.balloons()
                            else : 
                                st.warning("Veuillez entrer un nom, un prénom, une date de naissance et un salaire pour ajouter un nouvel employé.")

                # Right Column
                with col2:
                    employes = Employe.get_employes(bdd)
                    employes_df = pd.DataFrame(data=employes, columns=['ID', 'Nom', 'Prénom', 'Date de naissance', 'Salaire', "Est dans l'hopital"])
                    st.write(employes_df)

        with tab3:
            st.header("Archives")
            with st.container():
                col1, col2 = st.columns([1,2])
                # Left column
                with col1:
                    with st.form("archive_entree"):
                        st.write("Ajouter une date d'entrée")
                        archive_id = st.text_input('ID')
                        archive_date_entree = st.date_input("Date d'entrée")
                        archive_submitted = st.form_submit_button("Ajouter date d'entrée")
                        if archive_submitted and archive_id and archive_date_entree:
                            with st.spinner('Processus en cours...'):
                                # Sauvegarde de date_entree dans la table 'archives'
                                archive = Archive(archive_id)
                                archive.enregister_entree(bdd, archive_date_entree)
                                # Sauvegarde de is_in_hospital dans table 'patients' ou working_at_hospital dans table 'rh'
                                archive_patient_list = Patient.get_patient(bdd, archive_id)
                                archive_rh_list = Employe.get_employe(bdd, archive_id)
                                if archive_patient_list:
                                    patient_archive = Patient(archive_patient_list[0][1], archive_patient_list[0][2], archive_patient_list[0][3].strftime("%Y-%m-%d"), archive_patient_list[0][4])
                                    patient_archive.entrer_a_l_hopital(bdd)
                                elif archive_rh_list:
                                    employe_archive = Employe(archive_rh_list[0][1], archive_rh_list[0][2], archive_rh_list[0][3].strftime("%Y-%m-%d"), archive_rh_list[0][4])
                                    employe_archive.debuter_CDD_CDI(bdd)
                                else:
                                    st.warning('Aucun ID correspondant dans la base de données.')
                                st.success("Date d'entrée sauvegardée avec succès !")
                                st.balloons()
                        else : 
                            if 'my_button' in st.session_state:
                                st.warning("Veuillez entrer un ID et une date d'entrée.")

                    with st.form("archive_sortie"):
                        st.write("Ajouter une date de sortie")
                        archive_id_2 = st.text_input('ID')
                        archive_date_sortie = st.date_input("Date de sortie")
                        archive_submitted = st.form_submit_button("Ajouter date de sortie")
                        if archive_submitted and archive_id_2 and archive_date_sortie:
                            with st.spinner('Processus en cours...'):
                                # Sauvegarde de la date de sortie dans la table 'archives'
                                archive_2 = Archive(archive_id_2)
                                archive_2.enregistrer_sortie(bdd, archive_date_sortie)
                                # Sauvegarde de is_in_hospital dans table 'patients' ou working_at_hospital dans table 'rh'
                                archive_patient_list_2 = Patient.get_patient(bdd, archive_id)
                                archive_rh_list_2 = Employe.get_employe(bdd, archive_id_2)
                                if archive_patient_list_2:
                                    patient_archive_2 = Patient(archive_patient_list_2[0][1], archive_patient_list_2[0][2], archive_patient_list_2[0][3].strftime("%Y-%m-%d"), archive_patient_list_2[0][4])
                                    patient_archive_2.sortir_de_l_hopital(bdd)
                                elif archive_rh_list_2:
                                    employe_archive_2 = Employe(archive_rh_list_2[0][1], archive_rh_list_2[0][2], archive_rh_list_2[0][3].strftime("%Y-%m-%d"), archive_rh_list_2[0][4])
                                    employe_archive_2.quitter_CDD_CDI(bdd)
                                else:
                                    st.warning('Aucun ID correspondant dans la base de données.')
                                st.success("Date d'entrée sauvegardée avec succès !")
                                st.balloons()
                        else :
                            if 'my_button' in st.session_state:
                                st.warning("Veuillez entrer un ID et une date de sortie.")


                with col2:
                    archives = Archive.get_archives(bdd)
                    archives_df = pd.DataFrame(data=archives, columns=['ID', "Date d'entrée", "Date de sortie"])
                    st.write(archives_df)

    # st.write(st.session_state) 
    if 'my_button' not in st.session_state:
        st.session_state.my_button = True