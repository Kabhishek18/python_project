import requests

def shorten_url(url, token):
    """Shorten a long URL using the Bitly API."""
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    payload = {
        "long_url": url,
    }
    response = requests.post("https://api-ssl.bitly.com/v4/shorten", headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        short_url = data["link"]
        return short_url
    else:
        return None

# Get the long URL from the user
url = input("Enter long URL: ")

# Get the Bitly access token from the user
token = input("Enter Bitly access token: ")

# Shorten the URL using the Bitly API
short_url = shorten_url(url, token)

# Print the short URL
if short_url:
    print("Short URL:", short_url)
else:
    print("Error shortening URL.")
