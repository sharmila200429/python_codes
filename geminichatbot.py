import google.generativeai as genai
import os

genai.configure(api_key="key")
model=genai.GenerativeModel("gemini-3.1-flash-lite-preview")
chat=model.start_chat(history=[])

print("chargebee chatbot (Type 'exit' to quit)")
print("welcome,how can i help you?")

while True:
    user_input=input("you:")
    if user_input.lower() in ["exit","quit","bye"]:
        break
    response = chat.send_message(user_input)
    print(f"chargebee:{response.text}")
