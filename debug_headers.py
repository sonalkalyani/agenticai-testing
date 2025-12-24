import requests

def check_my_disguise():
    url = "https://httpbin.org/user-agent"
    
    # 1. Define the disguise
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # 2. Send the request WITH the headers
    response = requests.get(url, headers=headers)

    # 3. Print what the server saw
    print(f"Status Code: {response.status_code}")
    print(f"The server thinks I am: {response.json()}")

check_my_disguise()