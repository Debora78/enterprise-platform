# Importa la libreria JWT per creare e verificare token JSON Web Token
import jwt

# Importa datetime per ottenere l'ora attuale
# Importa timedelta per aggiungere intervalli di tempo (es. +1 ora)
from datetime import datetime, timedelta

# Importa current_app per accedere alla configurazione di Flask (es. SECRET_KEY)
from flask import current_app

# Funzione che crea un token JWT per un utente
def create_token(user_id, role):
    
    # Il payload è il contenuto del token:
    # - "sub": identifica il soggetto del token (subject → user_id)
    # - "role": ruolo dell'utente (admin, user, ecc.)
    # - "exp": data di scadenza del token (ora attuale + 1 ora)
    payload = {
        "sub" : user_id,
        "role" : role,
        "exp" : datetime.utcnow() + timedelta(hours=1)
    }
    
    # Firma il token con la SECRET_KEY dell'app Flask
    # Usa l'algoritmo HS256 per la firma
    # Ritorna il token JWT codificato
    return jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")