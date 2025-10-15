#!/usr/bin/env python3
"""
Point d'entrée principal pour l'application de reconnaissance vocale Harry Potter.
Usage: python main.py
"""
import sys
import os

# Ajouter le répertoire src au path pour les imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.flask_app import create_app


def main():
    """Fonction principale pour lancer l'application."""
    print("🧙‍♂️ Démarrage de l'application de reconnaissance de sorts Harry Potter...")
    print("📡 Serveur disponible sur http://localhost:5000")
    print("🎤 Assurez-vous que votre microphone est connecté !")
    
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=False)


if __name__ == '__main__':
    main()