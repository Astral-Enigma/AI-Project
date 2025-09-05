import os
from dotenv import load_dotenv
from google import genai
import sys

def main():

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    script_name = sys.argv[0]
    arguments = sys.argv[1]

    response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=[sys.argv[1]]
    )

    if len(sys.argv) < 2:
        print("No prompt provided.")
        exit(1)

    if len(sys.argv) == 2:
        print(response.text)

    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        print(f"User prompt: {sys.argv[1]}")
        print(response.text)
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
