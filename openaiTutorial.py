import openai

# Replace YOUR_API_KEY with your actual OpenAI API key
openai.api_key = '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'

def ask_gpt_chat(question, model="gpt-3.5-turbo"):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage
user_input = input("Ask GPT-3.5: ")
response = ask_gpt_chat(user_input) # Using a GPT-3.5 chat model
print("GPT-3.5 says:", response)
