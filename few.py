from openai import OpenAI
client=OpenAI(
    api_key="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",
    base_url= "https://openrouter.ai/api/v1"
)
user_input= input("You: ")
reply= ""
response= client.chat.completions.create(
    model= "gpt-4o-mini", 
    messages= [{"role": "system","content": "You are expert translator."},
               {"role":"user","content":"English: Good Moring\n French: Bonjour"}, 
               {"role": "user", "content": f"English: {user_input}\nFrench: "}]
    )
reply = response.choices[0].message.content.strip()
print(f"Chatbot: {reply}\n")