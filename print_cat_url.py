import os
import requests
from PIL import Image
import io

def get_cat_picture_url():
    api_key = os.getenv("CATS_API_KEY")
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

def print_cat_picture_in_terminal(cat_picture_url):
    response = requests.get(cat_picture_url)
    image_bytes = io.BytesIO(response.content)
    image = Image.open(image_bytes)
    image = image.resize((80, 40))  # Adjust the size as needed
    ascii_chars = '@%#*+=-:. '  # ASCII characters used to represent pixel intensity
    for y in range(image.height):
        line = ''
        for x in range(image.width):
            pixel = image.getpixel((x, y))
            grayscale_value = sum(pixel) / 3
            char_index = int(grayscale_value / 255 * (len(ascii_chars) - 1))
            line += ascii_chars[char_index]
        print(line)

# Example usage
cat_picture_url = get_cat_picture_url()
if cat_picture_url:
    print("Here's a cat picture:")
    print_cat_picture_in_terminal(cat_picture_url)
