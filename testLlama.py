from groq import Groq

customer = Groq()

response = customer.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "You are an intelligent assistant to rebuild a Linux setup from logs."},
        {"role": "user", "content": "Analyze my JSON history and generate a reinstall script."}
    ],
)

print(response.choices[0].message.content)
