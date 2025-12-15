# Google Places API – Serial and Parallel API Calls using Latitude & Longitude

## Objective
To understand how API calls work using latitude and longitude and to compare serial and parallel execution.

## Description
Multiple API calls are made using different latitude and longitude values.
The calls are executed:
1. Serially (one by one)
2. In Parallel (at the same time)

## Example Coordinates Used
- Chennai: 13.0827, 80.2707
- Bangalore: 12.9716, 77.5946
- Hyderabad: 17.3850, 78.4867

## Technologies
- Python
- REST API
- requests
- asyncio
- aiohttp

## Conclusion
Parallel API calls are faster than serial API calls when working with multiple latitude and longitude requests.
