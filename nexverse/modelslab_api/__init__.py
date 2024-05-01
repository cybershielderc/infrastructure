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
    # NSFW
    DELIBERATE = "deliberateappfactory"
    PERFECT_DELI = "perfect-deli-appfact"
    MIX_APPFACTORY = "mix-appfactory"
    DARK_APPFACTORY = "dark-appfactory"
    # Realism
    MIDJOURNEY = "midjourney"
    REALISTIC_VISION = "realistic-vision-v40"
    JUGGERNAUT = "juggernaut-xl"
    # Anime
    ANYTHING = "anything-v4"
    DARK_SUSHI = "dark-sushi-25d"
    SAKURA = "sakurav3"


class TextToImage:
    MODELS: dict = {
        "nsfw": [
            MODEL.DELIBERATE,
            MODEL.PERFECT_DELI,
            MODEL.MIX_APPFACTORY,
            MODEL.DARK_APPFACTORY
        ],
        "realism": [
            MODEL.MIDJOURNEY,
            MODEL.REALISTIC_VISION,
            MODEL.JUGGERNAUT,
        ],
        "anime": [
            MODEL.ANYTHING,
            MODEL.DARK_SUSHI,
            MODEL.SAKURA,
        ]
    }

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
                      guidance_scale: float = 7.5
                      ) -> requests.api:
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
negative_prompt = "lowres, text, error, cropped, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, out of frame, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, username, watermark, signature"
nsfw_prompts = "hot lady in leggings, and see-through bra"
anime_prompts = "hot asian lady in a tight leather skirt and see-through buttoned white shirt"
realism_prompt = "hot brunette lady in lingerie, laying on a bed"

responses = []

for k, v in api.MODELS:
    for model in v:
        if k is "nsfw":
            responses.append(api.build_request(model, nsfw_prompts, negative_prompt))
        elif k is "anime":
            responses.append(api.build_request(model, anime_prompts, negative_prompt))
        elif k is "realism":
            responses.append(api.build_request(model, realism_prompt, negative_prompt))
