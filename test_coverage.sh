#!/bin/bash

# Script de test local pour vérifier la génération du coverage
# Usage: ./test_coverage.sh

echo "🧪 Test local de génération de coverage pour SonarCloud"
echo "========================================================"

# Nettoyage des anciens fichiers
echo "🧹 Nettoyage des anciens rapports..."
rm -f coverage.xml test-results.xml
rm -rf htmlcov/ .coverage

# Installation des dépendances
echo "📦 Installation des dépendances..."
python3 -m pip install -r requirements.txt

# Exécution des tests avec coverage
echo "🧪 Exécution des tests avec génération de coverage..."
python3 -m pytest tests/unit/ -v \
  --cov=src \
  --cov-report=xml:coverage.xml \
  --cov-report=html:htmlcov \
  --cov-report=term-missing \
  --cov-config=.coveragerc \
  --junit-xml=test-results.xml

# Vérification des fichiers générés
echo ""
echo "📊 Vérification des fichiers générés:"
echo "-------------------------------------"

if [ -f "coverage.xml" ]; then
    echo "✅ coverage.xml généré ($(du -h coverage.xml))"
    echo "📋 Premières lignes du fichier coverage.xml:"
    head -10 coverage.xml
else
    echo "❌ coverage.xml NON généré"
fi

echo ""
if [ -f "test-results.xml" ]; then
    echo "✅ test-results.xml généré ($(du -h test-results.xml))"
else
    echo "❌ test-results.xml NON généré"
fi

echo ""
if [ -d "htmlcov" ]; then
    echo "✅ Rapport HTML généré dans htmlcov/"
    echo "🌐 Ouvrir htmlcov/index.html dans un navigateur pour voir le rapport"
else
    echo "❌ Rapport HTML NON généré"
fi

echo ""
echo "🔍 Contenu du répertoire:"
ls -la *.xml htmlcov/ 2>/dev/null || echo "Aucun fichier de rapport trouvé"

echo ""
echo "✅ Test de génération de coverage terminé"
echo "📝 Ces fichiers doivent être générés pour que SonarCloud fonctionne:"
echo "   - coverage.xml (rapport de couverture)"
echo "   - test-results.xml (résultats des tests)"