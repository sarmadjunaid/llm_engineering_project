from constants import MODEL_LLAMA, MODEL_GPT
from .ollama import OllamaTutor
from .openAi import OpenAITutor


class TutorFactory:

    def get_model(self, model):
        if model == MODEL_LLAMA:
            return OllamaTutor()
        elif model == MODEL_GPT:
            return OpenAITutor()
        else:
            print("No model provided!")