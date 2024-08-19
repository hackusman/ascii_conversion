# Décodage de Codes ASCII en Python

## Description

Ce script Python convertit une liste de codes ASCII en une chaîne de caractères lisible en utilisant la fonction intégrée `chr()`. Les codes ASCII sont des valeurs décimales qui représentent des caractères dans le système de codage ASCII.

## Code

Voici le code complet :

```python
# Liste des codes ASCII en décimal
ascii_codes = [55, 56, 54, 79, 115, 69, 114, 116, 107, 49, 50]

# Convertir les codes en caractères ASCII et les joindre en une seule chaîne
decoded_string = ''.join(chr(code) for code in ascii_codes)

# Afficher le résultat
print(decoded_string)
```

## Explication du Code

1. **Liste des Codes ASCII**

   La variable `ascii_codes` contient une liste de codes ASCII sous forme de nombres décimaux. Chaque nombre correspond à un caractère spécifique dans le système ASCII.

   ```python
   ascii_codes = [55, 56, 54, 79, 115, 69, 114, 116, 107, 49, 50]
   ```

2. **Conversion des Codes en Caractères**

   La fonction `chr()` convertit chaque code ASCII en son caractère correspondant. La compréhension de liste est utilisée pour appliquer cette conversion à chaque code dans `ascii_codes`.

   ```python
   decoded_string = ''.join(chr(code) for code in ascii_codes)
   ```

3. **Affichage du Résultat**

   La chaîne résultante, qui est la combinaison de tous les caractères convertis, est affichée à l'écran avec `print()`.

   ```python
   print(decoded_string)
   ```

## Résultat

Lorsque vous exécutez ce script, il affiche la chaîne de caractères correspondante aux codes ASCII fournis. Pour le code donné, le résultat affiché est :

```
78sErkt12
```

## Utilisation

Pour utiliser ce script :

1. Copiez le code dans un fichier avec une extension `.py`, par exemple, `decode_ascii.py`.
2. Exécutez le script en utilisant Python. Assurez-vous d'avoir Python installé sur votre machine.

   ```sh
   python decode_ascii.py
   ```

3. Vous verrez le résultat dans la console.

## Conclusion

Ce script est un exemple simple de la manière dont on peut utiliser les codes ASCII pour manipuler des chaînes de caractères en Python. Il démontre également l'utilisation des fonctions intégrées et des compréhensions de liste pour rendre le code plus concis et lisible.


