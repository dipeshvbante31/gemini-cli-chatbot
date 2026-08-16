import os

from dotenv import load_dotenv
from google import genai


# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Please add it to your .env file."
    )


# Create Gemini client
client = genai.Client(api_key=API_KEY)


def chat():
    print("=" * 50)
    print("        Gemini AI Chatbot")
    print("=" * 50)
    print("Type 'exit' to quit.\n")

    while True:
        question = input("You: ")

        if question.lower().strip() == "exit":
            print("Goodbye!")
            break

        if not question.strip():
            print("Please enter a question.")
            continue

        try:
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=question
            )

            print("Gemini:", response.text)
            print()

        except Exception as e:
            print(f"Error: {e}")
            print()


if __name__ == "__main__":
    chat()
