#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple Bot pour répondre aux messages Telegram.

Ce programme est dédié au domaine public sous licence MIT.

Ce bot utilise la classe Updater pour gérer le bot.

Usage:
Example Echobot Basic.
"""
import logging
from os import environ
from flask import Flask
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

app = Flask(__name__)

# Activer la journalisation
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

@app.route('/')
def demarrer_page():
    """Appel pour démarrer le bot."""
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    demarrer()

    return """
    <h1>Démarrer Linux Senegal Bot</h1>
    <p>Il est actuellement {time}.</p>
    """.format(time=the_time)


@app.route('/stop')
def stop_page():
    """Appel pour arrête le bot."""
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    stop()

    return """
    <h1>Arrêter Linux Senegal Bot</h1>
    <p>Il est actuellement {time}.</p>
    """.format(time=the_time)



# Définition de quelques handlers commandes. Ceux-ci prennent généralement deux arguments bot et
# update. Error handlers reçoivent également l'objet TelegramError object dans error.
def start(bot, update):
    """Envoyer un message lorsque la commande /start est émis."""
    update.message.reply_text('Salut je suis l\'assistant virtuel de Linux Sénégal!')


def help(bot, update):
    """Envoyer un message lorsque la commande /help est émis."""
    update.message.reply_text('Oui j\'ai besoin de ton aide, as tu des idées de fonctionnalités pour un assistant virtuel novice comme moi ? Tape "/idee <ton idée>" Merci.')


def idees(bot, update):
    """Envoyer un message lorsque la commande /idees est émis."""
    update.message.reply_text("1. Afficher le prochain meetup > @dofbi\n2. Répondre à des questions de commande basique sur Linux par exemple Q: comment savoir ma distribution Linux ? R: Tapez la commande \"cat /etc/*release\" > @bay_dam\n")


def noms(bot, update):
    """Envoyer un message lorsque la commande /noms est émis."""
    update.message.reply_text("1. YEKSIL > Seydina Issa PATE")


def devs(bot, update):
    """Envoyer un message lorsque la commande /devs est émis."""
    update.message.reply_text("1. @dofbi\n2. Mouhamed Fadel\n3. @bay_dam\n4. Cheick Ahmed Tidiane Dieng\n5. James Gaglo")


def commande(bot, update, args, job_queue, chat_data):
    """Envoyer un message lorsque la commande /exe est émis."""
    chat_id = update.message.chat_id
    try:
        # evalution de args[0]
        try:
            info = eval(compile(args[0], '<string>', 'eval'))
            update.message.reply_text(info)
        except SyntaxError:
            update.message.reply_text('Erreur d\'évalution')

    except (IndexError, ValueError):
        update.message.reply_text('exemple: /exe <commande>')


def echo(bot, update):
    """Echo le message de l'utilisateur."""
    update.message.reply_text('Je ne comprends pas, je suis encoure de développement. Tape "/aide" pour m\'aider')


def error(bot, update, error):
    """Erreurs de journal causées par les Updates."""
    logger.warning('Update "%s" erreur provoquée "%s"', update, error)


def demarrer():
    """Démarrer le bot."""
    # Crée un EventHandler et transmet le Token de votre bot.
    updater = Updater(environ.get('TOKEN'))

    # Obtenir le répartiteur pour enregistrer les handlers
    dp = updater.dispatcher

    # sur différentes commandes - répondre
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("aide", help))
    dp.add_handler(CommandHandler("idees", idees))
    dp.add_handler(CommandHandler("noms", noms))
    dp.add_handler(CommandHandler("devs", devs))
    dp.add_handler(CommandHandler("exe", commande,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))

    # si le message ne contien pas commande - faire echo
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log toutes les erreurs
    dp.add_error_handler(error)

    # Démarrer le bot
    updater.start_polling()


def stop():
    """Arrêter le bot."""
    # Crée un EventHandler et transmet le Token de votre bot..
    updater = Updater(environ.get('TOKEN'))

    # Arrêter le bot
    updater.stop()


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
