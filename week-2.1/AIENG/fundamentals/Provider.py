
from dotenv import load_dotenv
load_dotenv()
import os
from openai import OpenAI
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Provider:
    name: str
    env_var: str
    is_free: bool
    model: str
    base_url: Optional[str] = None

providers = [
    Provider("OpenAI","OPENAI_API_KEY",False,"gpt-4o-mini", None),
    Provider("Groq","GROQ_API_KEY",True,"gpt-oss-120b", "https://api.groq.com/openai/v1")
]

def select_provider() -> Provider:
    for provider in providers:
        if os.getenv(provider.env_var):
            return provider
    raise ValueError("No valid provider found. Please set the appropriate environment variable for a provider.")    

def build_client(provider: Provider) -> OpenAI:
    api_key = os.getenv(provider.env_var)
    if provider.base_url is None:
        return OpenAI(api_key=api_key)

    return OpenAI(api_key=api_key, base_url=provider.base_url)

def llm_reply(prompt: str) -> str:
    provider = select_provider()
    client = build_client(provider)
    result = client.chat.completions.create(
        model=provider.model,
        messages= [
            {"role": "user", "content": prompt}
        ]

    )
    return result.choices[0].message.content

if __name__ == "__main__":
    try:
        print(llm_reply("How to Write Research Paper?"))
    except ValueError as e:
        print(e)
        # No provider configured; instruct the user to set an env var.
        print("Set OPENAI_API_KEY or GROQ_API_KEY in your environment, then rerun.")