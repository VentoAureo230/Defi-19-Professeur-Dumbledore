"""Tests unitaires pour le module de reconnaissance de sorts."""
import pytest
import sys
import os

# Ajouter le répertoire src au path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from spell_recognition import SpellRecognizer


class TestSpellRecognizer:
    """Tests pour la classe SpellRecognizer."""
    
    def setup_method(self):
        """Setup exécuté avant chaque test."""
        self.recognizer = SpellRecognizer()
    
    def test_init(self):
        """Test de l'initialisation du recognizer."""
        assert self.recognizer is not None
        assert len(self.recognizer.get_spells()) > 0
        assert len(self.recognizer.get_spell_variants()) > 0
    
    def test_get_spells(self):
        """Test de récupération des sorts."""
        spells = self.recognizer.get_spells()
        assert isinstance(spells, dict)
        assert "lumos" in spells
        assert "expelliarmus" in spells
        assert "avada kedavra" in spells
    
    def test_get_spell_variants(self):
        """Test de récupération des variantes."""
        variants = self.recognizer.get_spell_variants()
        assert isinstance(variants, dict)
        assert "lumos" in variants
        assert isinstance(variants["lumos"], list)
        assert len(variants["lumos"]) > 0
    
    def test_recognize_spell_from_text_valid(self):
        """Test de reconnaissance de sort valide."""
        # Test avec texte exact
        effect = self.recognizer.recognize_spell_from_text("lumos")
        assert effect is not None
        assert "💡" in effect
        
        # Test avec variante phonétique
        effect = self.recognizer.recognize_spell_from_text("lumoss")
        assert effect is not None
        assert "💡" in effect
        
        # Test insensible à la casse
        effect = self.recognizer.recognize_spell_from_text("LUMOS")
        assert effect is not None
    
    def test_recognize_spell_from_text_invalid(self):
        """Test de reconnaissance de sort invalide."""
        # Texte vide
        effect = self.recognizer.recognize_spell_from_text("")
        assert effect is None
        
        # Texte None
        effect = self.recognizer.recognize_spell_from_text(None)
        assert effect is None
        
        # Texte inexistant
        effect = self.recognizer.recognize_spell_from_text("abracadabra")
        assert effect is None
    
    def test_recognize_spell_from_text_all_spells(self):
        """Test de reconnaissance pour tous les sorts."""
        test_cases = [
            ("expelliarmus", "🪄"),
            ("imperio", "👁️"),
            ("nox", "🌑"),
            ("accio", "📦"),
            ("stupefix", "💥"),
            ("wingardium leviosa", "🕴️"),
            ("avada kedavra", "💀")
        ]
        
        for spell_text, expected_emoji in test_cases:
            effect = self.recognizer.recognize_spell_from_text(spell_text)
            assert effect is not None, f"Sort '{spell_text}' non reconnu"
            assert expected_emoji in effect, f"Emoji incorrect pour '{spell_text}'"
    
    def test_is_valid_spell(self):
        """Test de validation des noms de sorts."""
        assert self.recognizer.is_valid_spell("lumos") is True
        assert self.recognizer.is_valid_spell("LUMOS") is True
        assert self.recognizer.is_valid_spell("expelliarmus") is True
        assert self.recognizer.is_valid_spell("abracadabra") is False
        assert self.recognizer.is_valid_spell("") is False
    
    def test_spell_variants_completeness(self):
        """Test que toutes les formules ont des variantes."""
        spells = self.recognizer.get_spells()
        variants = self.recognizer.get_spell_variants()
        
        for spell in spells:
            assert spell in variants, f"Sort '{spell}' n'a pas de variantes définies"
            assert len(variants[spell]) > 0, f"Sort '{spell}' a une liste de variantes vide"
    
    def test_spell_text_with_context(self):
        """Test de reconnaissance dans un contexte plus large."""
        # Sort dans une phrase
        effect = self.recognizer.recognize_spell_from_text("Je lance lumos pour éclairer")
        assert effect is not None
        assert "💡" in effect
        
        # Sort avec du bruit
        effect = self.recognizer.recognize_spell_from_text("euh... expelliarmus!")
        assert effect is not None
        assert "🪄" in effect