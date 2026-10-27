from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

def get_ai_response(message):
  response = client.chat.completions.create(
    model = "gpt-4o",
    temperature =0.9,
    message=[
      {"role": "system","content" : ""},
      {"role": "user", "content": "참새"},
      {"role": "assistant", "content": "짹짹"}
    ]
  )
  return response.choices[0].message.content

message = [{'role':"system","content":"너는 사용자를 도와주는 상담사야"},
           ]


while True:
  user_input = input("사용자: ")

  if user_input == 'exit':
    break


    messges.append({'role': "user",'content':user_input})
    ai_response = get_ai_response(messages)
    message.append({'role':'assistant','content':ai_response})
    
# print(response.choices[0].message.content) #response의 내용만 출력