from bots.tele.main import run_app
from bots.modules.cryptocurrency import *
from nexverse.bot import run_app as nexverse_runbot
from nexverse.modelslab_api import MODEL, TextToImageAsynchronous
import json
import threading

if __name__ == '__main__':
    with open("cfgs/bots.json", "r") as f:
        data = json.loads(f.read())
        f.close()
    with open("cfgs/lang_en_US.json", "r") as f:
        lang = json.loads(f.read())
        f.close()
    token = data['tg']['token']
    # Initiate cryptocurrency module
    cryptocurrency = Cryptocurrency()
    if not cryptocurrency.check_connection():
        print("Could not connect to Web3!, Exiting!")
        exit(0xdead)
    # Initiate Eth Net Connection
    cryptocurrency.initiate_eth_net()
    # Run threads
    # tele_app = run_app(token, cryptocurrency)
    nexverse = nexverse_runbot(data['nexverse']['token'], TextToImageAsynchronous(data['apis']['modelslab_api']), la)
    print("Running")
