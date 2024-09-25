import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class Chatbot:
    def __init__(self):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    def get_response(self, user_input):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant.",
                },
                {
                    "role": "user",
                    "content": user_input,
                },
            ],
            model="gpt-3.5-turbo",
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )

        message = chat_completion.choices[0].message["content"].strip()
        return message