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

    def build_request(self,
                      model: MODEL,
                      prompt: str = None,
                      negative_prompt: str = None,
                      size: [int, int] = [512, 512],
                      samples: int = 1,
                      num_inference_steps: int = 30,
                      seed: int = None,
                      guidance_scale: float = 7.5) -> str:
        if not prompt or not negative_prompt: raise Exception("No prompt/negative prompt provided")
        payload = json.dumps({
            "key": self.api_key,
            "model_id": model.value,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "width": size[0],
            "height": size[1],
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
        request = requests.request("POST", URIS.TTI, headers=header, data=payload)

        return request


api = TextToImage(data['apis']['modelslab'])
response = api.build_request(MODEL.PINKDREAM, "hot lady in leggings, and see-through bra",
                             "painting, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, ugly, blurry, bad anatomy, bad proportions, extra limbs, cloned face, skinny, glitchy, double torso, extra arms, extra hands, mangled fingers, missing lips, ugly face, distorted face, extra legs, anime")

print(response)
