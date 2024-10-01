import requests  
import json  

url = "https://api.apiduck.xyz/user-partner-mission/claim"  
headers = {  
    "authorization": "Bearer $Token",  
    "content-type": "application/json",  
}  

# 681
for i in range(1, 681):  
    data = {"partner_mission_id": i}  
    response = requests.post(url, headers=headers, data=json.dumps(data))  
    print(f"Request {i}: {response.text}")