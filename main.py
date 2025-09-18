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


    verbose = "--verbose" in sys.argv
    system_prompt = '''

                            You are a helpful AI coding agent.

                            When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

                                - List files and directories
                                - Read file contents
                                - Execute Python files with optional arguments
                                - Write or overwrite files

                            All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
                                
                                '''
    
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)
    user_prompt = " ".join(args)

    messages = [
        genai.types.Content(role="user", parts=[genai.types.Part(text=user_prompt)]),
    ]
    
    for i in range(20):
        try:
            response = client.models.generate_content(
            model='gemini-2.0-flash-001',
            contents= messages,
            config=genai.types.GenerateContentConfig(tools = [available_functions], system_instruction=system_prompt)
            )

            if response.candidates:
                for candidate in response.candidates:
                    messages.append(candidate.content)

            if len(sys.argv) < 2:
                print("No prompt provided.")
                exit(1)

            if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

            if response.function_calls:
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
                messages.append(genai.types.Content(role="user", parts=function_responses))

            if not response.function_calls:
                print(f"User prompt: {sys.argv[1]}")
                print(f"Final response: {response.text}")
                return
                    
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
        except Exception as e:
            print(e)
            
if __name__ == "__main__":
    main()
