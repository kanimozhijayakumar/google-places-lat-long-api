import requests
import time

locations = [
    (13.0827, 80.2707),   # Chennai
    (12.9716, 77.5946),   # Bangalore
    (17.3850, 78.4867)    # Hyderabad
]

start_time = time.time()

for lat, lon in locations:
    url = f"https://dummyjson.com/users/1"
    response = requests.get(url)
    data = response.json()
    print(f"Latitude: {lat}, Longitude: {lon}, User: {data['firstName']}")

end_time = time.time()

print("Total Time Taken (Serial):", end_time - start_time, "seconds")
