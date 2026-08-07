from dotenv import load_dotenv
from openai import OpenAI
from prompt import SYSTEM_PROMPT
load_dotenv()

try:
    client = OpenAI()
except KeyboardInterrupt:
    print('Some Error Occured, Task Buddy Good Bye!')
except Exception as e:
    print(f'Some Error Occured, Task Buddy Good Bye! {e}')
     

def main():

    messages_example = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    while True:
        input_text = input("You: ").strip()
        if input_text.lower() in ["exit", "quit"]:
            print("Task Buddy: Goodbye!")
            break
        if not input_text.strip():
            continue
        messages_example.append({"role": "user", "content": input_text})
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages = messages_example
            )
            print("Task Buddy:", response.choices[0].message.content)
            messages_example.append({"role": "assistant", "content": response.choices[0].message.content})
        except Exception as e:
            print(f"Task Buddy: An error occurred: {e}")
            continue    




if __name__ == "__main__":
    main()