import os

def write_file(working_directory, file_path, content):
  absWorkingDirectory = os.path.abspath(working_directory)
  fullpath = os.path.abspath(os.path.join(absWorkingDirectory, file_path))
  head, _ = os.path.split(fullpath)

  if not fullpath.startswith(absWorkingDirectory):
    return f'Error: Cannot write to "{fullpath}" as it is outside the permitted working directory'

  if not os.path.exists(head):
    os.makedirs(head)

  try:
    with open(fullpath, "w") as f:
      f.write(content)
      return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
  except Exception as e:
    return "Error: cannot write to file {e}"

print(write_file(".", "/hello/h.txt", "Hello from hello.txt"))
