import os
import sys
import shutil
import json

def file_create():
    
    file_name = input("Enter the file name: ")
    file_write = input("Enter content to write to the file: ")

    try:
        with open(file_name, 'w') as file:
            file.write(file_write)
        
        
        abs_path = os.path.abspath(file_name)  
        print(f"File '{file_name}' has been created at {abs_path}.")
        
        return abs_path  
    
    except Exception as e:
        print(f"Error: {e}")
        sys.exit()

def back_up():
    try:
        
        with open("config.json", 'r') as file:
            config = json.load(file)

            backup_path = config.get("backup_path", "")
            
            if not backup_path:
                print(f"Please check the config.json file. No 'backup_path' found.")
                sys.exit()

            
            if not os.path.exists(backup_path):
                print(f"{backup_path} does not exist. Creating it now.")
                os.mkdir(backup_path)

            return backup_path  

    except Exception as e:
        print(f"Error: {e}")
        sys.exit()

if __name__ == "__main__":
   
    file_path = file_create() 

    
    if not file_path:
        print("Error: File creation failed. Exiting.")
        sys.exit()

  
    copy_path = back_up()

    try:
        destination = os.path.join(copy_path, os.path.basename(file_path))  
        print(f"Destination path for backup: {destination}")  

        shutil.copy2(file_path, destination)
        print(f"File '{file_path}' successfully backed up to '{destination}'.")

    except Exception as e:
        print(f"Error during file backup: {e}")
        sys.exit()
