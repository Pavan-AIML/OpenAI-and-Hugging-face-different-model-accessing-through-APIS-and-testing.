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