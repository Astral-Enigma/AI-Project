import os
from dotenv import load_dotenv
from google import genai
from call_func import available_functions
from call_func import call_function
import sys

def main():

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    script_name = sys.argv[0]
    arguments = sys.argv[1]

    verbose = "--verbose" in sys.argv
    system_prompt = system_prompt = """

                            You are a helpful AI coding agent.

                            When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

                                - List files and directories
                                - Read file contents
                                - Execute Python files with optional arguments
                                - Write or overwrite files

                            All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
                                
                                """

    response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=[sys.argv[1]],
    config=genai.types.GenerateContentConfig(tools = [available_functions], system_instruction=system_prompt)
    )

    if len(sys.argv) < 2:
        print("No prompt provided.")
        exit(1)

    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if response.function_calls:
        for part in response.function_calls:
            print(f"Calling function: {part.name}({part.args})")

    if not response.function_calls:
        print(f"User prompt: {sys.argv[1]}")
        print(f"Response: {response.text}")
            
    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting.")

if __name__ == "__main__":
    main()
