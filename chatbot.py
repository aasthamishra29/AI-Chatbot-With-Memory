import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Store conversation history
chat_history = []

print("=" * 45)
print("🤖 AI Chatbot with Memory")
print("Type 'exit' to end the chat.")
print("=" * 45)

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("👋 Goodbye!")
        break

    # Save user message
    chat_history.append(f"User: {user_input}")

    # Combine conversation history
    conversation = "\n".join(chat_history)

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=conversation
        )

        ai_reply = response.text

        print("\nAI:", ai_reply)

        # Save AI response
        chat_history.append(f"AI: {ai_reply}")

    except Exception as e:
        print("\nError:", e)
