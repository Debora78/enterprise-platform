# Blueprint: permette di raggruppare le route in moduli separati (come i controller in PHP/Laravel)
# request: serve per leggere i dati inviati dal client (JSON, parametri, ecc.)
# jsonify: converte un dizionario Python in una risposta JSON
from flask import Blueprint, request, jsonify

# db: istanza di SQLAlchemy, usata per interagire con il database
from ..extensions import db

# User: modello ORM che rappresenta la tabella degli utenti
from ..models.user import User

# Role: modello ORM che rappresenta la tabella dei ruoli (admin, user, ecc.)
from ..models.role import Role

# create_token: funzione che genera un JWT contenente id e ruolo dell’utente
from ..utils.jwt_utils import create_token

# Creiamo un Blueprint chiamato "auth".
# Tutte le route di autenticazione (register, login) vivono dentro questo modulo.
bp = Blueprint("auth", __name__)

@bp.post("/register")
def register():
    """
    Route per registrare un nuovo utente.
    - Legge email e password dal JSON della richiesta
    - Recupera il ruolo "user" dal database
    - Crea un nuovo utente
    - Hasha la password
    - Salva l'utente nel database
    - Restituisce una risposta JSON
    """
    # Legge il JSON inviato dal client
    data = request.get_json()
    
    # Estrae l'email
    email = data["email"]
    
    # Estrae la password
    password = data["password"]
    
    # Recupera il ruolo "user" dal database
    role = Role.query.filter_by(name="user").first()
    
    # Crea l'oggetto utente con email e ruolo
    user = User(email=email, role=role)
    
    # Hash della password (metodo del modello User)
    user.set_password(password)
    
    # Salvataggio nel database
    db.session.add(user)
    db.session.commit()
    
    # Risposta JSON con codice 201 (Created)
    return jsonify({"message": "User created"}), 201



@bp.post("/login")
def login():
    """
    Route per effettuare il login.
    - Legge email e password dal JSON
    - Cerca l'utente nel database tramite email
    - Verifica la password hashata
    - Se credenziali valide → genera un JWT
    - Restituisce il token al client
    """
    
    # Legge il JSON della richiesta
    data = request.get_json()
    
    # Estrae l'email
    email = data["email"]
    
    # Estrae la password
    password = data["password"]
    
    # Cerca l'utente tramite email
    user = User.query.filter_by(email=email).first()
    
    # Se utente non esiste o password errata → errore 401
    if not user or not user.check_password(password):
        return jsonify({"message" : "Invalid credentials"}), 401
    
    # Genera un JWT contenente id e ruolo dell'utente
    token = create_token(user.id, user.role.name)
    
    # Restituisce il token al clien
    return jsonify({"token" : token}), 200