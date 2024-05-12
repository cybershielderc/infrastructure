from bot.main import run_app
import json

if __name__ == '__main__':
    with open("cfgs/bot.json", "r") as file:
        data = json.loads(file.read())
        file.close()
    run_app(data[""])
