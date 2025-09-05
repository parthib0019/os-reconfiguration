import json
from groq import Groq

client = Groq()

# Load your history JSON
with open("structured_history.json", "r") as f:
    history_data = f.read()

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "You are an assistant that analyzes Linux command history and generates reinstall scripts."},
        {"role": "user", "content": f"Here is my JSON history: {history_data}. Please generate a reinstall script for Ubuntu."}
    ],
)

print(response.choices[0].message.content)
