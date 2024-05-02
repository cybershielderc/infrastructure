import enum
import requests
import json


class URIS:
    TTI = "https://modelslab.com/api/v6/images/text2img"
    QUEUED_IMAGES = "https://modelslab.com/api/v6/images/fetch"


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
    DEFAULT_NEG_PROMPT: str = "lowres, text, error, cropped, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, out of frame, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, username, watermark, signature",

    def __init__(self, api: str = None) -> None:
        if not api: raise Exception("No api key provided")
        self.api_key = api

    def build_request(self,
                      model: MODEL,
                      prompt: str = None,
                      negative_prompt: str = DEFAULT_NEG_PROMPT[0],
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
            "negative_prompt": negative_prompt[0] if type(negative_prompt) == tuple else negative_prompt,
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
        try:
            req_response = 
        request_response = request.raise_for_status()
        while (request_response.json()['status'] != 'success'):
            request_response: requests.Response = request.raise_for_status()

    def get_model(self, model_id: str) -> MODEL:
        return {
            # NSFW
            "nsfw1": MODEL.DELIBERATE,
            "nsfw2": MODEL.PERFECT_DELI,
            "nsfw3": MODEL.MIX_APPFACTORY,
            "nsfw4": MODEL.DARK_APPFACTORY,
            # Anime
            "anime1": MODEL.ANYTHING,
            "anime2": MODEL.DARK_SUSHI,
            "anime3": MODEL.SAKURA,
            # Realism
            "realism1": MODEL.MIDJOURNEY,
            "realism2": MODEL.REALISTIC_VISION,
            "realism3": MODEL.JUGGERNAUT,
        }.get(model_id, None)

    def get_queued(self, id: int = None) -> requests.api:
        return requests.get(
            URIS.QUEUED_IMAGES,
            headers={
                'Content-Type': 'application/json'
            },
            data=json.dumps({
                "key": self.api_key,
                "request_id": id
            })
        )
