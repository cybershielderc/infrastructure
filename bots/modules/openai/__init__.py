import json
from openai import OpenAI



if __name__ == '__main__':
    with open("../../../cfgs/bots.json", "r") as file:
        data = json.loads(file.read())
        file.close()
    client = OpenAI(
        organization='org-QWIagU8FVcSxIPVtBvFafVRo',
        project='proj_n0WFoS0XjtiR6nRGRayxe4QC',
        api_key=data['apis']['openai_api']
    )
    MODEL = "gpt-3.5-turbo"
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Knock knock."},
            {"role": "assistant", "content": "Who's there?"},
            {"role": "user", "content": "Orange."},
        ],
        temperature=0,
    )
    print(response)