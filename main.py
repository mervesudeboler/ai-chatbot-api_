import os
import google.generativeai as genai

def main():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("HATA: GEMINI_API_KEY bulunamadı. Terminalde export ettin mi?")
        return

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")

    print("AI Chatbot (Gemini) - çıkmak için Ctrl+C\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue

        resp = model.generate_content(user_input)
        print("\nBot:", resp.text, "\n")

if __name__ == "__main__":
    main()
