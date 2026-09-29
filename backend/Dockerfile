
# ---------------------------------------------------------
# Immagine base Python 3.11 slim (leggera e stabile)
# ---------------------------------------------------------
FROM python:3.11-slim


# ---------------------------------------------------------
# Imposta la cartella di lavoro dentro il container
# ---------------------------------------------------------
WORKDIR /app


# ---------------------------------------------------------
# Copia il file requirements.txt per installare le dipendenze
# ---------------------------------------------------------
COPY requirements.txt  .

# ---------------------------------------------------------
# Installa le dipendenze Python senza cache (più leggero)
# ---------------------------------------------------------
RUN pip install --no-cache-dir -r requirements.txt


# ---------------------------------------------------------
# Copia tutto il progetto nel container
# ---------------------------------------------------------
COPY . . 

# ---------------------------------------------------------
# Rende la cartella /app parte del PYTHONPATH, così Python
# può importare correttamente il package "app" e i suoi moduli
# Aggiunge /app al PYTHONPATH per permettere gli import dei moduli
# ---------------------------------------------------------
ENV PYTHONPATH=/app

# ---------------------------------------------------------
# Comando di avvio del backend Flask
# ---------------------------------------------------------
CMD [ "python", "app/main.py" ]