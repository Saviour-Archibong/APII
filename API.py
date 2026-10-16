
import requests

url = "https://jsonplaceholder.typicode.com/users/2"
response = requests.get(url)
print(response.status_code)
if response.status_code == 200:
    data = response.json()
    print(data)
    
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    age = data.get("age", "Age not available")
    
    print("Name:", name)
    print("Email:", email)
    print("Phone:", phone)
    print("Age:", age)
    
   
else:
    print("Error: Request failed.")
    
