import json
import os

import openai


def gpt_init():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise Exception("OPENAI_API_KEY is not set")
    openai.api_key = api_key


def gpt_generate_image(theme):
    try:
        response = openai.Image.create(
            prompt=f"Create the imgage about the theme: {theme}",
            n=1,
            size="256x256",
        )
        return response["data"][0]["url"]
    except Exception as e:
        raise Exception(f"Error while generating image: {e}")


def gpt_generate_words(theme):
    query = (
        "Create me a list of 10 random English words related to the "
        f"{theme} along with short descriptions for each."
        "Do not include any explanations, only provide a RFC8259 "
        "compliant JSON response following this format without deviation. "
        "[{word: 'word', description: 'description'}]"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {
                    "role": "system",
                    "content": "Act as a search engine with JSON responses",
                },
                {"role": "user", "content": query},
            ],
        )
        raw = response["choices"][0]["message"]["content"]
        data = json.loads(raw)
        return data
    except Exception as e:
        raise Exception(f"Error while generating words: {e}")
