# Importa la classe SQLAlchemy per gestire il database
from flask_sqlalchemy import SQLAlchemy

# Importa la classe Migrate per gestire le migrazioni del DB
from flask_migrate import Migrate

# Crea l'istanza di SQLAlchemy.
# db sarà l'oggetto principale che userai per:
# - definire i modelli (class User(db.Model))
# - eseguire query
# - interagire con il database
db = SQLAlchemy()

# Crea l'istanza di Migrate.
# migrate collega Flask, SQLAlchemy e Alembic per permettere:
# - creare migrazioni
# - aggiornare il database
# - gestire versioni dello schema
migrate = Migrate()