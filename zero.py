from openai import OpenAI
client=OpenAI(
    api_key="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",
    base_url= "https://openrouter.ai/api/v1"
)
while True:
    user_input = input("You: ") 
    if user_input.lower() in ["exit", "quit", "bye","see you later"]:
        print("Chatbot: Goodbye!")
        break
    response=client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[
            {"role": "system", "content": "You are a helpful and friendly AI assistent."},
            {"role": "user","content": user_input}
        ]
    )
    reply = response.choices[0].message.content.strip()
    print(f"Chatbot: {reply}\n")
    

