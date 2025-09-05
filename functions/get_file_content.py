import os
from google.genai import types

MAX_CHARS = 10000


def get_file_content(working_directory, file_path):
	absWorkingDirectory = os.path.abspath(working_directory)
	fullpath = os.path.abspath(os.path.join(absWorkingDirectory, file_path))
	print(fullpath)

	if not fullpath.startswith(absWorkingDirectory):
		return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

	if not os.path.isfile(fullpath):
		return f'Error: "{file_path}" is not a file'

	try:
		with open(fullpath, 'r') as f:
			file_content_string = f.read(MAX_CHARS)
			if len(file_content_string) == MAX_CHARS:
				file_content_string += '...File "{file_path}" truncated at 10000 characters'
			return file_content_string
	except Exception as e:
		return f'Error: Cannot read {file_path} content {e}'


schema_get_file_content = types.FunctionDeclaration(
	name='get_file_content',
	description='Reads content of the files, constrained to the working directory.',
	parameters=types.Schema(
		type=types.Type.OBJECT,
		properties={
			'file_path': types.Schema(
				type=types.Type.STRING,
				description='Path of the file relative to working directory',
			),
		},
	),
)
