from google import genai
from environs import Env

env = Env()
env.read_env()
api_key = env.str("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

print("Gemini chatni boshlash uchun savolingizni kiriting (chiqish uchun 'exit' deb yozing):")

while True:
    user_prompt = input("Siz: ").strip()
    if not user_prompt:
        continue
    if user_prompt.lower() == "exit":
        print("Chat yakunlandi.")
        break
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_prompt
        )
        print("AI:", response.text)
    except Exception as e:
        print("Xatolik yuz berdi:", e)
