"""
Application Flask pour la reconnaissance vocale de sorts Harry Potter.
"""
from flask import Flask, render_template_string, request
from src.spell_recognition import SpellRecognizer


def create_app():
    """Factory pour créer l'application Flask."""
    app = Flask(__name__)
    spell_recognizer = SpellRecognizer()
    
    # Template HTML intégré
    html_template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Formules Magiques</title>
        <meta charset="utf-8">
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #f0f8ff; }
            .container { max-width: 600px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
            h1 { color: #4a4a4a; text-align: center; }
            button { background: #007bff; color: white; border: none; padding: 15px 30px; font-size: 16px; border-radius: 5px; cursor: pointer; width: 100%; }
            button:hover { background: #0056b3; }
            .result { margin-top: 20px; padding: 15px; border-radius: 5px; }
            .speech { background: #e9ecef; }
            .effect { background: #d4edda; color: #155724; font-size: 18px; font-weight: bold; }
            .error { background: #f8d7da; color: #721c24; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🧙‍♂️ Reconnaissance de Formules Magiques</h1>
            <form method="POST">
                <button type="submit">🎤 Prononcer une formule</button>
            </form>
            {% if texte %}
                <div class="result speech">
                    <strong>Vous avez dit :</strong> {{ texte }}
                </div>
            {% endif %}
            {% if effet %}
                <div class="result {% if 'Erreur' in effet or 'Aucune' in effet %}error{% else %}effect{% endif %}">
                    {{ effet }}
                </div>
            {% endif %}
            <div style="margin-top: 30px; font-size: 12px; color: #6c757d;">
                <strong>Sorts disponibles :</strong><br>
                Imperio, Expelliarmus, Lumos, Nox, Accio, Stupefix, Wingardium Leviosa, Avada Kedavra
            </div>
        </div>
    </body>
    </html>
    '''
    
    @app.route('/', methods=['GET', 'POST'])
    def index():
        """Route principale de l'application."""
        texte = None
        effet = None
        
        if request.method == 'POST':
            texte, effet = spell_recognizer.recognize_spell_from_audio()
            if not effet:
                effet = "Aucune formule magique reconnue."
        
        return render_template_string(html_template, texte=texte, effet=effet)
    
    @app.route('/health')
    def health():
        """Endpoint de santé pour les checks Docker."""
        return {"status": "ok", "spells_count": len(spell_recognizer.get_spells())}
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=False)