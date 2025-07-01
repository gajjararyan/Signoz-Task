import requests
import random
import time

endpoints = ["/", "/slow", "/unstable", "/login", "/purchase", "/external"]

for _ in range(100):
    endpoint = random.choice(endpoints)
    try:
        r = requests.get(f"http://localhost:5000{endpoint}")
        print(f"{endpoint}: {r.status_code}")
    except Exception as e:
        print(f"{endpoint}: ERROR {e}")
    time.sleep(random.uniform(0.1, 0.5))
