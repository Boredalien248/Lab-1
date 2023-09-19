import requests

google = requests.get("https://www.google.com/")
print(google)

raw_file = requests.get("https://raw.githubusercontent.com/Boredalien248/Lab-1/main/lab1.py")
print(raw_file)

print(requests.__version__)
