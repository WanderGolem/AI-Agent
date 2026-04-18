import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types, errors
from prompts import system_prompt
from call_function import available_functions, call_function

def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        raise RuntimeError("no API-Key is set")

    client = genai.Client(api_key=api_key)
    
    generate_content(client, messages, args.verbose, args.user_prompt)    


def generate_content(client, messages, verbose, user_prompt): 
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=messages,
            config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt, temperature=0)
        )

        if not response.usage_metadata:
            raise RuntimeError("API request failed")

        if verbose:
            print(f"User prompt: {user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

        if response.function_calls:
            function_results = []
            for function_call in response.function_calls:
                function_call_result = call_function(function_call, verbose)

                if not function_call_result.parts:
                    raise Exception("empty parts in function call result")
                if not function_call_result.parts[0].function_response:
                    raise Exception("first item is not a object in function call result")
                if not function_call_result.parts[0].function_response.response:
                    raise Exception("empty function call result")
                
                function_results.append(function_call_result.parts[0])

                if verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
        else:
            print("Response:")
            print(response.text)
            
    except errors.APIError as e:
        print(f"API error: {e}")
if __name__ == "__main__":
    main()
