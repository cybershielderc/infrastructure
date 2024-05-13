from bot.main import run_app
import json
from auton_net.bot.database import (
    FirstRun,
    CheckDeveloperStatus
)

if __name__ == '__main__':
    with open("cfgs/bot.json", "r") as file:
        data = json.loads(file.read())
        file.close()
    f_run = FirstRun(data['database'], data['database']['credentials'])
    # Connect to First Run Model
    f_run.connect()
    # Execute Table Creation Scripts
    f_run.execute_scripts()
    # Run APP
    run_app(data["keys"]["tg"], data, {})
