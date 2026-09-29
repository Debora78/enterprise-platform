# Importa l'istanza di SQLAlchemy per definire il modello
from ..extensions import db

# Importa funzioni per creare hash sicuri della password e verificarli
from werkzeug.security import generate_password_hash, check_password_hash

# Definisce il modello User, che rappresenta la tabella "users"
class User(db.Model):
    
    # Nome esplicito della tabella nel database PostgreSQL
    __tablename__ = "users"
    
    
     # Colonna ID:
    # - Integer → numero intero
    # - primary_key=True → chiave primaria della tabella
    id = db.Column(db.Integer, primary_key=True)
    
    # Colonna EMAIL:
    # - String(120) → massimo 120 caratteri
    # - unique=True → non possono esistere due utenti con la stessa email
    # - nullable=False → il campo è obbligatorio
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    # Colonna PASSWORD_HASH:
    # - String(255) → contiene l'hash della password (non la password in chiaro!)
    # - nullable=False → obbligatoria
    password_hash = db.Column(db.String(255), nullable=False)
    
    # Colonna ROLE_ID:
    # - Integer → numero intero
    # - ForeignKey → collega questa colonna alla colonna "id" della tabella "roles"
    # - nullable=False → ogni utente deve avere un ruolo
    # - la foreign key è formata da nome_tabella . nome_colonna
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False)
    
    # Relazione con il modello Role:
    # - "Role" → nome del modello collegato
    # - back_populates="users" → collega la relazione inversa definita nel modello Role
    # Questa relazione permette: user.role → ruolo dell'utente
    role = db.relationship("Role", back_populates="users")
    
    # Relazione con il modello Task:
    # - "Task" → nome del modello collegato
    # - backref="user" → permette a Task di accedere all'utente tramite task.user
    # - lazy=True → carica i task solo quando servono
    # Questa relazione permette: user.tasks → lista dei task associati all'utente
    tasks = db.relationship("Task", backref="user", lazy=True)
    
     # Metodo per impostare la password:
    # - prende la password in chiaro
    # - la trasforma in un hash sicuro
    # - salva l'hash nella colonna password_hash
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    # Metodo per verificare la password:
    # - prende la password inserita dall'utente
    # - confronta l'hash salvato con l'hash della password inserita
    # - ritorna True se coincidono, False altrimenti
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)    