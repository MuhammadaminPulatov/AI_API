from openai import OpenAI
from environs import Env

env = Env()
env.read_env()

client = OpenAI(api_key=env.str("OPENAI_API_KEY"))

print("Chatni boshlash uchun savolingizni kiriting (chiqish uchun 'exit' deb yozing):")

while True:
    user_prompt = input("Siz: ")

    if user_prompt.lower() == "exit":
        print("Chat yakunlandi.")
        break

    response = client.responses.create(
        model="gpt-5-nano",
        input=user_prompt
    )

    print("AI:", response.output_text)
