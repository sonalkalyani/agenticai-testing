# 1. Import the library we need
import requests

def test_login_api():
    # 2. Setup our variables
    base_url = "https://httpbin.org"
    my_data = {"email": "eve.holt@reqres.in", "password": "cityslicka"}

    # 3. Send the POST request
 
    print(f"{base_url}/api/login")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.post(f"{base_url}/post", json = my_data, headers = headers)
    
    assert response.status_code == 200
    print(f"Status Code: {response.status_code}")
    print("Login Test Passed Successfully!")

def test_login_failure():
    url = "https://httpbin.org/status/401"
    response = requests.post(url)
    assert response.status_code == 401
    print("Negative Test Passed")

# 6. Call the function to actually run the test
test_login_api()
test_login_failure()