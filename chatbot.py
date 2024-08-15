import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key =
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
