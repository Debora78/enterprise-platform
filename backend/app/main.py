
# Importa la factory function che crea e configura l'app Flask
from app import create_app

# Crea l'app Flask usando la factory: qui nasce l'applicazione
app = create_app()

# Questo blocco viene eseguito SOLO se il file viene lanciato direttamente:
# python main.py
# __name__ sarà "__main__"
# Se invece il file viene importato, il blocco NON viene eseguito.
if __name__ == "__main__":
    
    # Avvia il server Flask in modalità debug (utile per sviluppo)
    app.run(debug=True)