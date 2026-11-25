import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found in .env file")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Send a question to Gemini
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="What is Artificial Intelligence? Explain in simple words."
)

# Display the response
print("\nGemini Response:")
print(response.text)