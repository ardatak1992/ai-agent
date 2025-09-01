import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
	
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
	res = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
	if verbose:
		print(f"User prompt: {prompt}")
		print(f"Response tokens: {res.usage_metadata.candidates_token_count}")
		print(f"Prompt tokens: {res.usage_metadata.prompt_token_count}")
	print(res.text)

if __name__ == "__main__":
	main()
