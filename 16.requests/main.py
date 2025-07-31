import httpx

# 1. Simple GET request
print("1. GET Request:")
response = httpx.get("https://jsonplaceholder.typicode.com/posts/1")
print("Status Code:", response.status_code)
print("JSON Response:", response.json())  # Parsed JSON data
print()

# 2. GET with query parameters
print("2. GET with Params:")
params = {'userId': 1}
response = httpx.get("https://jsonplaceholder.typicode.com/posts", params=params)
print("Requested URL:", response.url)
print("First Post Title:", response.json()[0]['title'])
print()

# 3. Custom headers
print("3. GET with Headers:")
headers = {'User-Agent': 'MyApp/1.0'}
response = httpx.get("https://postman-echo.com/headers", headers=headers)
print("Status Code:", response.status_code)
if response.headers.get('Content-Type') == 'application/json':
    print("Returned Headers:", response.json().get('headers'))
else:
    print("Unexpected response type.")
    print("Raw content:\n", response.text)
print()

# 4. POST request with data
print("4. POST Request:")
data = {'title': 'foo', 'body': 'bar', 'userId': 1}
response = httpx.post("https://jsonplaceholder.typicode.com/posts", json=data)
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
print()

# 5. Handling timeouts
print("5. Timeout Example:")
try:
    httpx.get("https://httpbin.org/delay/3", timeout=1)
except httpx.exceptions.Timeout:
    print("Request timed out!")
print()

# 6. Download a file (image)
print("6. File Download:")
img_url = "https://images6.alphacoders.com/131/thumb-1920-1312386.jpeg"
img_response = httpx.get(img_url)
with open("image.jpg", "wb") as f:
    f.write(img_response.content)
print("Image saved as image.jpg")
print()

# 7. Handling errors (404, etc.)
print("7. Error Handling:")
bad_response = httpx.get("https://jsonplaceholder.typicode.com/unknown")
if bad_response.status_code != 200:
    print("Error:", bad_response.status_code)
else:
    print("Content:", bad_response.text)
print()

# 8. Inspecting headers & other metadata
print("8. Inspecting Headers:")
print("Content-Type:", response.headers.get('Content-Type'))
print("Encoding:", response.encoding)
print()
