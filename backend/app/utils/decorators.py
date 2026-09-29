"""
Questo file contiene i decoratori utilizzati per aggiungere funzionalità
alle route dell'applicazione senza modificare il loro codice originale.

In particolare, il decoratore `@jwt_required` agisce come un middleware:
- intercetta la richiesta prima che arrivi alla funzione della route;
- verifica la presenza dell'header Authorization;
- controlla che il token JWT sia valido e non scaduto;
- estrae dal token le informazioni dell'utente (user_id e role);
- blocca l'esecuzione della route se il token è mancante o invalido;
- permette l'esecuzione della funzione originale solo quando l'utente è autenticato.

I decoratori in Python funzionano come un "involucro" attorno a una funzione:
permettono di eseguire logica aggiuntiva prima o dopo la funzione decorata,
senza alterarne direttamente il codice. Sono l'equivalente dei middleware
o degli override dei metodi nelle classi in altri linguaggi.
"""



# wraps serve per mantenere nome e docstring della funzione originale
from functools import wraps

# request → per leggere header, body, ecc.
# jsonify → per restituire risposte JSON
# current_app → per leggere la configurazione (SECRET_KEY)
from flask import request, jsonfy, current_app

# Libreria JWT per decodificare il token
import jwt

# Decoratore personalizzato che richiede un token JWT per accedere alla route
def jwt_required(fn):
    
    # Mantiene le informazioni della funzione originale
    @wraps(fn)
    def wrapper(*arg, **kwargs):
        
        # Legge l'header Authorization
        auth = request.headers.get("Authorization")
        
        # Se non c'è l'header o non inizia con "Bearer", token mancante
        if not auth or not auth.startswith("Bearer"):
            return jsonfy({"message": "Missing token"}), 401

        # Estrae il token: "Bearer <token>"
        token = auth.split(" ")[1]
        
        
        try:
            # Decodifica il token usando la SECRET_KEY dell'app
            payload = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
        
        except:
            
            # Se la decodifica fallisce → token invalido
            return jsonfy({"message": "Invalid token"}), 401
        
        # Salva i dati del token dentro request
        # Così la route può sapere chi è l'utente
        request.user_id = payload["sub"]
        request.user_role = payload["role"]
        
        
        # Esegue la funzione originale
        # (*arg, **kwargs) corrisponde allo spread operator di php cioè accetta tanti valori
        return fn(*arg, **kwargs)
    
    # Ritorna il decoratore
    return wrapper            
        