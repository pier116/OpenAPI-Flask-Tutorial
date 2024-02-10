from openai import OpenAI
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

class Chatbot:
    def __init__(self, model="gpt-3.5-turbo"):
        self.client = OpenAI()
        self.model = model
        self.client.api_key = os.getenv('OPENAI_API_KEY')
        # Initialize with a system message defining the assistant's role
        self.messages = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]

    def ask(self, user_message):
        # Add the user's message to the conversation history
        self.messages.append({"role": "user", "content": user_message})

        # Use the OpenAI client to create a chat completion
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages
        )

        # Extract the assistant's message from the response
        assistant_message = response.choices[0].message.content

        # Optionally, you can append the assistant's response to the messages list for full history
        # self.messages.append({"role": "assistant", "content": assistant_message})

        return assistant_message

# Example usage
chatbot = Chatbot()  # Initialize the chatbot

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    response = chatbot.ask(user_input)
    print("GPT-3.5 says:", response)
