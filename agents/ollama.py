import ollama
from constants import MODEL_LLAMA

class OllamaTutor:

    def _call(self, messages):
        response = ollama.chat(
            model=MODEL_LLAMA,
            messages=messages
        )
        return response['message']['content']