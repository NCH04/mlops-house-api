import requests

maisons = [
    {"size": 100, "nb_rooms": 3, "garden": 1},
    {"size": 50,  "nb_rooms": 1, "garden": 0},
    {"size": 200, "nb_rooms": 5, "garden": 1},
]
for m in maisons:
    r = requests.post("http://127.0.0.1:8000/predict", json=m)
    print(m, "→", r.status_code, r.json())