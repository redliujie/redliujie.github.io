import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = "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"

def ask_openai(question):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    return response['choices'][0]['message']['content']

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit"]:
        break
    answer = ask_openai(user_input)
    print(f"Bot: {answer}")
