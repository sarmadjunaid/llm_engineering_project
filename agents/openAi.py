from openai import OpenAI
from constants import MODEL_GPT


class OpenAITutor:
    def __init__(self):
        self.openai = OpenAI()

    def _call(self, messages):
        response = self.openai.chat.completions.create(
            model=MODEL_GPT,
            messages=messages
        )
        return response.choices[0].message.content