import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = 'your-api-key'

def chat_with_bot(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003", # You can change the model if needed
            prompt=prompt,
            max_tokens=150,            # Adjust the response length as needed
            temperature=0.7,           # Controls the creativity of the response
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("Hello! I'm your chatbot. Type something to start a conversation, or type 'exit' to leave.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        bot_response = chat_with_bot(user_input)
        print(f"Bot: {bot_response}")
