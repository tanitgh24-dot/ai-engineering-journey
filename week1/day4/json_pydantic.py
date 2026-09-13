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

#structure the prompt to extract personal information from the given text
from pydantic import BaseModel
class Ticket(BaseModel):
    name:str
    email:str
    issue : str

schema=Ticket.model_json_schema()

response_format={
    "type": "json_object",
}

system_prompt = f"""
Extract the personal information from the given text and return it in the following JSON format
{schema}
"""

message_system = {"role": "system", "content": system_prompt}


text = "hello my name is tanit ghosh and my iphone has genuinely stopped working bro, i live in kolkata. my email is tan@gmail.com. my phone number is 12345"

prompt = f"""
This is a customer ticket please extract the personal information from this.
{text}
"""
message = {"role": role, "content": prompt}

messages = [message_system, message]

response = client.chat.completions.create(model=model, messages=messages, response_format=response_format)

answer = response.choices[0].message.content
print(answer)

# to read the data and convert it into a pydantic model
import json
raw_json = answer
data_file=json.loads(raw_json)
tickets=Ticket(**data_file)

print(tickets.name)
print(tickets.email)
print(tickets.issue)