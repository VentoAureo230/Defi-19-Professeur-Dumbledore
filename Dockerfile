# ===============================================================================
# Dockerfile pour l'application Harry Potter Spell Voice Recognition
# ===============================================================================

# Image de base Python 3.11 slim pour optimiser la taille
FROM python:3.11-slim

# Métadonnées de l'image
LABEL maintainer="DevOps Team"
LABEL description="Harry Potter Spell Voice Recognition Application"
LABEL version="1.0.0"

# Variables d'environnement
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_APP=src.flask_app:create_app \
    FLASK_ENV=production \
    PORT=5000

# Répertoire de travail
WORKDIR /app

# Installation des dépendances système nécessaires pour audio
RUN apt-get update && apt-get install -y \
    gcc \
    portaudio19-dev \
    python3-dev \
    libasound2-dev \
    && rm -rf /var/lib/apt/lists/*

# Copie du fichier requirements en premier pour optimiser le cache Docker
COPY requirements.txt .

# Installation des dépendances Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copie du code source
COPY src/ src/
COPY main.py .

# Création d'un utilisateur non-root pour la sécurité
RUN groupadd -r appuser && useradd -r -g appuser appuser
RUN chown -R appuser:appuser /app
USER appuser

# Exposition du port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1

# Commande par défaut
CMD ["python", "main.py"]

# ===============================================================================
# Instructions d'utilisation:
# 
# Build:    docker build -t harrypotter-spell-voice .
# Run:      docker run -p 5000:5000 harrypotter-spell-voice
# Health:   docker run --rm -d --name spell-app -p 5000:5000 harrypotter-spell-voice
# ===============================================================================