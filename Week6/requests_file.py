import requests

response = requests.get("https://api.github.com/events")
# print("Status Code:",response.status_code)

if response.status_code == 200:
    events = response.json()
    if events:
        print(events[0])
    else:
        print("No events found")
else:
    print(f"Failed to fetch events. Status code: {response.status_code}")
