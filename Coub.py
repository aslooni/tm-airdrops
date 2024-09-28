import requests  

 
headers = {  
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjNlZjc0NmZmOGNjZTU2ZTMyOWU1YjIxY2QzYWU5YTBkMTQxNzQ2ODYifQ.eyJleHAiOjE3Mjc2NDI4NTEsImlhdCI6MTcyNzU1NjQ1MSwiaXNzIjoiY291YiIsImF1ZCI6InRvcnVzIiwic3ViIjoiMTcwMTY2ODIifQ.g5hYSHs5GcOSxa5x66OYdJxjy7K0Zp1y9AVnxyodMGtphv9_lB5kAk4F-4ZV0YDo6OMeQn7Wir539LAeaB0htowMzW5srIOD2DP34w85rZyxL7VaPq8kzwsNQymVNSBZgJZe-UX3MOY59STkuLEyVJ7IprFMHykxMKSyae8n6Z8RiYGSS16PAqcFnelVY_VNs-Iv83DFB29qzk2R30WR-Z_9uWn0okOxAF1qq08TbhZnnWF68opjW3WRi4vkuw3Ub09YS43VHsgBhdMoBnG6zWAVlI4CxbykgFM86MEq3b7PkMGQspQMVL6hB6dCl9fXV1haQycfmHltew-SeLqpIg',  
    }  

for i in range(1, 30):  
    url = f'https://rewards.coub.com/api/v2/complete_task?task_reward_id={i}' 
    response = requests.post(url, headers=headers)  
    print(f"Call {i}: {response.status_code}")