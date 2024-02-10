import openai

openai.api_key = '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'

class Chatbot:
    def __init__(self, model="gpt-3.5-turbo"):
        self.model = model
        self.conversation_history = []

    def ask_gpt_chat(self, question):
        try:
            self.conversation_history.append({"role": "user", "content": question})
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=self.conversation_history
            )
            model_response = response.choices[0].message['content'].strip()
            self.conversation_history.append({"role": "assistant", "content": model_response})
            return model_response
        except Exception as e:
            return f"An error occurred: {str(e)}"

# Example usage
chatbot = Chatbot() # Initialize the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    response = chatbot.ask_gpt_chat(user_input)
    print("GPT-3.5 says:", response)
