# Sudoku Solver

Projet d’algorithmique consistant à implémenter un solveur automatique de grilles de Sudoku.  
Ce projet met l’accent sur la logique, la récursivité et la résolution de problèmes par satisfaction de contraintes.

---

## Objectifs du projet

- Implémenter un solveur de Sudoku générique
- Mettre en pratique un algorithme de backtracking
- Travailler sur un problème classique de satisfaction de contraintes
- Produire un code clair, lisible et facilement extensible

---

## Concepts et compétences mobilisés

- Algorithmique
- Backtracking
- Programmation récursive
- Recherche exhaustive avec élagage
- Manipulation de structures de données

---

## Principe de résolution

Le solveur fonctionne selon les étapes suivantes :

1. Lecture de la grille initiale
2. Recherche d’une case vide
3. Test des valeurs possibles (1 à 9)
4. Vérification des contraintes :
   - unicité sur la ligne
   - unicité sur la colonne
   - unicité dans le sous-carré 3x3
5. Appel récursif jusqu’à résolution complète ou retour arrière en cas d’échec


