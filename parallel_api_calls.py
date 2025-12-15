import asyncio
import aiohttp
import time

locations = [
    (13.0827, 80.2707),
    (12.9716, 77.5946),
    (17.3850, 78.4867)
]

async def fetch(session, lat, lon):
    url = "https://dummyjson.com/users/1"
    async with session.get(url) as response:
        data = await response.json()
        print(f"Latitude: {lat}, Longitude: {lon}, User: {data['firstName']}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, lat, lon) for lat, lon in locations]
        await asyncio.gather(*tasks)

start_time = time.time()
asyncio.run(main())
end_time = time.time()

print("Total Time Taken (Parallel):", end_time - start_time, "seconds")
