from openai import OpenAI
client=OpenAI(
    api_key="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",
    base_url= "https://openrouter.ai/api/v1"
)

user_input = input("You: ")

reply=""

response=client.chat.completions.create(
    model="mistralai/mistral-7b-instruct",
    messages=[{"role": "system", "content": "You are a helpful assistant"}, {"role": "user", "content": f"{user_input}\nThink step by step."}, {"role": "assistant", "content": reply}]
)

reply = response.choices[0].message.content.strip()
print(f"Chatbot: {reply}\n")