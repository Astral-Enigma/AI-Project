import os

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
        return f"Error: {e}"         