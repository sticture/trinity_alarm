import requests
import json

#b'{"access_token":"f6ff9a8c-370e-4c85-b587-d038496e90ae","token_type":"bearer","refresh_token":"9bd04ebc-dc16-4ea0-a3eb-dc9b47daf906","expires_in":64619,"scope":"read write"}'
def get_token():
    url = 'https://tcocapp.trinityiot.in/HTTPProtAdaptorService/oauth/token'
    headers = {
            'Authorization': 'Basic dHJpbml0eS1jbGllbnQ6dHJpbml0eS1zZWNyZXQ=', 
            'Content-Type': 'application/x-www-form-urlencoded'
            }
    
    data = {
            'username':'trinity',
            'password':'trinity@123',
            'grant_type':'password',
            }
    r = requests.post(url, headers=headers, data=data)
    print(r.content)
    token = json.loads(r.content)['access_token']
    return token

TOKEN = get_token()
#ALGO_LIST = ('waving_hands', 'violence') #, 'clothing', 'crowd', 'face', 'loiter', 'mask', 'sociald', 'vehicle', 'violence')
ALGO_LIST = ('451','289','253','208','292','281','279','275','268','266','262','261','501')    
def send1(alert, token):
    url = 'https://tcocapp.trinityiot.in/HTTPProtAdaptorService/rest/VMSServices/VMSAnalyticsAlerts/32'
    headers = {
            'Authorization': f'bearer {token}',
            'Content-Type': 'application/json',
            'deviceId': '1'
            }
    data = {
        "deviceId": 1,
        "eventTime": alert['time'],
        "alertMessage": alert['alert_type'],
        "eventType": ALGO_LIST.index(alert['alert_type']),
        "severity": None,
        "geocoordinates":{
            "latitude":None,
            "longitude":None,
            "location":None
            },
        "visualInfo": {
            "imageUrl":[
                alert['img_url']
                ],
            "videoUrl": [
                alert['video_url']
                ]
            },
        "objectDetails": alert['data']
        }
    
    data = json.dumps(data)
    
    r = requests.post(url, headers=headers, data=data)
#    print(r.content)
    return r

class Sender:
    def __init__(self):
        #self.token = get_token()
        self.token = TOKEN

    def send(self, alert):
        if alert['alert_type'] not in ('451','289','253','208','292','281','279','275','268','266','262','261','501'): # ('waving_hands','violence'): #no_helmet', 'loiter', 'mask', 'sociald','violence'):
            return
        global TOKEN
        r = send1(alert, self.token)
        print(f"attempt post 1:{r}")
        r = json.loads(r.content)
        if 'error' in r and r['error'] == 'invalid_token':
            self.token = TOKEN
            r = send1(alert, self.token)
            print(f"attempt post 2:{r}")
            r = json.loads(r.content)
            if 'error' in r and r['error'] == 'invalid_token':
                self.token = get_token()
        return r
            


if __name__ == '__main__':
    sender = Sender()
    sender.token = 0
    alert = {
            'alert_type':'208',
            'time':'0',
            'img_url':'0',
            'video_url':'0',
            'data':{}
            }

    for i in range(3):
        r = sender.send(alert)
        print(r)


