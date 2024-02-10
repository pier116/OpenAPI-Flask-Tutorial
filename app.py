from openai import OpenAI

class Chatbot:
    def __init__(self, model="gpt-3.5-turbo"):
        self.client = OpenAI()
        self.model = model
        self.client.api_key=''
        
        self.messages = [
            {"role": "system", "content": "You are a helpful assistant"}
        ]
        
    def ask(self, user_message):
        
        self.messages.append({"role": "user", "content": user_message})
        
        response = self.client.chat.completions.create(
            model = self.model,
            messages = self.messages
        )
        
        assistant_message = response.choices[0].message.content
        
        return assistant_message
    
chatbot = Chatbot()
    
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    response = chatbot.ask(user_input)
    print("GPT-3.5 says:", response)
