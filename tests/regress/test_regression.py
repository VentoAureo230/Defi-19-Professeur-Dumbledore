"""Tests de régression pour vérifier la stabilité des comportements."""
import pytest
import sys
import os
import json

# Ajouter le répertoire src au path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from spell_recognition import SpellRecognizer


class TestSpellRecognitionRegression:
    """Tests de régression pour la reconnaissance de sorts."""
    
    def setup_method(self):
        """Setup exécuté avant chaque test."""
        self.recognizer = SpellRecognizer()
        
        # Données de référence pour les tests de régression
        self.reference_spells = {
            "imperio": "👁️ L'adversaire est contrôlé !",
            "expelliarmus": "🪄 L'adversaire est désarmé !",
            "lumos": "💡 La baguette s'allume !",
            "nox": "🌑 La lumière s'éteint !",
            "accio": "📦 L'objet arrive !",
            "stupefix": "💥 L'adversaire est étourdi !",
            "wingardium leviosa": "🕴️ L'objet lévite !",
            "avada kedavra": "💀 Sortilège de mort !"
        }
        
        # Cas de test de référence avec résultats attendus
        self.reference_test_cases = [
            ("lumos", "💡 La baguette s'allume !"),
            ("lumoss", "💡 La baguette s'allume !"),
            ("EXPELLIARMUS", "🪄 L'adversaire est désarmé !"),
            ("Je lance accio", "📦 L'objet arrive !"),
            ("stupefy maintenant", "💥 L'adversaire est étourdi !"),
            ("wingardium leviosa doucement", "🕴️ L'objet lévite !"),
            ("texto inexistant", None),
            ("", None)
        ]
    
    def test_spell_effects_unchanged(self):
        """Test que les effets des sorts n'ont pas changé."""
        current_spells = self.recognizer.get_spells()
        
        for spell, expected_effect in self.reference_spells.items():
            assert spell in current_spells, f"Sort '{spell}' manquant"
            actual_effect = current_spells[spell]
            assert actual_effect == expected_effect, (
                f"Effet du sort '{spell}' a changé: "
                f"attendu '{expected_effect}', reçu '{actual_effect}'"
            )
    
    def test_spell_count_stable(self):
        """Test que le nombre de sorts reste stable."""
        current_spells = self.recognizer.get_spells()
        expected_count = len(self.reference_spells)
        actual_count = len(current_spells)
        
        assert actual_count >= expected_count, (
            f"Nombre de sorts a diminué: attendu au moins {expected_count}, "
            f"reçu {actual_count}"
        )
    
    def test_reference_cases_regression(self):
        """Test des cas de référence pour détecter les régressions."""
        for input_text, expected_output in self.reference_test_cases:
            actual_output = self.recognizer.recognize_spell_from_text(input_text)
            assert actual_output == expected_output, (
                f"Régression détectée pour '{input_text}': "
                f"attendu '{expected_output}', reçu '{actual_output}'"
            )
    
    def test_variant_recognition_stability(self):
        """Test que toutes les variantes continuent de fonctionner."""
        variants = self.recognizer.get_spell_variants()
        spells = self.recognizer.get_spells()
        
        for spell, variant_list in variants.items():
            expected_effect = spells[spell]
            
            for variant in variant_list:
                actual_effect = self.recognizer.recognize_spell_from_text(variant)
                assert actual_effect == expected_effect, (
                    f"Variante '{variant}' du sort '{spell}' ne fonctionne plus: "
                    f"attendu '{expected_effect}', reçu '{actual_effect}'"
                )
    
    def test_case_insensitive_stability(self):
        """Test que la reconnaissance reste insensible à la casse."""
        test_cases = [
            "lumos",
            "LUMOS", 
            "Lumos",
            "LuMoS"
        ]
        
        expected_effect = self.reference_spells["lumos"]
        
        for case_variant in test_cases:
            actual_effect = self.recognizer.recognize_spell_from_text(case_variant)
            assert actual_effect == expected_effect, (
                f"Sensibilité à la casse détectée pour '{case_variant}'"
            )
    
    def test_performance_regression(self):
        """Test simple de performance pour détecter les régressions."""
        import time
        
        # Test avec 100 reconnaissances
        start_time = time.time()
        for _ in range(100):
            self.recognizer.recognize_spell_from_text("lumos")
        end_time = time.time()
        
        # Ne devrait pas prendre plus de 1 seconde pour 100 appels
        duration = end_time - start_time
        assert duration < 1.0, (
            f"Régression de performance détectée: "
            f"{duration:.2f}s pour 100 reconnaissances"
        )
    
    def test_memory_stability(self):
        """Test que l'initialisation reste stable en mémoire."""
        # Créer plusieurs instances pour vérifier qu'il n'y a pas de fuite
        recognizers = []
        for _ in range(10):
            recognizers.append(SpellRecognizer())
        
        # Vérifier que toutes les instances sont cohérentes
        reference_spells = recognizers[0].get_spells()
        for i, recognizer in enumerate(recognizers[1:], 1):
            assert recognizer.get_spells() == reference_spells, (
                f"Instance {i} incohérente avec la référence"
            )