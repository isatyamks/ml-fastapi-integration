import os

def myfunc(directory):
   
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir_name in dirs:
            
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):
                try:
                    os.rmdir(dir_path)  
                    print(f"Deleted empty folder: {dir_path}")
                except Exception as e:
                    print(f"Error deleting folder {dir_path}: {e}")

if __name__ == "__main__":

    path = "/path/to/your/folder"
    
    myfunc(path)
