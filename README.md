# 🧙‍♂️ Harry Potter Spell Voice Recognition

[![CI/CD Pipeline](https://github.com/VentoAureo230/Defi-19-Professeur-Dumbledore/actions/workflows/ci.yml/badge.svg)](https://github.com/VentoAureo230/Defi-19-Professeur-Dumbledore/actions/workflows/ci.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=VentoAureo230_Defi-19-Professeur-Dumbledore&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=VentoAureo230_Defi-19-Professeur-Dumbledore)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=VentoAureo230_Defi-19-Professeur-Dumbledore&metric=coverage)](https://sonarcloud.io/summary/new_code?id=VentoAureo230_Defi-19-Professeur-Dumbledore)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=VentoAureo230_Defi-19-Professeur-Dumbledore&metric=bugs)](https://sonarcloud.io/summary/new_code?id=VentoAureo230_Defi-19-Professeur-Dumbledore)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=VentoAureo230_Defi-19-Professeur-Dumbledore&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=VentoAureo230_Defi-19-Professeur-Dumbledore)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=VentoAureo230_Defi-19-Professeur-Dumbledore&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=VentoAureo230_Defi-19-Professeur-Dumbledore)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=VentoAureo230_Defi-19-Professeur-Dumbledore&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=VentoAureo230_Defi-19-Professeur-Dumbledore)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=VentoAureo230_Defi-19-Professeur-Dumbledore&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=VentoAureo230_Defi-19-Professeur-Dumbledore)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=VentoAureo230_Defi-19-Professeur-Dumbledore&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=VentoAureo230_Defi-19-Professeur-Dumbledore)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=VentoAureo230_Defi-19-Professeur-Dumbledore&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=VentoAureo230_Defi-19-Professeur-Dumbledore)

Application web Flask de reconnaissance vocale des sorts Harry Potter avec CI/CD complète.

## 🎯 Fonctionnalités

- **Reconnaissance vocale** de 8 sorts Harry Potter principaux
- **Interface web** intuitive avec Flask
- **Support multi-variantes** phonétiques pour chaque sort
- **API REST** avec endpoint de santé
- **Dockerisation** complète avec health checks
- **Tests** unitaires et de régression
- **CI/CD** GitHub Actions avec 8 étapes

## 🏗️ Architecture

```bash
harrypotter-spell-voice/
├── src/                          # Code source principal
│   ├── spell_recognition.py      # Module de reconnaissance
│   ├── flask_app.py             # Application Flask
│   └── __init__.py
├── tests/                        # Tests automatisés
│   ├── unit/                    # Tests unitaires
│   └── regress/                 # Tests de régression
├── .github/workflows/            # Pipeline CI/CD
│   └── ci.yml
├── main.py                      # Point d'entrée
├── Dockerfile                   # Image Docker
├── docker-compose.yml          # Orchestration locale
├── requirements.txt            # Dépendances Python
├── sonar-project.properties   # Configuration SonarCloud
└── README.md                  # Documentation
```

## 🚀 Démarrage rapide

### Prérequis

- Python 3.11+
- Docker et Docker Compose
- Microphone fonctionnel

### Installation locale

```bash
# Cloner le projet
git clone https://github.com/votre-username/harrypotter-spell-voice.git
cd harrypotter-spell-voice

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
python main.py
```

Application disponible sur http://localhost:5000

### Avec Docker

```bash
# Build et run avec Docker Compose
docker-compose up --build

# Ou avec Docker directement
docker build -t harrypotter-spell-voice .
docker run -p 5000:5000 harrypotter-spell-voice
```

## 🎪 Sorts reconnus

| Sort | Variantes | Effet |
|------|-----------|-------|
| **Lumos** | lumos, lumoss, lumoz | 💡 La baguette s'allume ! |
| **Expelliarmus** | expelliarmus, expeliarmus, expeliamus | 🪄 L'adversaire est désarmé ! |
| **Imperio** | impero, imperro | 👁️ L'adversaire est contrôlé ! |
| **Nox** | nox, noks, noxe | 🌑 La lumière s'éteint ! |
| **Accio** | accio, akio, acio, action | 📦 L'objet arrive ! |
| **Stupefix** | stupefy, stupefie, stupify, stupeflip | 💥 L'adversaire est étourdi ! |
| **Wingardium Leviosa** | wingardium leviosa, wingardium levioza | 🕴️ L'objet lévite ! |
| **Avada Kedavra** | avada kedavra, avada kadavra | 💀 Sortilège de mort ! |

## 🧪 Tests

```bash
# Tests unitaires
python -m pytest tests/unit/ -v

# Tests de régression
python -m pytest tests/regress/ -v

# Tests avec couverture
python -m pytest tests/ --cov=src --cov-report=html

# Qualité de code
flake8 src/
black --check src/
isort --check-only src/
```

## 🔄 Pipeline CI/CD

La pipeline GitHub Actions comprend 8 étapes séquentielles :

1. **🔨 Build** - Installation des dépendances et vérification
2. **🧪 Unit Tests** - Tests unitaires avec couverture de code
3. **🔄 Regression Tests** - Tests de non-régression
4. **📏 Code Quality** - Vérification PEP8 (flake8, black, isort)
5. **🔍 SonarCloud** - Analyse qualité et sécurité du code
6. **📦 Packaging** - Création du package wheel Python
7. **🐳 Dockerize** - Construction et test de l'image Docker
8. **🚀 Deploy** - Déploiement sur Docker Hub (main uniquement)

### Variables d'environnement requises

Configurer dans GitHub Settings → Secrets :

```
SONAR_TOKEN          # Token SonarCloud
DOCKERHUB_USERNAME   # Nom d'utilisateur Docker Hub
DOCKERHUB_TOKEN      # Token Docker Hub
```

## 🐳 Docker

### Images disponibles

- `harrypotter-spell-voice:latest` - Version stable
- `harrypotter-spell-voice:v1.0.0` - Version taguée
- `harrypotter-spell-voice:sha-abc123` - Version par commit

### Commands utiles

```bash
# Build local
docker build -t harrypotter-spell-voice .

# Run avec port mapping
docker run -p 5000:5000 harrypotter-spell-voice

# Health check
curl http://localhost:5000/health

# Logs en temps réel
docker logs -f container_name

# Inspection de l'image
docker inspect harrypotter-spell-voice
```

## 🔧 Configuration

### Variables d'environnement

| Variable | Description | Défaut |
|----------|-------------|--------|
| `FLASK_ENV` | Environnement Flask | `production` |
| `PORT` | Port d'écoute | `5000` |
| `PYTHONPATH` | Path Python | `/app` |

### SonarCloud

Modifier `sonar-project.properties` avec vos valeurs :

```properties
sonar.projectKey=votre-projet-key
sonar.organization=votre-organisation
```

## 📊 Métriques de qualité

- **Couverture de code** : > 80%
- **Complexité cyclomatique** : < 10
- **PEP8 compliance** : 100%
- **Tests** : Unitaires + Régression
- **Sécurité** : Scan Trivy sur images Docker

## 🚀 Déploiement

### Test local CI/CD avec Docker

```bash
# 1. Simuler le build
docker build -t harrypotter-spell-voice:test .

# 2. Test de l'application
docker run -d --name test-app -p 5000:5000 harrypotter-spell-voice:test

# 3. Health check
curl -f http://localhost:5000/health || echo "Health check failed"

# 4. Test interface
curl -f http://localhost:5000/ || echo "App check failed"

# 5. Nettoyage
docker stop test-app && docker rm test-app
```

### Déploiement production

1. **Push sur main** → Déclenchement automatique
2. **Validation** → Tous les jobs verts requis
3. **Build multi-arch** → AMD64 + ARM64
4. **Push Docker Hub** → Tags multiples
5. **Notification** → Résumé dans GitHub

## 🤝 Contribution

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/amazing-feature`)
3. Commit (`git commit -m 'Add amazing feature'`)
4. Push (`git push origin feature/amazing-feature`)
5. Ouvrir une Pull Request

## 📝 License

Projet éducatif - Tous droits réservés

## 🆘 Support

- **Issues** : [GitHub Issues](https://github.com/votre-username/harrypotter-spell-voice/issues)
- **Documentation** : [Wiki](https://github.com/votre-username/harrypotter-spell-voice/wiki)
- **CI/CD** : [Actions](https://github.com/votre-username/harrypotter-spell-voice/actions)

---

**Note** : Ce projet utilise PyAudio qui peut nécessiter des dépendances système spécifiques sur certaines plateformes. L'exécution via Docker évite ces problèmes de compatibilité.