
import requests

def get_geolocation():
    """Returns the user's geolocation based on their IP address."""
    try:
        response = requests.get('http://ip-api.com/json')
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        return f"City: {data.get('city')}, Region: {data.get('regionName')}, Country: {data.get('country')}"
    except requests.exceptions.RequestException as e:
        return f"Error getting geolocation: {e}"

if __name__ == "__main__":
    print(get_geolocation())
