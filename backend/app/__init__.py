# Importa la classe Flask, necessaria per creare l'applicazione
from flask import Flask

# Importa la classe di configurazione che contiene:
# - SECRET_KEY
# - SQLALCHEMY_DATABASE_URI
# - altre impostazioni dell'app
from .config import Config

# Importa le istanze di SQLAlchemy e Flask-Migrate
# Queste sono create in utils/extensions.py
from .extensions import db, migrate


# Factory function: crea e configura l'app Flask
# Questo approccio è professionale e permette:
# - test più semplici
# - modularità
# - compatibilità con Flask-Migrate
def create_app():
    
    # Crea l'istanza dell'app Flask.
    # __name__ indica il modulo corrente e aiuta Flask a trovare template/static.
    app = Flask(__name__)
    
    # Carica tutte le configurazioni dalla classe Config:
    # - database
    # - secret key
    # - opzioni varie
    app.config.from_object(Config)


    # Inizializza SQLAlchemy collegandolo all'app Flask.
    # Da questo momento db è "agganciato" all'app e può creare modelli e tabelle
    db.init_app(app)
    
    # Inizializza Flask-Migrate collegando:
    # - l'app Flask
    # - l'istanza db di SQLAlchemy
    # Questo permette di usare:
    #   flask db init
    #   flask db migrate
    #   flask db upgrade
    migrate.init_app(app, db)

    # 🔥 IMPORTANTE: importa i modelli QUI dentro.
    # Flask-Migrate deve vedere i modelli quando create_app() viene eseguita.
    # Se non li importi qui, Alembic non li rileva e non crea le tabelle.
    from .models.user import User
    from .models.role import Role
    from .models.task import Task

    # Restituisce l'app completamente configurata
    return app

