
![GitHub Logo](assets/img/logo.png)

# Linux Senegal Bot

Un assistant virtuel qui accompagne les membres de la communauté Linux Sénégal

### Prérequis

Python versions 2.7, 3.3+.

### Installation

Installer à partir de la source avec:

```
git clone https://github.com/Linux-Senegal/Linux-Senegal-Bot.git
cd Linux-Senegal-Bot
pip install -r requirements.txt
```
## Guide de démarrage

Pour commencer, vous aurez besoin d'un TOKEN d'accès.

Pour générer un jeton d'accès, vous devez parler à [BotFather](https://telegram.me/botfather) et suivez quelques étapes simples (décrit [ici](https://core.telegram.org/bots#6-botfather)).

Puis ajouter votre TOKEN au fichier .env
```
echo TOKEN=MA_VARIABLE_TOKEN > .env
```
Vous devriez être capable d'exécuter l'application sur votre propre système via la commande suivante et en visitant http://localhost:5000

```
python app.py
```


## Développer avec

* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - Cette bibliothèque fournit une interface Python pour l'API Telegram Bot
* [flask](https://github.com/pallets/flask) - Le micro framework Python pour la construction d'applications web.

## contribuer

Les contributions de toutes tailles sont les bienvenues. S'il vous plaît examiner notre [guide de contribution](CONTRIBUTING.md) pour commencer. Vous pouvez également aider en [rapportant des erreurs](https://github.com/Linux-Senegal/Linux-Senegal-Bot/issues/new).

## License

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails
