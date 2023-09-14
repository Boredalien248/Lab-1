import requests

stuff = requests.get("https://raw.githubusercontent.com/Boredalien248/Lab-1/main/lab1/lab1.py?token=GHSAT0AAAAAACHR3TOIGDUINVZKTGQCVS64ZICMRCA")
print(stuff)

print(requests.__version__)
