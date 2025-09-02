#Webserver gateway
import requests #Inviting the elder to your fireplace

#Send a message to a website and get a response
response = requests.get('https://api.github.com')
#Check if it was successful
if response.status_code == 200:
    print('Request was successful')
else:
    print("Request failed:", response.status_code)
#print response
print(response.text)

#Print response headers
print(response.headers)
print(response.headers['Content-Type'])#Type of content returned
print(response.headers['Server'])


