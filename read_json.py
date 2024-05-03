import requests
import json

def read_json_file_from_github(owner, repo, path, token):
    # Construct the URL to the raw JSON file in the private repository
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{path}"
    
    # Set the Authorization header with the token for authentication
    headers = {
        "Authorization": f"token {token}"
    }
    
    try:
        # Make a GET request to fetch the file content
        response = requests.get(url, headers=headers)
        
        # Check if request was successful (status code 200)
        if response.status_code == 200:
            # Load the JSON data from the response content
            json_data = json.loads(response.text)
            return json_data
        else:
            print(f"Failed to fetch JSON file. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error occurred while fetching JSON file: {e}")
        return None

# Example usage:
owner = "username"  # Replace 'username' with the GitHub username of the repository owner
repo = "repository-name"  # Replace 'repository-name' with the name of the private repository
path = "path/to/file.json"  # Replace 'path/to/file.json' with the path to the JSON file within the repository
token = "your-personal-access-token"  # Replace 'your-personal-access-token' with your GitHub personal access token

json_data = read_json_file_from_github(owner, repo, path, token)
if json_data:
    print("JSON file content:")
    print(json_data)
