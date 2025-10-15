"""
Module de reconnaissance vocale des sorts Harry Potter.
"""

from typing import Dict, List, Optional, Tuple

import speech_recognition as sr


# Constantes pour les noms de sorts (évite la duplication)
SPELL_IMPERIO = "imperio"
SPELL_EXPELLIARMUS = "expelliarmus"
SPELL_LUMOS = "lumos"
SPELL_NOX = "nox"
SPELL_ACCIO = "accio"
SPELL_STUPEFIX = "stupefix"
SPELL_WINGARDIUM_LEVIOSA = "wingardium leviosa"
SPELL_AVADA_KEDAVRA = "avada kedavra"


class SpellRecognizer:
    """Classe principale pour la reconnaissance de formules magiques."""

    def __init__(self):
        """Initialise le reconnaisseur de sorts."""
        self.formules = {
            SPELL_IMPERIO: "👁️ L'adversaire est contrôlé !",
            SPELL_EXPELLIARMUS: "🪄 L'adversaire est désarmé !",
            SPELL_LUMOS: "💡 La baguette s'allume !",
            SPELL_NOX: "🌑 La lumière s'éteint !",
            SPELL_ACCIO: "📦 L'objet arrive !",
            SPELL_STUPEFIX: "💥 L'adversaire est étourdi !",
            SPELL_WINGARDIUM_LEVIOSA: "🕴️ L'objet lévite !",
            SPELL_AVADA_KEDAVRA: "💀 Sortilège de mort !",
        }

        self.variantes = {
            SPELL_IMPERIO: [SPELL_IMPERIO, "impero", "imperro"],
            SPELL_EXPELLIARMUS: [SPELL_EXPELLIARMUS, "expeliarmus", "expeliamus"],
            SPELL_LUMOS: [SPELL_LUMOS, "lumoss", "lumoz"],
            SPELL_NOX: [SPELL_NOX, "noks", "noxe"],
            SPELL_ACCIO: [SPELL_ACCIO, "akio", "acio", "action"],
            SPELL_STUPEFIX: ["stupefy", "stupefie", "stupify", "stupeflip"],
            SPELL_WINGARDIUM_LEVIOSA: [
                SPELL_WINGARDIUM_LEVIOSA,
                "wingardium levioza",
                "wingardium levioça",
            ],
            SPELL_AVADA_KEDAVRA: [SPELL_AVADA_KEDAVRA, "avada kadavra", "avada cadavra"],
        }

        self.recognizer = sr.Recognizer()

    def get_spells(self) -> Dict[str, str]:
        """Retourne la liste des sorts disponibles."""
        return self.formules.copy()

    def get_spell_variants(self) -> Dict[str, List[str]]:
        """Retourne les variantes phonétiques des sorts."""
        return self.variantes.copy()

    def recognize_spell_from_text(self, text: str) -> Optional[str]:
        """
        Reconnaît un sort à partir d'un texte.

        Args:
            text: Le texte à analyser

        Returns:
            L'effet du sort reconnu ou None si aucun sort n'est trouvé
        """
        if not text:
            return None

        text_lower = text.lower().strip()

        for formule, variants in self.variantes.items():
            if any(variant in text_lower for variant in variants):
                return self.formules[formule]

        return None

    def recognize_spell_from_audio(
        self, timeout: int = 5, language: str = "fr-FR"
    ) -> Tuple[Optional[str], Optional[str]]:
        """
        Reconnaît un sort à partir de l'audio du microphone.

        Args:
            timeout: Temps d'écoute maximum en secondes
            language: Langue de reconnaissance

        Returns:
            Tuple (texte_reconnu, effet_sort) ou (None, None) en cas d'erreur
        """
        try:
            with sr.Microphone() as source:
                print("Écoute en cours... Parlez maintenant !")
                audio = self.recognizer.listen(source, timeout=timeout)

            text = self.recognizer.recognize_google(audio, language=language)
            effect = self.recognize_spell_from_text(text)

            return text, effect

        except sr.UnknownValueError:
            return None, "Impossible de comprendre l'audio"
        except sr.RequestError as e:
            return None, f"Erreur du service de reconnaissance: {e}"
        except Exception as e:
            return None, f"Erreur inattendue: {e}"

    def is_valid_spell(self, spell_name: str) -> bool:
        """Vérifie si un nom de sort est valide."""
        return spell_name.lower() in self.formules
