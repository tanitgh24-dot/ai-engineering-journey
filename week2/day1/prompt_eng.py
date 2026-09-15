# 6 parts to prompts -- 
# 1> role 
# 2> task 
# 3> constraints 
# 4> output format 
# 5> zero-shot/one-shot/few-shot 
# 6> fall back

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

def llm_an(prompt):
    message={
        "role": "user",
        "content": prompt
    }
    messages = [message]
    response = client.chat.completions.create(model = model, messages = messages)
    ans = response.choices[0].message.content
    return ans

bad_prompt = """
#ROLE: 
You are a customer support agent at a mobile /laptop company.
#TASK WITH CONSTRAINTS:
Classify the user complaint into one of the following categories: billing, technical, return
#OUTPUT FORMAT:
your answer should be a single word, either billing, technical, or return
#EXAMPLE:
for instance, if the user complaint is "I was charged twice for my order", your answer should be "billing"
#FALLBACK:
If the issue is unrealated to any of the above categories, respond with "other"
This is a user complaint:
my stomach hurts bro
"""

print(llm_an(bad_prompt))