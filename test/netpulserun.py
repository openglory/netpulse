import requests

# 🔹 Replace with the RAW URL of your GitHub Python file
url = "https://raw.githubusercontent.com/openglory/netpulse/main/stablemain.py"

response = requests.get(url)

if response.status_code == 200:
    code = response.text
    exec(code)  # Run the downloaded Python code
else:
    print(f"Failed to fetch file. Status code: {response.status_code}")
