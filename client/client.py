import requests

try:
    session = requests.Session()
    response = session.post('http://api/v1/app/{appid}?token=<>', timeout=5)
    if (response.status_code == 200):
        print("The request was a success!")
    elif (response.status_code == 404):
        print("Result not found!")

except requests.exceptions.HTTPError as errhttp:
    print(errhttp)
except requests.exceptions.ConnectionError as errconn:
    print(errconn)
except requests.exceptions.Timeout as errtout:
    print(errtout)
except requests.exceptions.RequestException as errreq:
    print(errreq)
