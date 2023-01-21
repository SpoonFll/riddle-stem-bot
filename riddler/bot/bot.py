
import logging
import os
import traceback
from pathlib import Path

import hikari
import lightbulb
from aiohttp import ClientSession

log = logging.getLogger(__name__)

bot = hikari.GatewayBot(token="")


@bot.listen()
bot.run()


def run():
    print("hello")
