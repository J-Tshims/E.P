# Projet EP

Ce dépôt contient le projet Django "EP".

Sauvegarde et récupération :

- Pour sauvegarder : pousse le code sur un dépôt distant (GitHub/GitLab) privé.
- La base de données locale `db.sqlite3` est exclue du dépôt par défaut. Utilise `python manage.py dumpdata > dump_all.json` pour exporter les données.
- Ne commite pas de secrets. Mets les variables sensibles dans un fichier `.env` (qui est ignoré).

Commandes rapides :

```bash
# installer les dépendances
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# lancer le serveur
python manage.py migrate
python manage.py runserver
```
