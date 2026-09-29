# Importa il modulo os, che permette di leggere variabili d'ambiente dal sistema
import os

# Classe che contiene tutte le configurazioni dell'app Flask
    # Legge la variabile d'ambiente SECRET_KEY.
    # Se non esiste, usa "dev_secret" come valore di default.
    # La SECRET_KEY serve per firmare sessioni, token e proteggere parti interne di Flask.
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev_secret")
    
    # Legge la variabile d'ambiente DATABASE_URL.
    # Se non esiste, usa la stringa di connessione di default per PostgreSQL.
    # Questa stringa indica:
    # - tipo di database: postgresql
    # - credenziali: user:password
    # - host: localhost
    # - porta: 5432
    # - nome del database: enterprise_db
    SQLALCHEMY_DATABASE_URI =  os.environ.get(
            "DATABASE_URL",
            "postgresql://user:password@localhost:5432/enterprise_db"
    )
    
    # Disattiva il tracking delle modifiche degli oggetti SQLAlchemy.
    # È una best practice perché evita consumi inutili di memoria e warning.
    SQLALCHEMY_TRACK_MODIFICATIONS = False