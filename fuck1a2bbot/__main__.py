import logging
from argparse import ArgumentParser, Namespace
from pathlib import Path

from telegram import Update
from telegram.ext import Application, ApplicationBuilder, CommandHandler
from telegram.ext.filters import TEXT

from . import callback

parser: ArgumentParser = ArgumentParser("python -m fuck1a2bbot")
parser.add_argument("-d", "--debug", action="store_true")
parser.add_argument("-k", "--token")
parser.add_argument("-p", "--proxy")
args: Namespace = parser.parse_args()

logging.basicConfig(
    level=logging.CRITICAL,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

if args.debug:
    logging.getLogger("telegram.ext.Application").setLevel(logging.DEBUG)

application: Application = (
    ApplicationBuilder()
    .token(args.token)
    .http_version("2")
    .proxy(args.proxy)
    .get_updates_proxy(args.proxy)
    .build()
)

application.add_handler(CommandHandler("/fuck1a2b", callback))
application.run_polling(allowed_updates=Update.ALL_TYPES)
