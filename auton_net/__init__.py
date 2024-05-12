from bot.main import run_app
import json
from database import FirstRun

if __name__ == '__main__':
    with open("cfgs/bot.json", "r") as file:
        data = json.loads(file.read())
        file.close()
    f_run = FirstRun(data['database'], data['database']['credentials'])
    f_run.connect()
    f_run.execute_scripts()
    # run_app(data["keys"]["tg"], {})
