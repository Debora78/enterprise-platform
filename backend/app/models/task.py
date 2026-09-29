# Importa l'istanza di SQLAlchemy per definire il modello
from ..extensions import db

# Definisce il modello Task, che rappresenta la tabella "tasks"
class Task(db.Model):
    
    # Nome esplicito della tabella nel database PostgreSQL
    __tablename__ = "tasks"
    
    # Colonna ID:
    # - Integer → numero intero
    # - primary_key=True → chiave primaria della tabella
    id = db.Column(db.Integer, primary_key=True)
    
    # Colonna TITLE:
    # - String(200) → massimo 200 caratteri
    # - nullable=False → il titolo è obbligatorio
    title = db.Column(db.String(200), nullable=False)
    
    # Colonna DESCRIPTION:
    # - Text → testo lungo (descrizione del task)
    # - nullable=True → può essere vuoto
    description = db.Column(db.Text)
    
    # Colonna STATUS:
    # - String(50) → stato del task (pending, completed, ecc.)
    # - default="pending" → valore predefinito
    status = db.Column(db.String(50), default="pending")
    
    # Colonna USER_ID:
    # - Integer → numero intero
    # - ForeignKey → collega questa colonna alla colonna "id" della tabella "users"
    # - nullable=False → ogni task deve appartenere a un utente
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    