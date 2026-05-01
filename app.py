import streamlit as st
import pandas as pd
import sqlite3
import os

#Configure la BD
DB_NAME = "enquete_enspd.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS etudiants
                (filiere TEXT, moyenne REAL, heures_etude REAL, heures_rs REAL, stress INTEGER)
              '''  
            )
    conn.commit()
    conn.close()

def save_data(filiere, moyenne, etude, rs, stress):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO etudiants VALUES(?, ?, ?, ?, ?)",(filiere, moyenne, etude, rs, stress))
    conn.commit()
    conn.close()

#interface streamlit
st.set_page_config(page_title = "StatEdu", layout="wide")
init_db()

st.title("Collecte Et Analyse Descriptive")
st.markdown("Bienvenue dans l'application de collecte pour le cours d'analyse de donnees.")


#Formulaire de collecte
with st.sidebar:
    st.header("Formulaire de collecte")
    with st.form("survey_form", clear_on_submit=True):
        filiere = st.selectbox("Votre filiere", ["TCO", "GIT", "GAM", "GC", "GM","GE","GP","QHSE","GESI"])
        moyenne = st.number_input("Moyenne session normale precedente", 0.0, 20.0, 10.0)
        h_etude = st.slider("Heures d'etude / jour", 0.0, 15.0, 4.0)
        h_rs = st.slider("Heures Reseaux Sociaux / Jour", 0.0, 15.0, 2.0)
        stress = st.select_slider("Niveau de stress", options=list(range(1, 11)))

        submit = st.form_submit_button("Envoyer les donnees")
        if submit:
            save_data(filiere, moyenne, h_etude, h_rs, stress)
            st.success("Donnees enregistrees !")

#Analyse descriptive
st.header("Resultats de l'analyse en temps reel")

conn = sqlite3.connect(DB_NAME)
df = pd.read_sql_query("SELECT * FROM etudiants", conn)
conn.close()

if not df.empty:
    col1, col2, col3 = st.columns(3)
    col1.metric("Nombre de repondants", len(df))
    col2.metric("MOyenne Generale", round(df["moyenne"].mean(), 2))
    col3.metric("Moyenne Etude (en heure)", round(df["heures_etude"].mean(), 1))

    #Graphique pour l'analyse descriptive
    st.subheader("Correlation : Etude vs Reseaux Sociaux")
    st.scatter_chart(data=df, x="heures_rs", y="heures_etude", color="filiere")

    st.subheader("repartition de la moyenne par filiere")
    st.bar_chart(df.groupby("filiere")["moyenne"].mean())

else:
    st.info("En attente de donnees pour generer l'analyse...")
