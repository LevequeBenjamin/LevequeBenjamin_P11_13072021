[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

# BenjaminLeveque_P11_13072021

## Améliorez une application Web Python par des tests et du débogage

Le projet 11 de la formation Développeur d'application Python et l'amélioration d'une application web Python
par des tests et du débogage.

## Technologies
- Python
- Flask
- Pytest
- Locust

## Auteur
Lévêque Benjamin

--------------------
### Installation

Cet application web exécutable localement peut être installée en suivant les étapes décrites ci-dessous.

#### 1. Clonez le [repository](https://github.com/LevequeBenjamin/LevequeBenjamin_P11_13072021.git) à l'aide de la commande suivante :

```
$ git clone "https://github.com/LevequeBenjamin/BenjaminLeveque_P9_23062021.git"
``` 
(vous pouvez également télécharger le code en temps 
[qu'archive zip](https://github.com/LevequeBenjamin/LevequeBenjamin_P11_13072021/archive/refs/heads/master.zip))

#### 2. Exécutez l'application dans un environnement virtuel

Rendez-vous depuis un terminal à la racine du répertoire BenjaminLeveque_P11_13072021 avec la commande :
```
$ cd BenjaminLeveque_P11_13072021
```

Pour créez un environnement, utilisez la commande :

`$ python3 -m venv env` sous macos ou linux.

`$ python -m venv env` sous windows.

Pour activer l'environnement, exécutez la commande :

`$ source env/bin/activate` sous macos ou linux.

`$ env/Scripts/activate` sous windows.

#### 3. Installez les dépendances du projet avec la commande :
```
$ pip install -r requirements.txt
```
--------------------
### Usage

Pour lancer l'application utilisez les commandes :

```
$ export FLASK_APP=server.py
$ export FLASK_ENV=development
$ flask run
```
#### Puis rendez-vous sur votre [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

--------------------
### Tests

#### 1. Installez les dépendances du projet avec la commande :

```
$ pip install -r requirements--dev.txt
```

#### 2. Testez l'application avec `Pytest` :

```
$ coverage run -m pytest
```

#### 3. Générer un rapport de couverture avec `Coverage` :

```
$ pytest --cov=gudlft --cov-report html
```

#### 4. Testez les performances avec `Locust` :

```
$ locust --config tests/locust/master.conf
```
--------------------

Vous pouvez également tester les perfomances avec la commande suivante :

```
$ locust -f tests/locust/locust_file.py 
```
Une fois que vous avez démarré Locust en utilisant l'une des lignes de commande ci-dessus, vous devez
ouvrir un navigateur et le pointer vers [http://0.0.0.0:8089/](http://0.0.0.0:8089/). Ensuite, vous
devriez être accueilli avec quelque chose comme ceci :

Remplissez le formulaire et essayez-le !

![Screenshot](docs/Capture%20d’écran%20du%202021-07-24%2014-09-28.png)

![Screenshot](docs/Capture%20d’écran%20du%202021-07-24%2014-23-29.png)

![Screenshot](docs/Capture%20d’écran%20du%202021-07-24%2014-24-28.png)

Le lien vers la [documentation de Locust](https://docs.locust.io/en/stable/)

--------------------
