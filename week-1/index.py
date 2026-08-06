from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

openaiClient = OpenAI()



response = openaiClient.chat.completions.create(
    model="gpt-4o-mini",
    messages= [
        {
            "role": "user",
            "content": "Roadmap in 100 words for AI Engineering 2026"
        }
    ]
)

print(response.choices[0].message.content)