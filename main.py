from bots.tele.main import run_app
from bots.modules.cryptocurrency import *
from nexverse.bot import run_app as nexverse_runbot
from nexverse.modelslab_api import MODEL, TextToImage
import json
import threading

if __name__ == '__main__':
    with open("cfgs/bots.json", "r") as f:
        data = json.loads(f.read())
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
    nexverse = nexverse_runbot(data['nexverse']['token'], Tex(data['apis']['modelslab_api']))
    print("Running")
