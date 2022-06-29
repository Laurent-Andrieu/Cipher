# [Cipher](https://github.com/Laurent-Andrieu/Cipher)
Programme de chiffrement et déchiffrement AES-256 Galois/Counter Mode (GCM) avec clé de 32 octets
---
## Dépendences
Les bibliothèques utilisées sont intégrée au fichier [requirements](https://github.com/Laurent-Andrieu/Cipher/blob/master/requirements.txt)
Pour les installer via **pip**:

`pip install -r requirements.txt`


---
## Utilisation
### Préliminaires
Pour chiffrer un fichier, renseignez dans le fichier [Creditentials.py](https://github.com/Laurent-Andrieu/Cipher/blob/master/Creditentials.py):
* un mot de passe dans dans le champs: `password=` 
* le nom du fichier dans le champs: `file=`


### Chiffrage d'un fichier

Le mot de passe est hashé en SHA-256 pour obtenir une clée de 32 octets

_Prévoir un mot de passe fort pour le chiffrement_

Faites simplement appel au fichier [Encrypt.py](https://github.com/Laurent-Andrieu/Cipher/blob/master/Encrypt.py)


### Déchiffrage d'un fichier

Faites simplement appel au fichier [Decrypt.py](https://github.com/Laurent-Andrieu/Cipher/blob/master/Decrypt.py)
