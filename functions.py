# Definign the generator function.

import openai
import config
def generate_text(prompt):
    response = openai.Completion.create(engine = "davinci-002",
    prompt = prompt,
    max_tokens = 10,
    temperature = 0.7)

    return response.choices[0].text.strip()
