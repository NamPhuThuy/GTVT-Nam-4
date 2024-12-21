import gzip
import json
import urllib.request
import requests

# Example 1.1: Simple GET request
def simple_html_request(urlString):
    response = urllib.request.urlopen(urlString)
    html_data = response.read().decode("utf-8")
    print(html_data)

# Example 1.2: Simple GET request with error handle
def error_handle_html_request(urlString):
    try:
        with urllib.request.urlopen(urlString) as response:
            print(response.status)
            html_data = response.read().decode("utf-8")
            print(html_data)
    except urllib.error.URLErorr as e:
        print(f"Error fetching webpage: {e}")
        return None

# Method 1: Simple POST request with JSON data
def simple_push_data(url_string):
    """Basic POST request with JSON data"""
    data = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_API_TOKEN"
    }

    try:
        response = requests.post(url_string, json=data) # POST request to JSONPlaceholder
        # response = requests.post(url_string, data = json.dumps(data), headers=headers)
        
        response.raise_for_status() # Check if the request was successful

        print('Response Status Code:', response.status_code)
        print('Response JSON:', response.json())

    except requests.exceptions.RequestException as e:
        print('Error occurred:', e)

def push_multiple_datas(url_string):
    data_list = [
        {"title": "numeric", "body": 42, "userId": 2},
        {"title": "string", "body": "Hello, World!", "userId": 2},
        {"title": "mixed", "body": [1, "two", 3.0], "userId": 1}
    ]

    try:
        response = requests.post(url_string, json=data_list)
        response.raise_for_status()
        print("Multiple data points pushed successfully!")
        print("Full response:", response.text)
        
    except requests.exceptions.RequestException as e:
        print("Error pushing data:", e)

def get_posts(url_string):
    try:
        response = requests.get(url_string) # Perform GET request
        response.raise_for_status() # Raise an exception for bad status codes

        posts = response.json() # Parse JSON response
        print(f"Total posts retrieved: {len(posts)}")

        # Print details of first few posts
        print("\nFirst 3 Posts:")
        for post in posts[:3]:
            print(f"ID: {post['id']}")
            print(f"Title: {post['title']}")
            print(f"User ID: {post['userId']}")
            print("---")

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

def basic_add_header():
    req = urllib.request.Request('http://google.com')

    # req.add_header("Accept-Language", "en")
    # response = urllib.request.urlopen(req)
    # print(*response)

    req.add_header("Accept-Encoding", "gzip")
    response = urllib.request.urlopen(req)
    data = gzip.decompress(response.read())

    print(data)
    # print(response.getheaders())

if __name__ == "__main__" :
    # URL 
    url_string = "https://www.example.com"
    url_string_2 = "https://jsonplaceholder.typicode.com/posts"
    # simple_html_request(urlString)
    # error_handle_html_request(urlString)
    
    
    # PUSH DATA
    # simple_push_data(url_string_2)
    # push_multiple_datas(url_string_2)
    
    # GET DATA
    get_posts(url_string_2)