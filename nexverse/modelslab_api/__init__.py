import requests
import json

with open("../cfgs/bot.json", "r") as file:
    data = json.loads(file.read())
    file.close()

api_data = data['apis']['modelslab']


class URIS:
    TTI = "https://modelslab.com/api/v6/images/text2img"
