import os

def create_folders(base_directory, folder_names):

    if not os.path.exists(base_directory):
        os.makedirs(base_directory)


    for folder_name in folder_names:
        folder_path = os.path.join(base_directory, folder_name)
        

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Folder '{folder_name}' created at: {folder_path}")
        else:
            print(f"Folder '{python}' already exists at: {d:/python/python projects}")

          

        


base_directory = "C:/YourBaseDirectory"

folder_names = ["Folder1", "Folder2", "Folder3","Folder4","Folder5","Folder6","Folder7"]

create_folders(base_directory, folder_names)



