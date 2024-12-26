# Definign the generator function.

import openai
import config

def generate_text(prompt):
    response = openai.Completion.create(engine = "davinci-002",
    prompt = prompt,
    max_tokens = 10,
    temperature = 0.7)

    return response.choices[0].text.strip()


def generate_text_1(prompt, max_tokens):
    response = openai.Completion.create(
        engine = "davinci-002",
        prompt = prompt,
        max_tokens = max_tokens,
        temperature = 0.7)
    return response.choices[0].text.strip()





def generate_text_2(prompt, max_tokens, randomness):
    response = openai.Completion.create(
        engine = "davinci-002",
        prompt = prompt,
        max_tokens = max_tokens,
        temperature = randomness)
    return response.choices[0].text.strip()# temperature controls the randomness.

def text_summarizer(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [

            {"role": "system", "content": "You are a helpful assistant that summarizes text."},

            {"role": "user", "content":  "A flying saucer seen by a guest house"},

            {
                "role": "assistant", "content":"A flying saucer was spotted by guests at a house, causing excitement and speculation about its origin and purpose."
            },

            {"role": "user", "content": "Each April, in village 10 miles from the city, the villagers celebrate the festival of the flying saucer. The festival is a celebration of the annual visit of a flying saucer to the village. The saucer is believed to be a symbol of good luck and prosperity, and the villagers welcome it with songs, dances, and feasts. The festival has been celebrated for generations, and it is a source of pride and joy for the villagers."

            },
            {
                "role": "assistant", "content": "A village 10 miles from a city hosts an annual festival celebrating the visit of a flying saucer, symbolizing good luck and prosperity. The event features songs, dances, and feasts, and has been a tradition for many generations."
            },
            {
                "role":"user",
                "content": prompt
            }
        ],
        temperature = 0.7,
        max_tokens = 64

    )
    return response.choices[0].message.content.strip()