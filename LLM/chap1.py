from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
  model = "gpt-4o",
  temperature =0.9,
  message=[
    {"role": "system","content" : "너는 왕자야 그 역할에 맞게 답변해줘"},
    {"role": "user", "content": "너는 누구니?"},
  ]
)

print(response.choices[0].message.content) #response의 내용만 출력