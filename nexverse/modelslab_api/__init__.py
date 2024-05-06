import enum
import time

import requests
import json
import asyncio
import datetime


def ftime() -> str:
    return datetime.datetime.now().strftime("%d-%m-%Y//%H:%M:%S.%f")


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
            "safety_checker": False,
        })
        header = {
            'Content-Type': 'application/json'
        }
        request = requests.request("POST", URIS.TTI, headers=header, data=payload)

        try:
            response: requests.Response = request.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
        return request

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

    def __default_prompt__(self) -> str:
        return self.DEFAULT_NEG_PROMPT


class TextToImageAsynchronous(TextToImage):
    def __init__(self, api: str = None) -> None:
        if not api: raise Exception("No api key provided")
        self.api_key = api

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

    async def get_image(self,
                        model: MODEL = None,
                        requesting_uid: int = None,
                        prompt: str = None,
                        neg_prompt: str = TextToImage.DEFAULT_NEG_PROMPT,
                        size: [int, int] = [512, 512],
                        samples: int = 1,
                        num_inference_steps: int = 30,
                        seed: int = None,
                        guidance_scale: float = 7.5,
                        safety_checker: bool = False
                        ) -> list:
        if not prompt or not neg_prompt: raise Exception("No prompt/negative prompt provided")
        if not requesting_uid: raise Exception("No requesting uid provided")
        print(f"[{ftime()}]-(TTI): Creating payload and header for user request URQ-{requesting_uid}")
        payload = json.dumps({
            "key": self.api_key,
            "model_id": model.value,
            "prompt": prompt,
            "negative_prompt": neg_prompt if not type(neg_prompt) is tuple else neg_prompt[0],
            "width": size[0],
            "height": size[1],
            "samples": samples,
            "num_inference_steps": num_inference_steps,
            "seed": seed,
            "guidance_scale": guidance_scale,
            "scheduler": "UniPCMultistepScheduler",
            "webhook": None,
            "track_id": None,
            "safety_checker": False,
        })
        header = {
            'Content-Type': 'application/json'
        }
        print(f"[{ftime()}]-(TTI): payload and header created for user request URQ-{requesting_uid}")
        print(f"[{ftime()}]-(TTI): payload for user request URQ-{requesting_uid}:\n{payload}")
        print(f"[{ftime()}]-(TTI): Sending request to API for user request URQ-{requesting_uid}")
        try:
            request = requests.request("POST", URIS.TTI, headers=header, data=payload)
            print(f"[{ftime()}]-(TTI): Request sent to API for user request URQ-{requesting_uid}")
            print(f"[{ftime()}]-(TTI): Returning request response for user request URQ-{requesting_uid}")
            print(f"[{ftime()}]-(TTI): Showing raw data for request URQ-{requesting_uid}")
            print(f"[{ftime()}]-(TTI): URQ-{requesting_uid}:<{request.status_code}>\n{request.json()}")
            return [
                request.status_code,
                request.json(),
                {"data": {
                    "ruid": requesting_uid,
                    "safety_checker": safety_checker,
                }}
            ]
        except requests.RequestException as e:
            print(f"[{ftime()}]-(TTI): An error occurred for request URQ-{requesting_uid}")
            print(f"[{ftime()}]-(TTI): Error response for request URQ-{requesting_uid}")
            print(f"[{ftime()}]-(TTI): {str(e)}")
            return [None, str(e)]

    async def handle_response(self,
                              model: MODEL = None,
                              requesting_uid: int = None,
                              prompt: str = None,
                              neg_prompt: str = TextToImage.DEFAULT_NEG_PROMPT,
                              size: [int, int] = [1024, 1024],
                              samples: int = 1,
                              num_inference_steps: int = 100,
                              seed: int = None,
                              guidance_scale: float = 9.5,
                              safety_checker: bool = False
                              ):
        print(f"[{ftime()}]-(TTI): request URQ-{requesting_uid} parameters:" + \
              f"\n[{ftime()}]-(TTI): URQ-{requesting_uid} // MODEL: {model.value}" + \
              f"\n[{ftime()}]-(TTI): URQ-{requesting_uid} // PROMPT: \n{prompt}" + \
              f"\n[{ftime()}]-(TTI): URQ-{requesting_uid} // NEG_PROMPT: \n{neg_prompt}" + \
              f"\n[{ftime()}]-(TTI): URQ-{requesting_uid} // SIZE: {size}" + \
              f"\n[{ftime()}]-(TTI): URQ-{requesting_uid} // TECHNICAL // SAMPLES: {samples}" + \
              f"\n[{ftime()}]-(TTI): URQ-{requesting_uid} // TECHNICAL // N. INFER STEPS: {num_inference_steps}" + \
              f"\n[{ftime()}]-(TTI): URQ-{requesting_uid} // TECHNICAL // GUIDANCE: {guidance_scale}" + \
              f"\n[{ftime()}]-(TTI): URQ-{requesting_uid} // TECHNICAL // SAFETY CHECKER?: {safety_checker}"
              )
        start_time = time.time()
        response = await self.get_image(
            model, requesting_uid, prompt, neg_prompt,
            size, samples, num_inference_steps, seed,
            guidance_scale, safety_checker
        )
        if response[0] is not None:
            print(f"[{ftime()}]-(TTI): request URQ-{requesting_uid} is valid")
            if response[0] is 200:
                print(f"[{ftime()}]-(TTI): HTTP<200> code received for request URQ-{requesting_uid}")
                # Handle 200 OK HTTP CODE
                if response[1]['status'] == 'success':
                    print(f"[{ftime()}]-(TTI): HTTP<200><success> received for request URQ-{requesting_uid}")
                    # Handle SUCCESS status response
                    print(f"[{ftime()}]-(TTI): Returning request URQ-{requesting_uid}\n" + \
                          f"[{ftime()}]-(TTI): URQ-{requesting_uid} Data: \n{response[1]}")
                    return [
                        response[1]['id'],  # Image ID
                        response[1]['output'][0],  # Image URI,
                        "N/A",  # Prompt
                        f"{response[1]['generationTime']:.2f}",  # Image Generation Time
                    ]
                elif response[1]['status'] == 'processing':
                    print(f"[{ftime()}]-(TTI): HTTP<200><processing> received for request URQ-{requesting_uid}")
                    print(
                        f"[{ftime()}]-(TTI): Awaiting {response[1]['eta']:.2f}s before returning request URQ-{requesting_uid}")
                    eta: int = response[1]['eta']
                    await asyncio.sleep(eta + 0.95)
                    
                    if requests.post(
                            url=response[1]['future_links'][0]
                    ).status_code == 404:
                    print(f"[{ftime()}]-(TTI): Returning request URQ-{requesting_uid}\n" + \
                          f"[{ftime()}]-(TTI): URQ-{requesting_uid} Data: \n{response[1]}")
                    return [
                        response[1]['id'],  # Image ID
                        response[1]['future_links'][0],
                        # Image URI ignore the fetch endpoint as it is returning the same URI in both the future_links and api fetch endpoint
                        "N/A",  # Prompt
                        f"{start_time - time.time():.2f}",  # Image Generation Time
                    ]
