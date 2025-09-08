import os
<<<<<<< HEAD
from google import genai

=======
>>>>>>> b9338f1 (1st commit)

def get_file_content(working_directory, file_path):
    working_directory = os.path.abspath(working_directory)
    full_path = os.path.join(working_directory, file_path)
    abs_path = os.path.abspath(full_path)

    if not abs_path.startswith(working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory' 
    
    if not os.path.isfile(abs_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(abs_path,"r") as file:
            data = file.read(10000)

            if os.path.getsize(abs_path) > 10000:
                data += f'[...File "{file_path}" truncated at 10000 characters]'
            
            return data
        
    except Exception as e:
<<<<<<< HEAD
        return f"Error: {e}"         
    

schema_get_file_content = genai.types.FunctionDeclaration(
    name="get_file_content",
    description= "Reads and returns the first 10000 characters of the content from a specified file within the working directory.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "file_path": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)
=======
        return f"Error: {e}"         
>>>>>>> b9338f1 (1st commit)
