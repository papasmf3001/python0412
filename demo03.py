import os
import openai
openai.api_key = "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" # 발급받은 API Key를 큰따옴표안에("") 입력하세요.

messages = []

user_contents = input("user : ") # 내가 ChatGPT에게 물어볼 내용을 적는곳입니다.
messages.append({"role": "user", "content": f"{user_contents}"})

# 모델을 변경해보세요. gpt-3.5-turbo 모델을 사용하겠습니다.
# 18달러까지 무료로 사용할 수 있습니다.
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages) 

assistant_contents = completion.choices[0].message["content"].strip()

messages.append({"role": "user", "content": f"{assistant_contents}"})

print(f"GPT : {assistant_contents}")