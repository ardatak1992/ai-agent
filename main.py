import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python import schema_run_python_file
from functions.call_function import call_function


def main():

	available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
				schema_get_file_content,
				schema_write_file,
				schema_run_python_file
    ]
	)


	system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""



	if len(sys.argv) < 2 :
		print("Please enter prompt")
		exit(1)
	
	prompt = sys.argv[1]
	verbose = False
	if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
		verbose = True

	messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
]

	load_dotenv()
	api_key = os.environ.get("GEMINI_API_KEY")
	client = genai.Client(api_key=api_key)
	res = client.models.generate_content(
		model="gemini-2.0-flash-001", 
		contents=messages,
		config=types.GenerateContentConfig(
			tools=[available_functions], 
			system_instruction=system_prompt
			))
	
	if verbose:
		print(f"User prompt: {prompt}")
		print(f"Response tokens: {res.usage_metadata.candidates_token_count}")
		print(f"Prompt tokens: {res.usage_metadata.prompt_token_count}")

	
	if len(res.function_calls) > 0:
		for function_call_part in res.function_calls:
			res = call_function(function_call_part, verbose=True)
			if (res.parts[0].function_response.response) and verbose:
				print(f"-> {res.parts[0].function_response.response}")
			else:
				raise ReferenceError("No function response found")
	

if __name__ == "__main__":
	main()
