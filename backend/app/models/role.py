# Importa l'istanza di SQLAlchemy per definire il modello
from ..extensions import db

# Definisce il modello Role, che rappresenta la tabella "roles"
class Role(db.Model):
    
    # Nome esplicito della tabella nel database PostgreSQL
    __tablename__ = "roles"
    
    # Colonna ID:
    # - Integer → numero intero
    # - primary_key=True → chiave primaria della tabella
    id = db.Column(db.Integer, primary_key=True)
    
    # Colonna NAME:
    # - String(50) → massimo 50 caratteri
    # - unique=True → non possono esistere due ruoli con lo stesso nome
    # - nullable=False → il campo è obbligatorio
    name = db.Column(db.String(50), unique=True, nullable=False)
    
    # Relazione con la tabella User:
    # - "User" → nome del modello collegato
    # - back_populates="role" → collega la relazione inversa definita nel modello User
    # Questa relazione permette: role.users → lista degli utenti che hanno quel ruolo
    users = db.relationship("User", back_populates="role")