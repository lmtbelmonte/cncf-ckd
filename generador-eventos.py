import time
import random
import logging
import os
from logging.config import dictConfig

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

users = ["USUARIO1", "USUARIO2", "USUARIO3", "USUARIO4"]

events = ["logged in", "logged out", "Visitando pagina 1", "Visitando pagina 2", "Visitandeo pagina 3"]

# Special message to print at regular interval
special_message = {
    5: "Al USUARIO5 le ha fallado el login, la cuenta esta bloqueada ya que ha superado el numero maximo de fallos.",
    8: "{0} La Orden ha fallado ya que el item esta fuera de stock."
}


PRINT_SPECIAL_MESSAGE = "PRINT_SPECIAL_MESSAGE" in os.environ and os.environ["PRINT_SPECIAL_MESSAGE"] or True
OVERRIDE_USER = "OVERRIDE_USER" in os.environ and os.environ["OVERRIDE_USER"] or "USER7"
LOG_HANDLERS = "LOG_HANDLERS" in os.environ and os.environ["LOG_HANDLERS"] or "file,console"

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/log/app.log',
            'maxBytes': 5242880,
            'backupCount': 3,
            'formatter': 'default'
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }},
    'root': {
        'level': 'INFO',
        'handlers': LOG_HANDLERS.split(",")
    }
})

i = 0

while True:
    r1 = random.randint(0, len(users)-1)
    r2 = random.randint(0, len(events)-1)
    message = "{0} {1}".format(users[r1], events[r2])
    logging.info(message)
    time.sleep(1)

    i = i + 1

    if PRINT_SPECIAL_MESSAGE != "FALSE":
        for key in special_message:
            mod_5 = i % key
            if mod_5 == 0:
                logging.warning(special_message[key].format(OVERRIDE_USER))