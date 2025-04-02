import openai
from cs50 import get_string

# Your OpenAI API Key
openai.api_key = "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"  # ← paste your API key here

def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

# Start conversation
while True:
    question = get_string("\nAsk the AI (or type 'exit' to quit): ")
    if question.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    response = ask_gpt(question)
    print("\nAI says:", response)
