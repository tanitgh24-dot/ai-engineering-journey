import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"
role = "user"

content = "so i am starting this new food delivery app what should i name it? Give only one name and do not explain it"

message_system = {"role": "system", "content": "You are a brand manager and your job is to sugest names for my new food delivery app"}
message = {"role": role, "content": content}

messages = [message_system, message]

response1 = client.chat.completions.create(model=model, messages=messages, temperature=2)
response2 = client.chat.completions.create(model=model, messages=messages, temperature=0.7)
# print(response)
print ("***************************************************************")

answer1 = response1.choices[0].message.content
answer2 = response2.choices[0].message.content
print(answer1)
print(answer2)