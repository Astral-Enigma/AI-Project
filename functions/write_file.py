import os

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
            
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'