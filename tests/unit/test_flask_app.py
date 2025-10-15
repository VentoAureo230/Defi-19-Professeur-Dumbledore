"""Tests unitaires pour l'application Flask."""
import pytest
import sys
import os
import json

# Ajouter le répertoire src au path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from flask_app import create_app


class TestFlaskApp:
    """Tests pour l'application Flask."""
    
    def setup_method(self):
        """Setup exécuté avant chaque test."""
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False  # Désactiver CSRF pour les tests
        self.client = self.app.test_client()
    
    def test_app_creation(self):
        """Test de création de l'application."""
        assert self.app is not None
        assert self.app.config['TESTING'] is True
    
    def test_home_page_get(self):
        """Test de la page d'accueil en GET."""
        response = self.client.get('/')
        assert response.status_code == 200
        assert b'Reconnaissance de Formules Magiques' in response.data
        assert b'Prononcer une formule' in response.data
    
    def test_health_endpoint(self):
        """Test de l'endpoint de santé."""
        response = self.client.get('/health')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['status'] == 'ok'
        assert 'spells_count' in data
        assert data['spells_count'] > 0
    
    def test_home_page_post_mock(self):
        """Test de la route de reconnaissance en POST (sans audio réel)."""
        # Ce test vérifie que le POST fonctionne même si l'audio échoue
        with self.app.test_request_context():
            response = self.client.post('/recognize')
            assert response.status_code == 200
            # En cas d'erreur audio, on doit avoir un message d'erreur ou "Aucune formule"
    
    def test_recognize_route_separation(self):
        """Test que les routes GET et POST sont bien séparées."""
        # GET sur /recognize devrait être interdit
        response = self.client.get('/recognize')
        assert response.status_code == 405  # Method Not Allowed
        
        # POST sur / devrait être interdit  
        response = self.client.post('/')
        assert response.status_code == 405  # Method Not Allowed
    
    def test_invalid_route(self):
        """Test d'une route inexistante."""
        response = self.client.get('/nonexistent')
        assert response.status_code == 404