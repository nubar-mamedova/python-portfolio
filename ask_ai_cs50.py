import openai
from cs50 import get_string

# Your OpenAI API Key
client = openai.OpenAI(api_key="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")  # replace with your real key

# Ask loop
while True:
    prompt = get_string("\nAsk the AI (or type 'exit' to quit): ")
    if prompt.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    print("\nAI says:", response.choices[0].message.content)
