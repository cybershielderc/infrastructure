from bots.tele.main import run_app
from bots.modules.cryptocurrency import *
from nexverse.bot import run_app as nexverse_runbot
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
    cserc_thread = threading.Thread(target=run_app, args=(token, cryptocurrency,))
    nexverse_thread = threading.Thread(target=nexverse_runbot, args=(data['nexverse']['token'],))

    cserc_thread.start()
    nexverse_thread.start()

    cserc_thread.join()
    nexverse_thread.join()
    # tele_app = run_app(token, cryptocurrency)
    # nexverse = nexverse_runbot(data['nexverse']['token'])
    print("Running")
