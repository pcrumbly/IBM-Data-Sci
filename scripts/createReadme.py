import os

def create_readme_in_folders(root_dir):
    for foldername in os.listdir(root_dir):
        if os.path.isdir(os.path.join(root_dir, foldername)):
            readme_content = f"This is the README for the folder '{foldername}'."
            readme_path = os.path.join(root_dir, foldername, "README.md")
            
            with open(readme_path, "w") as readme_file:
                readme_file.write(readme_content)
                
            print(f"Created README.md in '{foldername}' folder.")

if __name__ == "__main__":
    current_directory = os.getcwd()  # Get the current working directory
    parent_directory = os.path.dirname(current_directory)
    create_readme_in_folders(parent_directory)
