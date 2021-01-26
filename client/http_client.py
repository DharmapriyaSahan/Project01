import requests
import json

def login():
    url = 'http://127.0.0.1:8083/login'
    response = requests.post(url, json=payload, auth=('user', 'secret'), timeout=5)
    if (response.status_code == 200):
        print("Login success!")
    elif (response.status_code == 404):
        print("Result not found!")
    else:
        print(response.status_code)
    return response

try:
    payload = {"name": "java application","app" : "Java","version" : "2.0"}
    url = 'http://127.0.0.1:8083/api/v1/app/?appid=2'
    login_res = login()
    if (login_res.status_code == 200):
        token=login_res.json()
        print('Your login token : ' + token['token'])
        headers = {"token": token['token']}
        response = requests.post(url, json=payload, headers=headers, timeout=5)
        if (response.status_code == 200):
            print("The request was a success!")
        elif (response.status_code == 404):
            print("Result not found!")
        else:
            print(response.status_code)

except requests.exceptions.HTTPError as errhttp:
    print(errhttp)
except requests.exceptions.ConnectionError as errconn:
    print(errconn)
except requests.exceptions.Timeout as errtout:
    print(errtout)
except requests.exceptions.RequestException as errreq:
    print(errreq)
