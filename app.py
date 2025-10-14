from flask import Flask, render_template_string, request
import speech_recognition as sr

app = Flask(__name__)

# Formules et effets
formules = {
    "imperio": " L'adversaire est contrôlé !",
    "expelliarmus": "🪄 L'adversaire est désarmé !",
    "lumos": "💡 La baguette s'allume !",
    "nox": "🌑 La lumière s'éteint !",
    "accio": "📦 L'objet arrive !",
    "stupefix": "💥 L'adversaire est étourdi !",
    "wingardium leviosa": "🕴️ L'objet lévite !",
    "avada kedavra": "💀 Sortilège de mort !"
}

# Variantes phonétiques pour chaque formule
variantes = {
    "imperio": ["impero", "imperro"],
    "expelliarmus": ["expelliarmus", "expeliarmus", "expeliamus"],
    "lumos": ["lumos", "lumoss", "lumoz"],
    "nox": ["nox", "noks", "noxe"],
    "accio": ["accio", "akio", "acio", "action"],
    "stupefix": ["stupefy", "stupefie", "stupify" , "stupeflip"],
    "wingardium leviosa": ["wingardium leviosa", "wingardium levioza", "wingardium levioça"],
    "avada kedavra": ["avada kedavra", "avada kadavra", "avada cadavra"]
}

html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Formules Magiques</title>
</head>
<body>
    <h1>🧙‍♂️ Reconnaissance de Formules Magiques</h1>
    <form method="POST">
        <button type="submit">🎤 Prononcer une formule</button>
    </form>
    {% if texte %}
        <p><strong>Vous avez dit :</strong> {{ texte }}</p>
    {% endif %}
    {% if effet %}
        <h2 style="color:green">{{ effet }}</h2>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    texte = None
    effet = None
    if request.method == 'POST':
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Écoute en cours... Parlez maintenant !")
            audio = recognizer.listen(source, timeout=5)
        try:
            texte = recognizer.recognize_google(audio, language="fr-FR")
            texte_lower = texte.lower()
            for formule, mots in variantes.items():
                if any(var in texte_lower for var in mots):
                    effet = formules[formule]
                    break
            if not effet:
                effet = "Aucune formule magique reconnue."
        except:
            effet = "Erreur de reconnaissance vocale."
    return render_template_string(html, texte=texte, effet=effet)

if __name__ == '__main__':
    app.run(debug=True)