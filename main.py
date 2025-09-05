import json
from groq import Groq

client = Groq()

# Load your history JSON
with open("structured_history.json", "r") as f:
    history_data = f.read()

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "See there is a problem with programmers, like if you are going to reinsall your os then after reinstallation of you os you have to configure by installing modules and softwares so i want You to assistant to analyzes Linux command history and find out what configuration i have in computer and in which porocess of input of the command to achive that configuration give me a bash script which will install all neccesary configurations in my new os.  You have to give me only bash script nothing else. ignore those command which clone or push or pull data with git"},
        {"role": "user", "content": f"Here is my JSON history: {history_data}. Please generate a reinstall script for Ubuntu."}
    ],
)

print(response.choices[0].message.content)
