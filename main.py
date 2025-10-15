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
    
    # Configuration du port via variable d'environnement
    port = int(os.environ.get('PORT', 5000))
    print(f"📡 Serveur disponible sur http://localhost:{port}")
    print("🎤 Assurez-vous que votre microphone est connecté !")
    
    # Vérification de la clé secrète en production
    if not os.environ.get('FLASK_SECRET_KEY'):
        print("⚠️  ATTENTION: Variable FLASK_SECRET_KEY non définie. Génération automatique.")
        print("   En production, définissez cette variable avec une clé forte.")
    
    app = create_app()
    app.run(host='0.0.0.0', port=port, debug=False)


if __name__ == '__main__':
    main()