import enum
import requests
import json

with open("../cfgs/bot.json", "r") as file:
    data = json.loads(file.read())
    file.close()

api_data = data['apis']['modelslab']


class URIS:
    TTI = "https://modelslab.com/api/v6/images/text2img"

class MODEL(enum.Enum):
    PINKDREAM = "pinkdream-appfactory"

class TextToImage:
    def __init__(self, api: str = None) -> None:
        if not api: raise Exception("No api key provided")
        self.api_key = api

    def build_request(self, model: MODEL, prompt: str = None, negative_prompt: str = None, size: tuple = ):
        return json.dumps({
            "key": self.api_key,
            "model_id":
        })
