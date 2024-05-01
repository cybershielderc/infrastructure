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

    def build_request(self, model: MODEL, prompt: str = None, negative_prompt: str = None,
                      size: [int, int] = [512, 512], samples: int = 1, num_inference_steps: int = 30, seed: int = None,
                      guidance_scale: float = 7.5) -> str:
        data = json.dumps({
            "key": self.api_key,
            "model_id": model.value,
            "prompt": prompt,
            "negative_prompt": negative_prompt
            "width":size[0],
            "height":size[1],
            "samples": samples,
            "num_inference_steps": num_inference_steps,
            "seed": seed,
            "guidance_scale": guidance_scale,
            "scheduler": "UniPCMultistepScheduler",
            "webhook": None,
            "track_id": None,
        })
        header = {
            'Content-Type': 'application/json'
        }
        request = requests.request("POST", URIS.TTI, headers=header, )
