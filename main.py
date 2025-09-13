import os
from dotenv import load_dotenv
from constants import MODEL_GPT, MODEL_LLAMA
from agents.agentFactory import TutorFactory


load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

if api_key and api_key.startswith('sk-proj-') and len(api_key) > 10:
    print("API key looks good so far")
else:
    print("There might be a probolem with your API key")



if __name__ == "__main__":
    system_prompt = "You are an expert tutor of python. You will guide us through the questions and explain each logic."
    system_prompt += "\nThe response should be in MarkDown format." 

    input_model = input("Which model you want to ask question from ? gpt/ollama : ")
    user_prompt = input("Question: ")

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    model_mapping = {
        "gpt": MODEL_GPT,
        "ollama": MODEL_LLAMA
    }
    tutor = TutorFactory().get_model(model=model_mapping[input_model])
    answer = tutor._call(messages=messages)
    print(answer)