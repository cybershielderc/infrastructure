from auton_net.bot.main import run_app
import json
from auton_net.bot.database import (
    FirstRun,
    CheckDeveloperStatus,
    RetrieveAllConversations
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
    # Test retrieval scripts
    print("Attempting to retrieve all MFPC conversations...")
    print(RetrieveAllConversations.get_all_conversations({
        'host': data['database']['host'],
        
    }))
    # Run APP
    try:
        run_app(data["keys"]["tg"], data, {})
    except KeyboardInterrupt as e:
        exit(-1)
