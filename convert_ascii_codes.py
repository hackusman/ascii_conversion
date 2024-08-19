# Liste des codes ASCII en décimal
ascii_codes = [55, 56, 54, 79, 115, 69, 114, 116, 107, 49, 50]

# Convertir les codes en caractères ASCII et les joindre en une seule chaîne
decoded_string = ''.join(chr(code) for code in ascii_codes)

# Afficher le résultat
print(decoded_string)

