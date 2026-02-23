import os
from google import genai

def main():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY is not found. Did you export in your Terminal?")
        return

    client = genai.Client(api_key=api_key)

    print("AI Chatbot (Gemini) - for exit Ctrl+C\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input
        )
        print("\nBot:", response.text, "\n")

if __name__ == "__main__":
    main()
