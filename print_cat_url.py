import os
import requests

def get_cat_picture_url():
    api_key = os.getenv("cats_api_key")
    if not api_key:
        print("Error: API key not found. Please set the 'cats_api_key' environmental variable.")
        return

    url = "https://api.thecatapi.com/v1/images/search"
    headers = {
        "x-api-key": api_key
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    if response.status_code == 200:
        # Extract the URL of the cat picture from the API response
        cat_picture_url = data[0]['url']
        return cat_picture_url
    else:
        print(f"Failed to fetch cat picture: {response.status_code} - {data.get('message')}")

# Example usage
cat_picture_url = get_cat_picture_url()
if cat_picture_url:
    print("Here's a cat picture:", cat_picture_url)
