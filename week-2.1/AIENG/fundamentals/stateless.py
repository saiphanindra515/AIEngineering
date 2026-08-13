from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

def stateless_chat(prompt: str) -> str:
    response = client.responses.create(
        model = "gpt-4o-mini",
        input = prompt
    )
    return response.output_text

print(stateless_chat("Who is prime minister of India before 2020?"))
