import requests  
import json  

url = "https://api.apiduck.xyz/user-partner-mission/claim"  
headers = {  
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjUxNTQ5NzEsInRpbWVzdGFtcCI6MTcyNzU1NzU2NTk4OCwidHlwZSI6MSwiaWF0IjoxNzI3NTU3NTY1LCJleHAiOjE3MjgxNjIzNjV9.W8f8vAFd3Gev4ln8pP8nz3FG7-zamaFHYT0HCMvbe3Y",  
    "content-type": "application/json",  
}  

# 727
for i in range(727, 800):  
    data = {"partner_mission_id": i}  
    response = requests.post(url, headers=headers, data=json.dumps(data))  
    print(f"Request {i}: {response.text}")