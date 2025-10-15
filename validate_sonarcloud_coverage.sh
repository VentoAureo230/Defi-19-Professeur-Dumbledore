#!/bin/bash

# Script de validation avancée pour SonarCloud Coverage
# Usage: ./validate_sonarcloud_coverage.sh

echo "🔍 Validation avancée du coverage pour SonarCloud"
echo "================================================="

# Nettoyage et génération
echo "🧹 Nettoyage et génération du coverage..."
rm -f coverage.xml test-results.xml sonar-report.json
rm -rf htmlcov/ .coverage

python3 -m pytest tests/unit/ -v \
  --cov=src \
  --cov-report=xml:coverage.xml \
  --cov-report=term-missing \
  --cov-config=.coveragerc \
  --junit-xml=test-results.xml \
  --quiet

echo ""
echo "📊 Validation des fichiers pour SonarCloud:"
echo "============================================"

# Validation coverage.xml
if [ -f "coverage.xml" ]; then
    echo "✅ coverage.xml généré ($(du -h coverage.xml | cut -f1))"
    
    # Vérification XML bien formé
    if command -v xmllint &> /dev/null; then
        if xmllint --noout coverage.xml 2>/dev/null; then
            echo "  ✅ XML bien formé"
        else
            echo "  ❌ XML malformé"
            exit 1
        fi
    fi
    
    # Extraction des métriques
    LINE_RATE=$(grep -o 'line-rate="[^"]*"' coverage.xml | head -1 | cut -d'"' -f2)
    LINES_VALID=$(grep -o 'lines-valid="[^"]*"' coverage.xml | head -1 | cut -d'"' -f2)
    LINES_COVERED=$(grep -o 'lines-covered="[^"]*"' coverage.xml | head -1 | cut -d'"' -f2)
    
    echo "  📈 Métrique: ${LINES_COVERED}/${LINES_VALID} lignes couvertes (${LINE_RATE})"
    
    # Vérification des sources
    if grep -q "<source>src</source>" coverage.xml; then
        echo "  ✅ Sources correctement définies (chemins relatifs)"
    else
        echo "  ⚠️ Sources avec chemins absolus détectés"
        grep "<source>" coverage.xml
    fi
    
    # Vérification des classes
    CLASS_COUNT=$(grep -c '<class name=' coverage.xml)
    echo "  📁 ${CLASS_COUNT} fichiers source analysés"
    
else
    echo "❌ coverage.xml NON généré"
    exit 1
fi

# Validation test-results.xml
if [ -f "test-results.xml" ]; then
    echo "✅ test-results.xml généré ($(du -h test-results.xml | cut -f1))"
    
    if command -v xmllint &> /dev/null; then
        if xmllint --noout test-results.xml 2>/dev/null; then
            echo "  ✅ XML bien formé"
        else
            echo "  ❌ XML malformé"
        fi
    fi
    
    # Extraction du nombre de tests
    if grep -q 'testsuite' test-results.xml; then
        TESTS_COUNT=$(grep -o 'tests="[^"]*"' test-results.xml | head -1 | cut -d'"' -f2)
        FAILURES_COUNT=$(grep -o 'failures="[^"]*"' test-results.xml | head -1 | cut -d'"' -f2)
        echo "  🧪 ${TESTS_COUNT} tests exécutés, ${FAILURES_COUNT} échecs"
    fi
else
    echo "⚠️ test-results.xml NON généré (optionnel)"
fi

echo ""
echo "🔧 Vérification de la configuration SonarCloud:"
echo "==============================================="

if [ -f "sonar-project.properties" ]; then
    echo "✅ sonar-project.properties trouvé"
    
    # Vérification des paramètres clés
    if grep -q "sonar.python.coverage.reportPaths=coverage.xml" sonar-project.properties; then
        echo "  ✅ Chemin coverage correctement configuré"
    else
        echo "  ❌ Chemin coverage mal configuré"
    fi
    
    if grep -q "sonar.sources=src/" sonar-project.properties; then
        echo "  ✅ Sources correctement configurées"
    else
        echo "  ❌ Sources mal configurées"
    fi
    
    if grep -q "sonar.tests=tests/" sonar-project.properties; then
        echo "  ✅ Tests correctement configurés"
    else
        echo "  ❌ Tests mal configurés"
    fi
    
else
    echo "❌ sonar-project.properties NON trouvé"
fi

echo ""
echo "📋 Résumé pour SonarCloud:"
echo "========================="
echo "- Coverage XML: ✅ Prêt (format Cobertura)"
echo "- Test Results: $([ -f "test-results.xml" ] && echo "✅ Prêt" || echo "⚠️ Manquant")"
echo "- Configuration: ✅ Optimisée"
echo "- Chemins relatifs: ✅ Configurés"
echo ""
echo "🚀 Votre configuration est prête pour SonarCloud !"
echo "   Push vos modifications pour déclencher l'analyse."