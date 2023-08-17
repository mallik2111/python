import json
import requests

"""
Modify these please
"""
username = "admin"
password = "VMwar3!!"

ip_addr =  "10.234.137.158"
endpoints = "/api/mo/sys.json"
payload = None
def aaa_login(username, password, ip_addr):
    payload = {
        'aaaUser' : {
            'attributes' : {
                'name' : username,
                'pwd' : password
                }
            }
        }
    url = "http://" + ip_addr + "/api/aaaLogin.json"
    auth_cookie = {}

    response = requests.request("POST", url, data=json.dumps(payload))
    if response.status_code == requests.codes.ok:
        data = json.loads(response.text)['imdata'][0]
        token = str(data['aaaLogin']['attributes']['token'])
        auth_cookie = {"APIC-cookie" : token}

    print ()
    print ("aaaLogin RESPONSE:")
    print (json.dumps(json.loads(response.text), indent=2))

    return response.status_code, auth_cookie


def aaa_logout(username, ip_addr, auth_cookie):
    payload = {
        'aaaUser' : {
            'attributes' : {
                'name' : username
                }
            }
        }
    url = "http://" + ip_addr + "/api/aaaLogout.json"

    response = requests.request("POST", url, data=json.dumps(payload),
                                cookies=auth_cookie)

    print ()
    print ("aaaLogout RESPONSE:")
    print (json.dumps(json.loads(response.text), indent=2))
    print ()


def get(ip_addr, auth_cookie, url, payload):
    response = requests.request("GET", url, data=json.dumps(payload),
                                cookies=auth_cookie)

    print ()
    print ("GET RESPONSE:")
    print (json.dumps(json.loads(response.text), indent=2))


if __name__ == '__main__':
    status, auth_cookie = aaa_login(username, password, ip_addr)
    if status == requests.codes.ok:
        url = "http://" + ip_addr + endpoints 
        get(ip_addr, auth_cookie, url, payload)
        aaa_logout(username, ip_addr, auth_cookie)