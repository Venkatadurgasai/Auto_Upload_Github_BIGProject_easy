from github import Github
import os

# GitHub credentials
github_username = '*****************'
github_token = '*****'

# Repository details
repository_name = '*****'
repository_owner = '*****'

# Folder to upload
folder_path = 'C:\Users\sample\path'

def upload_folder_to_github(folder_path, repository_name, repository_owner, github_username, github_token):
    try:
        # Authenticate with GitHub
        g = Github(github_username, github_token)
        
        # Get repository
        repo = g.get_user(repository_owner).get_repo(repository_name)

        # Create a new git repository in the specified folder
        os.chdir(folder_path)
        os.system('git init')

        # Add all files in the folder
        os.system('git add .')

        # Commit changes
        os.system('git commit -m "Initial commit"')

        # Add remote origin
        remote_url = f'https://github.com/{repository_owner}/{repository_name}.git'
        os.system(f'git remote add origin {remote_url}')

        # Push changes to GitHub
        os.system('git push -u origin master')

        print("Folder uploaded successfully to GitHub!")
    except Exception as e:
        print(f"Error: {str(e)}")

# Call the function to upload the folder
upload_folder_to_github(folder_path, repository_name, repository_owner, github_username, github_token)
