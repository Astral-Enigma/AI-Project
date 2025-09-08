import os
<<<<<<< HEAD
from google import genai
=======
>>>>>>> b9338f1 (1st commit)

def write_file(working_directory, file_path, content):


    working_directory = os.path.abspath(working_directory)
    full_path = os.path.join(working_directory, file_path)
    abs_path = os.path.abspath(full_path)

    if not abs_path.startswith(working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory' 
    
    try:
        if not os.path.exists(abs_path):
            os.makedirs(os.path.dirname(abs_path), exist_ok=True)
    except Exception as e:
       return f"Error:{e}"
    
    try:
        with open(abs_path, "w") as f:
            f.write(content)        
    except Exception as e:
            f"Error: {e}"
            
<<<<<<< HEAD
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

schema_write_file = genai.types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the working directory. Creates the file if it doesn't exist.",
    parameters= genai.types.Schema(
        type= genai.types.Type.OBJECT,
        properties={
            "file_path": genai.types.Schema(
                type= genai.types.Type.STRING,
                description= "Path to the file to write, relative to the working directory.",
            ),
            "content": genai.types.Schema(
                type= genai.types.Type.STRING,
                description="Content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)
=======
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
>>>>>>> b9338f1 (1st commit)
